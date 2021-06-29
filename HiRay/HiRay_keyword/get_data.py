#coding=utf-8
from util.opera_excel import OperaExcel
class GetData:
    def __init__(self):
        self.opera_excel =OperaExcel()

    def get_case_lines(self):
        """为了整洁"""
        lines = self.opera_excel.get_lines()
        return lines
    def get_handle_step(self,row):
        """获取操作步骤里面的操作方法名"""
        method_name = self.opera_excel.get_cell(row,3)
        return method_name

    def get_element_key(self,row):
        """获取操作元素的key"""
        element_key = self.opera_excel.get_cell(row,4)
        if element_key == '':
            return None
        return element_key

    def get_handle_value(self,row):
        """q获取操作值"""
        handle_value = self.opera_excel.get_cell(row,5)
        if handle_value == '':
            return None
        return handle_value

    def get_expect_element(self,row):
        """预期元素"""
        expect_element = self.opera_excel.get_cell(row,7)
        if expect_element == '':
            return None
        return expect_element

    def get_assert(self,row):
        '''
        获取是否运行元素
        :param row:
        :return:
        '''
        assert_element = self.opera_excel.get_cell(row,6)
        if assert_element == '':
            return None
        return assert_element

    def get_expect_handle(self,row):
        '''
        获取预期步骤
        :param row:
        :return:
        '''
        expect_step = self.opera_excel.get_cell(row,8)
        if expect_step =='':
            return None
        return expect_step

    def write_value(self,row,value):
        OperaExcel().write_value(row,value)





if __name__ == '__main__':
    get = GetData()
    i=10
    get.write_value(i,"pass")
    # print(get.get_element_key(8))
    # print(get.get_case_lines())
    # lines = get.get_case_lines()
    # for i in range(1, lines):
    #     # 不需要第0行  是标题行
    #     # print(i)
    #     handle_step = get.get_handle_step(i)  # 操作步骤
    #     print(handle_step)