# -*- coding: utf-8 -*-
from base.run_method import RunMethod
from data.get_data import GetData
from util.operation_excel import OperationExcel
import json
from jsonpath_rw import jsonpath, parse

from util.operation_json import OperationJson


class DependData:
    def __init__(self, case_id):
        self.casi_id = case_id
        self.operation = OperationExcel()
        self.data = GetData()

    # 根据caseid获取行的内容
    def get_lines_data(self):
        self.operation.get_rows_data(self.casi_id)

    # 执行依赖测试case，获取结果
    def run_depend_case(self):
        run_method = RunMethod()
        row_num = self.operation.get_row_num(self.casi_id)  # 获取行号
        request_data = self.data.get_json_data(row_num)  # 获取请求数据
        request_method = self.data.get_request_way(row_num)  # 获取请求方法
        url = self.data.get_url(row_num)
        cookie = self.data.get_is_cookies(row_num)
        if cookie == 'yes':
            operation = OperationJson('../data/scm-cookies.json')
            cookie = operation.get_data('SESSION')
            cookies = {
                "SESSION": cookie
            }
            res = run_method.run_main(request_method, url, request_data, cookie)
        else:
            res = run_method.run_main(request_method, url, request_data)
        return json.loads(res)

    # 获取依赖case的值
    def get_depned_value(self, row):
        depend_data = self.data.get_depend_data(row)  # 获取匹配的依赖字段
        response_data = self.run_depend_case()  # 获取响应数据
        json_exe = parse(depend_data)  # 根据depend_data去匹配对应的值
        madel = json_exe.find(response_data)  # 查找
        return [math.value for math in madel]  # 返回找到的值


if __name__ == '__main__':
    depent = DependData("Imooc-01")
    print(depent.run_depend_case())
