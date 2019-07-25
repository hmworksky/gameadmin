import requests


class Tool:

    @classmethod
    def merge_dict_in_the_list(cls, data):
        """合并列表中的字典，成为一个新字典"""
        temp = {}
        for value in data:
            temp.update(value)
        return temp

    @classmethod
    def request_(cls, _request, url, data=None):
        if _request == requests.post:
            res = _request.post(url, data=data).content
        else:
            res = _request.get(url, params=data).content
        return res
