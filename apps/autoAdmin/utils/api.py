import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mygame.settings")
django.setup()
from apps.autoAdmin.utils.tools import Tool
from apps.autoAdmin.utils.ctrl import InterfaceDetailCtrl


class InterfaceValidate:
    """接口字段校验规则[对外方法需要以generate开头]
    genre:
    (0, "string"),
    (1, "int"),
    (2, "float"),
    (3, "bool"),
    (4, "double")
    """

    def __set_return_value(self, field, value=None):
        temp = dict()
        name = field['name']
        temp[name] = value
        return temp

    def generate_more_than_length_field(self, field):
        """生成超过长度的字段值"""

        # 获取比最大长度大一个的长度的值
        need_length = field['length'] + 1
        need_value = '8' * need_length

        # 判断是否是数字，是数字就转成数字类型
        if field['genre'] in (1, 2, 4):
            need_value = int(need_value)

        return self.__set_return_value(field, need_value)

    def generate_error_type_field(self, field):
        """该字段生成错误的数据类型"""
        value = '<' if field['genre'] == 0 else 'test'
        return self.__set_return_value(field, value)

    def generate_null_value_field(self, field):
        """该字段生成空值"""
        return self.__set_return_value(field, '')

    def generate_none_value_field(self, field):
        """该字段生成None不传递"""
        return self.__set_return_value(field)


class GenerateAutoCase:

    def __init__(self, interface_id, is_auto=False):
        self.interface_detail = InterfaceDetailCtrl(interface_id)
        self.validate = InterfaceValidate()
        self.is_auto = is_auto

    def generate_success_value_field(self, field):
        """该字段生成正常值"""

        # 先生成值
        need_value = field['length'] * '8'

        # 判断是否是布尔类型
        if field['genre'] == 3:
            need_value = 1

        return {field['name']: need_value}

    def generate_single_field(self, field):
        """获取单个字段的错误值"""
        res = []
        for func in dir(self.validate):
            if func.startswith('generate'):
                value = getattr(self.validate, func)(field)
                res.append(value)
        return res

    def generate_all_field(self):
        """生成该接口所有的字段用例"""
        field_list = self.interface_detail.get_all_field()
        result = []
        for index, field_name in enumerate(field_list):
            other_field = [x for i, x in enumerate(field_list) if i != index]

            other_field_sucess = [self.generate_success_value_field(x) for x in other_field]
            other_field_sucess = Tool.merge_dict_in_the_list(other_field_sucess)

            # 获取该字段所有的异常情况
            self_field_fail = self.generate_single_field(field_name)

            # 将其它字段正常值添加进来
            for fail_field in self_field_fail:
                fail_field.update(other_field_sucess)
                result.append(fail_field)

        # 获取所有字段都成功的情况
        all_success = [self.generate_success_value_field(x) for x in field_list]
        all_success = Tool.merge_dict_in_the_list(all_success)
        result.append(all_success)

        return result


if __name__ == '__main__':
    from pprint import pprint
    g = GenerateAutoCase(1)
    field = g.interface_detail.get_all_field()
    res = g.generate_all_field()
    pprint(res)


