import time
import requests
from django.http import HttpResponse
from apps.autoAdmin.models import MockServer
from apps.autoAdmin.utils.tools import Tool


def mock_server(request):
    path = request.get_full_path()
    print(path)
    request_path = path.split('mock/')[1:][0]
    print(request_path)
    print('request_data:{}\n'.format(request.GET))
    result = MockServer.objects.filter(url_info__contains=request_path).values()
    if not result:
        return HttpResponse('请求地址未配置')

    # 列表转化为字典
    result = result[0]
    request_type = result['request_type']
    return_data = result['return_value']
    timeout = result['timeout']
    print('timeout', timeout)
    java_url = result['url_info']

    request_data = request.GET
    java_request = requests.get

    # 判断请求类型
    if request_type not in range(1, 5):
        return HttpResponse('请求地址未配置')

    if request.method == 'POST':
        request_data = request.POST
        java_request = requests.post

    # 该接口来源过滤
    if request_type == 1:
        time.sleep(timeout)
        return HttpResponse('continue')

    # 返回指定结果
    elif request_type == 2:
        time.sleep(timeout)
        return HttpResponse(return_data)

    # 继续请求JAVA获取JAVA结果
    elif request_type == 3:
        java_result = Tool.request_(java_request, java_url, request_data)
        return HttpResponse(java_result)

    # 继续请求JAVA返回指定结果
    elif request_type == 4:
        Tool.request_(java_request, java_url, request_data)
        return HttpResponse(return_data)


