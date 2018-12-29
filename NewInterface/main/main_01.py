from base.run_method import RunMethod
from data.depend_data import DependData
from data.get_data import GetData
from util.CommoUtil import CommonUtil
from util.operation_cookies import OperationCookie
from util.operation_json import OperationJson


class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.is_contain = CommonUtil()

    # 执行程序
    def go_no_run(self, i):
        rows_conut = self.data.get_case_lines()  # 获取行数
        is_run = self.data.get_is_run(i)
        print(is_run)
        if is_run:
            url = self.data.get_url(i)
            method = self.data.get_request_way(i)  # 获取请求的方法
            request_data = self.data.get_json_data(i)  # 获取请求数据
            data_type = self.data.get_data_type(i)
            print(data_type)
            cookie = self.data.get_is_cookies(i)  # 获取cookies
            expect = self.data.get_expect(i)  # 获取预期结果
            result = self.data.get_result(i)
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
                op_cookie = OperationCookie(res)  # 获取cookies
                op_cookie.write_cookie()  # 写入cookies
            elif cookie == 'yes':
                get_cookies = OperationJson('../data/cookies.json')
                cooki = get_cookies.get_data('SESSION')
                cookies = {
                    "SESSION": cooki
                }
                res = self.run_method.run_main(method, url, request_data, cookies, data_type)
            else:
                res = self.run_method.run_main(method, url, request_data)
            if self.is_contain.is_contain(expect, res):
                self.data.write_data(i, 'pass')

            else:
                self.data.write_data(i, 'fail')
                print(res)
            return result


if __name__ == '__main__':
    run = RunTest()
    print(run.go_no_run(1))
