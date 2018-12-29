# -*- coding: utf-8 -*-
import data.data_config
from log.get_log import UserLog
from util.operation_excel import OperationExcel
from util.operation_json import OperationJson


class GetData:
    def __init__(self):
        self.operation = OperationExcel()
        log = UserLog()
        self.logger = log.get_log()

    # 获取case的行数
    def get_case_lines(self):
        return self.operation.get_lines()

    # 获取单元格数据
    def get_cell_value(self, row, col):
        self.operation.get_cell_data(row, col)

    # 获取case名称
    def get_case_name(self, row):
        col = int(data.data_config.get_name())
        case_name = self.operation.get_cell_data(row, col)
        if case_name is not None:
            return case_name
        else:
            self.logger.info("用例名称为空")
            return None

    # 获取url
    def get_url(self, row):
        col = int(data.data_config.get_url())
        get_url = self.operation.get_cell_data(row, col)
        if get_url is not None:
            return get_url
        else:
            self.logger.error("url为空")
            return None

    # 获取是否执行
    def get_is_run(self, row):
        flag = None
        col = int(data.data_config.get_is_run())
        is_run = self.operation.get_cell_data(row, col)
        if is_run == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 获取请求方式
    def get_request_way(self, row):
        col = int(data.data_config.get_request_way())
        request_way = self.operation.get_cell_data(row, col)
        if request_way is not None:
            return request_way
        else:
            self.logger.error("请求方式为空")
            return None

    # 获取是否携带cookies
    def get_is_cookies(self, row):
        col = int(data.data_config.get_cookies())
        cookies = self.operation.get_cell_data(row, col)
        if cookies is not None:
            return cookies
        else:
            self.logger.error("cookie为空")
            return None

    # 获取数据类型
    def get_data_type(self, row):
        col = int(data.data_config.get_request_type())
        data_type = self.operation.get_cell_data(row, col)
        if data_type is not None:
            return data_type
        else:
            self.logger.error("请求数据为空")
            return None

    # 获取依赖id
    def get_depend_case_id(self, row):
        col = int(data.data_config.get_depend_id())
        depend_case_id = self.operation.get_cell_data(row, col)
        if depend_case_id == '':
            return None
        else:
            return depend_case_id

    # 获取依赖的数据
    def get_depend_data(self, row):
        col = int(data.data_config.get_depend_data())
        depend_data = self.operation.get_cell_data(row, col)
        if depend_data is not None:
            return depend_data
        else:
            return None

    # 获取请求需要替换的字段
    def get_depned_key(self, row):
        col = int(data.data_config.get_depend_key())
        depned_key = self.operation.get_cell_data(row, col)
        if depned_key is not None:
            return depned_key
        else:
            return None

    # 获取请求数据
    def get_request_data(self, row):
        col = int(data.data_config.get_request_data())
        request_data = self.operation.get_cell_data(row, col)
        if request_data is not None:
            return request_data
        # else:
        #     return None

    # 获取json数据
    def get_json_data(self, row):
        operation = OperationJson()
        json_data = operation.get_data(self.get_request_data(row))
        return json_data

    # 获取预期结果
    def get_expect(self, row):
        col = int(data.data_config.get_expect())
        expect = self.operation.get_cell_data(row, col)
        if expect is not None:
            return expect
        else:
            return None

    # 获取实际结果
    def get_result(self, row):
        col = int(data.data_config.get_result())
        result = self.operation.get_cell_data(row, col)
        if result is not None:
            return result
        else:
            return None

    # 写入结果
    def write_data(self, row, value):
        col = int(data.data_config.get_result())
        self.operation.write_data(row, col, value)


if __name__ == '__main__':
    get_data = GetData()
    print(get_data.get_depend_case_id(1))
