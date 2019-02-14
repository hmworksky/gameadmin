import os
import sys
import socket
import json
import time
import unittest
from websocket._exceptions import WebSocketTimeoutException, WebSocketAddressException, WebSocketConnectionClosedException
from websocket import create_connection
from unittest.case import SkipTest
from django.core.exceptions import ObjectDoesNotExist
from ApiManager.models import TestCaseInfo, ModuleInfo, ProjectInfo, DebugTalk, TestSuite
from ApiManager.utils.testcase import dump_python_file, dump_yaml_file
from httprunner.runner import Runner
from httprunner.task import HttpRunner
from httprunner.task import init_test_suites
from httprunner import exceptions, logger, response, utils

from httprunner.report import get_platform, get_summary, HtmlTestResult
from httprunner.utils import print_output, load_dot_env_file
PRIMUS_URL = "ws://tst-bubble-stg126.1768.com/primus?userId=2038983919"


class MySocket:
    def __init__(self, socket_url=PRIMUS_URL):

        self.socket_url = socket_url
        self.ws = self.create_socket(self.socket_url)
        # print("socket_url:##########", socket_url)

    @staticmethod
    def create_socket(socket_url):
        try:
            ws = create_connection(socket_url, sockopt=((socket.IPPROTO_TCP, socket.TCP_NODELAY, 1),), timeout=10)
        except WebSocketAddressException:
            ws.close()
        return ws

    def result(self, message):
        message = str(message).replace("'", '"')
        # print("进入发送命令，发送的值是", message)
        try:
            self.ws.send(message)
            # print("发送成功，开始接受参数...")
            return_data = self.ws.recv()
            # print("接收的数据为：", return_data)
            return json.loads(return_data)
        except WebSocketTimeoutException:
            self.ws.close()
            return {}

        except WebSocketConnectionClosedException:
            self.ws = self.create_socket(self.socket_url)
            return {}


class SocketSession:
    def __init__(self, base_url):
        self.base_url = base_url
        self.init_meta_data()

    def request(self, method, url, name=None, **kwargs):

        kwargs = kwargs["data"]
        kwargs["params"] = eval(kwargs["params"])
        url = self.base_url+url

        self.meta_data["request"]["url"] = url
        self.meta_data["request"]["method"] = method
        self.meta_data["request"]["start_timestamp"] = time.time()

        # prepend url with hostname unless it's already an absolute URL

        kwargs.setdefault("timeout", 120)

        sock = MySocket(url)
        data = sock.result(kwargs)

        # record the consumed time
        self.meta_data["response"]["response_time_ms"] = \
            round((time.time() - self.meta_data["request"]["start_timestamp"]) * 1000, 2)
        self.meta_data["request"]["content_size"] = sys.getsizeof(data)
        return data

    def init_meta_data(self):
        """ initialize meta_data, it will store detail data of request and response
        """
        self.meta_data = {
            "request": {
                "url": "N/A",
                "method": "N/A",
                "headers": {},
                "start_timestamp": None
            },
            "response": {
                "status_code": "N/A",
                "headers": {},
                "content_size": "N/A",
                "response_time_ms": "N/A",
                "elapsed_ms": "N/A",
                "encoding": None,
                "content": None,
                "content_type": ""
            }
        }


class NewRunner(HttpRunner):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def run(self, path_or_testsets, mapping=None, http_client_session=None):
        """ start to run test with varaibles mapping
        @param path_or_testsets: YAML/JSON testset file path or testset list
            path: path could be in several type
                - absolute/relative file path
                - absolute/relative folder path
                - list/set container with file(s) and/or folder(s)
            testsets: testset or list of testset
                - (dict) testset_dict
                - (list) list of testset_dict
                    [
                        testset_dict_1,
                        testset_dict_2
                    ]
        @param (dict) mapping:
            if mapping specified, it will override variables in config block
        """
        try:
            test_suite_list = init_test_suites(path_or_testsets, mapping, http_client_session)
        except exceptions.TestcaseNotFound:
            logger.log_error("Testcases not found in {}".format(path_or_testsets))
            sys.exit(1)

        self.summary = {
            "success": True,
            "stat": {},
            "time": {},
            "platform": get_platform(),
            "details": []
        }

        def accumulate_stat(origin_stat, new_stat):
            """ accumulate new_stat to origin_stat
            """
            for key in new_stat:
                if key not in origin_stat:
                    origin_stat[key] = new_stat[key]
                elif key == "start_at":
                    # start datetime
                    origin_stat[key] = min(origin_stat[key], new_stat[key])
                else:
                    origin_stat[key] += new_stat[key]

        for test_suite in test_suite_list:
            result = self.runner.run(test_suite)
            test_suite_summary = get_summary(result)

            self.summary["success"] &= test_suite_summary["success"]
            test_suite_summary["name"] = test_suite.config.get("name")
            test_suite_summary["base_url"] = test_suite.config.get("request", {}).get("base_url", "")
            test_suite_summary["output"] = test_suite.output
            print_output(test_suite_summary["output"])

            accumulate_stat(self.summary["stat"], test_suite_summary["stat"])
            accumulate_stat(self.summary["time"], test_suite_summary["time"])

            self.summary["details"].append(test_suite_summary)

        return self



def switch_session(method, base_url):
    """
    根据不同的协议调用不同的请求客户端
    :return:
    """
    session = SocketSession(base_url)
    return session if method in ["PRIMUS", "SOCKETIO"] else None


def run_by_single(index, base_url, path):
    """
    加载单个case用例信息
    :param index: int or str：用例索引
    :param base_url: str：环境地址
    :return: dict
    """
    config = {
        'config': {
            'name': '',
            'request': {
                'base_url': base_url
            }
        }
    }

    testcase_list = []

    testcase_list.append(config)

    try:
        obj = TestCaseInfo.objects.get(id=index)
    except ObjectDoesNotExist:
        return testcase_list

    include = eval(obj.include)
    request = eval(obj.request)
    name = obj.name
    project = obj.belong_project
    module = obj.belong_module.module_name

    config['config']['name'] = name

    testcase_dir_path = os.path.join(path, project)

    if not os.path.exists(testcase_dir_path):
        os.makedirs(testcase_dir_path)

        try:
            debugtalk = DebugTalk.objects.get(belong_project__project_name=project).debugtalk
        except ObjectDoesNotExist:
            debugtalk = ''

        dump_python_file(os.path.join(testcase_dir_path, 'debugtalk.py'), debugtalk)

    testcase_dir_path = os.path.join(testcase_dir_path, module)

    if not os.path.exists(testcase_dir_path):
        os.mkdir(testcase_dir_path)

    for test_info in include:
        try:
            if isinstance(test_info, dict):
                config_id = test_info.pop('config')[0]
                config_request = eval(TestCaseInfo.objects.get(id=config_id).request)
                config_request.get('config').get('request').setdefault('base_url', base_url)
                config_request['config']['name'] = name
                testcase_list[0] = config_request
            else:
                id = test_info[0]
                pre_request = eval(TestCaseInfo.objects.get(id=id).request)
                pre_request["test"]["request"]["url"] = base_url+pre_request["test"]["request"]["url"]
                testcase_list.append(pre_request)

        except ObjectDoesNotExist:
            return testcase_list

    if request['test']['request']['url'] != '':
        testcase_list.append(request)

    dump_yaml_file(os.path.join(testcase_dir_path, name + '.yml'), testcase_list)


def run_by_suite(index, base_url, path):
    obj = TestSuite.objects.get(id=index)

    include = eval(obj.include)

    for val in include:
        run_by_single(val[0], base_url, path)



def run_by_batch(test_list, base_url, path, type=None, mode=False):
    """
    批量组装用例数据
    :param test_list:
    :param base_url: str: 环境地址
    :param type: str：用例级别
    :param mode: boolean：True 同步 False: 异步
    :return: list
    """

    if mode:
        for index in range(len(test_list) - 2):
            form_test = test_list[index].split('=')
            value = form_test[1]
            if type == 'project':
                run_by_project(value, base_url, path)
            elif type == 'module':
                run_by_module(value, base_url, path)
            elif type == 'suite':
                run_by_suite(value, base_url, path)
            else:
                run_by_single(value, base_url, path)

    else:
        if type == 'project':
            for value in test_list.values():
                run_by_project(value, base_url, path)

        elif type == 'module':
            for value in test_list.values():
                run_by_module(value, base_url, path)
        elif type == 'suite':
            for value in test_list.values():
                run_by_suite(value, base_url, path)

        else:
            for index in range(len(test_list) - 1):
                form_test = test_list[index].split('=')
                index = form_test[1]
                run_by_single(index, base_url, path)


def run_by_module(id, base_url, path):
    """
    组装模块用例
    :param id: int or str：模块索引
    :param base_url: str：环境地址
    :return: list
    """
    obj = ModuleInfo.objects.get(id=id)
    test_index_list = TestCaseInfo.objects.filter(belong_module=obj, type=1).values_list('id')
    for index in test_index_list:
        run_by_single(index[0], base_url, path)


def run_by_project(id, base_url, path):
    """
    组装项目用例
    :param id: int or str：项目索引
    :param base_url: 环境地址
    :return: list
    """
    obj = ProjectInfo.objects.get(id=id)
    module_index_list = ModuleInfo.objects.filter(belong_project=obj).values_list('id')
    for index in module_index_list:
        module_id = index[0]
        run_by_module(module_id, base_url, path)


def run_test_by_type(id, base_url, path, type):
    if type == 'project':
        run_by_project(id, base_url, path)
    elif type == 'module':
        run_by_module(id, base_url, path)
    elif type == 'suite':
        run_by_suite(id, base_url, path)
    else:
        run_by_single(id, base_url, path)


if __name__ == '__main__':
    url = "ws://tst-bubble-stg126.1768.com/primus?userId=2038983919"
    data = {
                "name": "testcase description",
                "times": 3,
                "variables": [{'haha': 2038983919}],        # optional, override
                "request": {
                    "url": url,
                    "method":"POST",
                    "cmd": "getUserInfo",
                    "params": {"userId":2038983919}
                },
                "extract": [{'myname': 'content.res.data.userId'}],              # optional
                "validate": [{'eq':['content.res.data.userId','hello(2)']}],             # optional
                "setup_hooks": [],          # optional
                "teardown_hooks": []        # optional
            }

    runner = NewRunner(http_client_session=p)
    resul = runner.run(data)
    print(runner.context.testcase_variables_mapping)