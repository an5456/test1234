# -*- coding: utf-8 -*-
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base.run_method import RunMethod
from data.depend_data import DependData
from data.get_data import GetData
from log.get_log import UserLog
from util.CommoUtil import CommonUtil
from util.operation_json import OperationJson
from util.write_cookies import WriteCookies


class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.is_contain = CommonUtil()
        self.log = UserLog()
        self.logger = self.log.get_log()

    # 执行程序
    def go_no_run(self):
        rows_conut = self.data.get_case_lines()  # 获取行数

        for i in range(1, rows_conut):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_url(i)
                case_name = self.data.get_case_name(i)
                method = self.data.get_request_way(i)  # 获取请求的方法
                request_data = self.data.get_json_data(i)  # 获取请求数据
                data_type = self.data.get_data_type(i)
                cookie = self.data.get_is_cookies(i)  # 获取cookies
                expect = self.data.get_expect(i)  # 获取预期结果
                depend_case = self.data.get_depend_case_id(i)  # 获取依赖的caseid
                if depend_case is not None:
                    # 获取替换请求字段
                    depend_key = self.data.get_depned_key(i)
                    # 获取依赖的响应数据
                    self.depend_data = DependData(depend_case)
                    depend_response_data = self.depend_data.get_depned_value(i)
                    split = len(depend_key.split(">"))  # 切割替换的字段
                    # 根据请求字段的个数替换
                    for y in range(0, split):
                        re = depend_key.split(">")
                        request_data[re[y]] = depend_response_data[y]
                if cookie == 'write':
                    res = self.run_method.run_main(method, url, request_data)
                    op_cookie = WriteCookies(res)  # 获取cookies
                    op_cookie.write_cookie()  # 写入cook ies
                elif cookie == 'yes':
                    father_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
                    file_path = os.path.join(father_path, '金城-cookies.json')
                    get_cookies = OperationJson(file_path)

                    cooki = get_cookies.get_data('accessToken')
                    request_data['accessToken'] = cooki
                    res = self.run_method.run_main(method, url, request_data, data_type)

                else:
                    father_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
                    file_path = os.path.join(father_path, '金城-cookies.json')
                    get_cookies = OperationJson(file_path)
                    cooki = get_cookies.get_data('accessToken')
                    request_data['accessToken'] = cooki
                    res = self.run_method.run_main(method, url, request_data)

                if self.is_contain.is_contain(expect, res):
                    self.data.write_data(i, 'pass')
                    # self.logger.info("第" + str(i) + "个case-->" + case_name + ": \033[31m测试通过\033[0m")
                    self.logger.info("第%s 个case-->%s: 测试通过" % (str(i), case_name))
                    self.logger.info("url--> " + url)
                    self.logger.info("request_data-->" + str(request_data))
                    self.logger.info("response_data-->" + res)
                    print("第" + str(i) + "个case-->" + case_name + ": \033[32m测试通过\033[0m")
                    # print(res)
                else:
                    self.data.write_data(i, res)
                    self.logger.info("第" + str(i) + "个case-->" + case_name + ": 测试失败")
                    self.logger.info("url--> " + url)
                    self.logger.info("request_data-->" + str(request_data))
                    self.logger.info("response_data-->" + res)
                    # print("第" + str(i) + "个case-->" + "\033[35m测试失败\033[0m")
                    print("\033[35m第%s 个case-->%s: 测试失败\033[0m" % (str(i), case_name))
                    # print(res)


if __name__ == '__main__':
    run = RunTest()
    run.go_no_run()
