import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mygame.settings")
django.setup()
from apps.autoAdmin.models import InterfaceField


class InterfaceDetailCtrl:

    def __init__(self, interface_id):
        self.interface_id = interface_id

    def get_all_field(self):
        """获取字段表中的所有值"""
        return InterfaceField.objects.filter(interface_id=self.interface_id).all().values()


if __name__ == '__main__':
    interface_detail = InterfaceDetailCtrl(2)
    res = interface_detail.get_all_field()
    print(res)

