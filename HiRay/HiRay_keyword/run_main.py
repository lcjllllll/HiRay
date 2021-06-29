#coding=utf-8
import sys
sys.path.append('D:\PyWork\HiRay\HiRay') #当前工程目录
#No module named '__main__.action_method'; '__main__' is not a package  ===>你添加当前工程目录的话
from HiRay_keyword.action_method import ActionMethod
from HiRay_keyword.get_data import GetData
from util.server import Server
# from util.get_by_local import GetByLocal

class RunMain:
    def run_method(self):
        server = Server()
        server.main()
        data = GetData()
        action_method = ActionMethod()
        lines = data.get_case_lines()


        for i in range(1,lines):
            #不需要第0行  是标题行
            handle_step = data.get_handle_step(i)   #操作步骤
            #拿到步骤如何在action_method中执行：进行反射getattr(对象，操作值)
            element_key = data.get_element_key(i)   #元素
            # print("element_key-------------------"+element_key)
            handle_value = data.get_handle_value(i)  #操作值
            expect_key = data.get_expect_element(i)  #预期元素
            expect_step = data.get_expect_handle(i)  #预期步骤
            get_text=data.get_assert(i) #校验元素
            # 如何校验
            a = action_method.get_text(get_text)

            excute_method = getattr(action_method, handle_step)  # 操作步骤  此时不是函数 需要加括号才是
            if element_key != None:
                excute_method(element_key, handle_value)  # 元素 值
            else:
                # sleep
                excute_method(handle_value)  # 值



            if expect_step !=None:  #预期步骤
                expect_result = getattr(action_method,expect_step)
                result = expect_result(expect_key)  # 获取预期元素
                # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                # print(expect_key)
                # print(type(expect_key))
                if expect_key==a:
                    print("-----------------------yes")
                    data.write_value(i,"pass")
                elif result:
                    print("-----------------------yes")
                    data.write_value(i, "pass")
                else:
                    print("-----------------------no")
                    data.write_value(i,"fail")

if __name__ == '__main__':
    run_main = RunMain()
    run_main.run_method()
