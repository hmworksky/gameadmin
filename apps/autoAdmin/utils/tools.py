class Tool:

    @classmethod
    def merge_dict_in_the_list(cls, data):
        """合并列表中的字典，成为一个新字典"""
        temp = {}
        for value in data:
            temp.update(value)
        return temp
