#coding=utf-8
import xlrd
#写excel文件 用 xlwd  但是为了不要覆盖掉
from xlutils.copy import copy
import xlwt
import logging
# excel = xlrd.open_workbook('D:/case/HiRay.xls')
# data = excel.sheets()[0]
# print(data.nrows)
# print(data.cell(3,4).value)
class OperaExcel:
    def __init__(self,file_path=None,i=None):
        if file_path==None:
            self.file_path='../Testcase/HiRay.xls'
        else:
            self.file_path = file_path
        if i==None:
            i=0
        self.excel =self.get_excel()
        self.data = self.get_sheets(i)

    def get_excel(self):
        """获取excel"""
        excel = xlrd.open_workbook(self.file_path,formatting_info=True)
        return excel

    def get_sheets(self,i):
        """获取sheets的内容"""
        tables = self.excel.sheets()[i]
        return tables

    def get_lines(self):
        """获取excel行数"""
        lines = self.data.nrows
        return lines

    def get_cell(self,row,cell):
        """获取值"""
        data = self.data.cell(row,cell).value
        return data
    def write_value(self,row,value):
        read_value = self.excel  #xlrd.open_workbook(self.file_path)

        write_data = copy(read_value)   #复制内容
        write_save = write_data.get_sheet(0)

        #样式
        pattern = xlwt.Pattern()  # Create the Pattern
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
        # May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow,
        # 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown),
        # 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
        style = xlwt.XFStyle()  # Create the Pattern
        style.pattern = pattern  # Add Pattern to Style


        if value=="pass":
            pattern.pattern_fore_colour = 5
            write_save.write(row, 9, value, style)
        elif value=="fail":
            pattern.pattern_fore_colour = 2
            write_save.write(row,9,value,style)  #拿到excel内容
        else:
            logging.error("write_value没找到元素")
        write_data.save(self.file_path)  #必须是xls文件要不打不开"HiRayTest.xls"



if __name__ == '__main__':
    opera = OperaExcel()
    print(opera.get_cell(3,6))
    print(opera.get_lines())

