# -*- coding: utf-8 -*-
import json
import os

class OperationJson:
    def __init__(self, file_path=None):
        if file_path is None:
            father_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
            self.file_path = os.path.join(father_path, 'login.json')
            # self.file_path = '../data/login.json'
        else:
            self.file_path = file_path
        self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        with open(self.file_path, encoding='utf-8') as fp:
            data = json.load(fp, strict=False)
            return data

    # 根据key获取请求数据
    def get_data(self, key=None):
        data = None
        if key is None:

            data = list(self.data.keys())[0]

        else:
            data = self.data[key]
        return data

    # json写入数据
    def write_data(self, data):
        father_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
        self.file_path = os.path.join(father_path, 'scm-cookies.json')
        with open(self.file_path, 'w') as fp:
            fp.write(json.dumps(data))


if __name__ == '__main__':
    operation = OperationJson('../data/scm-cookies.json')
    print(type(operation.get_data('accessToken')))
    # print(operation.write_data('test112就的撒3'))
    # print(operation.get_data('test'))
