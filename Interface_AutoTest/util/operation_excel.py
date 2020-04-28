#coding=utf-8

import xlrd
from xlutils.copy import copy
import xlrd
class OperationExcel():

    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheetid = sheet_id
           
        else:
            self.file_name = "../dataconfig/interface.xlsx"
            self.sheetid = 0
        self.data = self.read_exceldata()

    def read_exceldata(self):
        data = xlrd.open_workbook(self.file_name)
        sheet_num = data.sheets()[self.sheetid]
        return sheet_num

    #获取单元格的行数
    def get_lines(self):
        return self.data.nrows

    #获取某一个单元格的内容
    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)

    #写入数据
    def write_value(self,row,col,value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)

if __name__ == "__main__":
    oe = OperationExcel()
    print(oe.get_lines())
    print(oe.get_cell_value(1,1))
