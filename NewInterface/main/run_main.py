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
                print(expect)
                depend_case = self.data.get_depend_case_id(i)  # 获取依赖的caseid
                print(depend_case)
                # if method != 'post' and method != 'get':
                #     session = GetCookies(url=method, username=cookie, password=data_type, code='1234')
                #     session.get_cookies()
                if depend_case is not None:
                    # 获取替换请求字段
                    depend_key = self.data.get_depned_key(i)
                    # 获取依赖的响应数据
                    self.depend_data = DependData(depend_case)
                    depend_response_data = self.depend_data.get_depned_value(i)
                    print(depend_response_data)
                    if depend_response_data is not None:
                        split = len(depend_key.split(">"))  # 切割替换的字段
                        # 根据请求字段的个数替换
                        for y in range(0, split):
                            re = depend_key.split(">")
                            request_data[re[y]] = depend_response_data[y]

                if cookie == 'write':
                    self.run_method.run_main(url=url, method=method, data_type=data_type)
                    res = 'Aa12345678'

                #     op_cookie = WriteCookies(res)  # 获取cookies
                #     op_cookie.write_cookie()  # 写入cook ies
                elif cookie == 'yes':
                    get_cookies = OperationJson('../data/cookies.json')
                    coo = get_cookies.get_data('SESSION')

                    cooki = {
                                "SESSION": coo
                            }
                    res = self.run_method.run_main(method, url, request_data, cooki, data_type)

                else:
                    # get_cookies = OperationJson('../data/cookies.json')
                    # cooki = get_cookies.get_data('accessToken')
                    # request_data['accessToken'] = cooki
                    res = self.run_method.run_main(method, url, request_data)

                if self.is_contain.is_contain(expect, res):
                    self.data.write_data(i, 'pass')
                    self.logger.info("第" + str(i) + "个case-->" + case_name+": 测试通过")
                    self.logger.info("url--> " + url)
                    self.logger.info("request_data-->" + str(request_data))
                    self.logger.info("response_data-->" + res)
                    print("第" + str(i) + "个case-->" + case_name+": 测试通过")
                    print(res)
                else:
                    self.data.write_data(i, res)
                    self.logger.info("第" + str(i) + "个case-->" + case_name + ": 测试失败")
                    self.logger.info("url--> " + url)
                    self.logger.info("request_data-->" + str(request_data))
                    self.logger.info("response_data-->" + res)
                    print("第" + str(i) + "个case-->" + "测试失败")
                    print(res)


if __name__ == '__main__':
    run = RunTest()
    run.go_no_run()
