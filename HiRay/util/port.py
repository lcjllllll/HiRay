#coding=utf-8
from util.dos_cmd import DosCmd
class Port:

    def port_is_used(self,port_num):
        """判断端口是否被占用 默认为空flag=None"""
        flag = None
        self.dos = DosCmd()
        result = self.dos.excute_cmd_result('netstat -ano | findstr '+str(port_num))
        if len(result)>0:
            flag = True
        else:
            flag = False
        return flag

    def create_port_list(self,start_port,device_list):
        """生成可用端口
        需要的参数：start_port(整型),device_list
        """
        port_list = []
        if device_list != None:
            while len(port_list)!=len(device_list):
                if self.port_is_used(start_port)!=True:
                    port_list.append(start_port)
                start_port =start_port+1
            return port_list
        else:
            print("生成可用端口失败")
            return None






if __name__ == '__main__':
    port = Port()
    print(port.port_is_used('8080'))
    li = [1,2,3,4,5]
    print(port.create_port_list(4721,li))

