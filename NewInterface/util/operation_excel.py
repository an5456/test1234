# -*- coding: utf-8 -*-
import sys
import os
import xlrd
from xlutils.copy import copy

sys.path.append('C:\\Users\\Administrator\\PycharmProjects\\NewInterface')


class OperationExcel:
    def __init__(self, file_name=None, sheet_name=None):
        if file_name is not None:
            self.file_name = file_name
            self.sheet_name = sheet_name
        else:
            pwd = os.getcwd()
            father_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
            self.file_name = '../data/interface.xls'
            self.sheet_name = 'Sheet1'
        self.data = self.get_data()

    # 获取Excel数据
    def get_data(self):
        # 获取excel
        data = xlrd.open_workbook(self.file_name)
        # 获取sheet
        sheet = data.sheet_by_name(self.sheet_name)
        return sheet

    # 获取行数
    def get_lines(self):
        return self.data.nrows

    # 获取单元格数据
    def get_cell_data(self, row, col):
        return self.data.cell_value(row, col)

    # excel写入数据
    def write_data(self, row, col, value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(self.sheet_name)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)

    # 根据行号,获取该行的内容
    def get_rows_data(self, case_id):
        row_num = self.get_row_num(case_id)
        row_data = self.get_rows_value(row_num)
        return row_data

    # 获取依赖caseID的行号
    def get_row_num(self, case_id):
        num = 0
        cols_data = self.get_cols_value()
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num = num + 1

    # 获取某一行的内容
    def get_rows_value(self, row):
        return self.data.row_values(row)

    # 获取某一列的内容
    def get_cols_value(self, caseid=None):
        if caseid is not None:
            cols = self.data.col_values(caseid)
        else:
            cols = self.data.col_values(0)
        return cols


if __name__ == '__main__':
    op = OperationExcel()
    print(op.get_cell_data(1, 10))
    print(op.write_data(2, 2, 'test2'))
