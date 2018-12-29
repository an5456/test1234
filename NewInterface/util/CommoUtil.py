class CommonUtil:
    # 字符串a是否存在b中
    def is_contain(self, str_one, str_two):
        flge = None
        if str_one in str_two:
            flge = True
        else:
            flge = False
        return flge