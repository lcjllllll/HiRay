#coding = utf-8
from util.dos_cmd import DosCmd
from util.port import Port
from util.write_user_command import WriteUserCommand
import threading
from util.get_by_local import GetByLocal

import time

class Server:
    def __init__(self):
        self.dos = DosCmd()


        self.write_file =WriteUserCommand()
        self.devices_list=self.get_devices()
    def get_devices(self):
        """
        获取设备信息
        :return:
        """
        devices_list=[]
        result_list = self.dos.excute_cmd_result("adb devices")
        if len(result_list)>=2:
            for i in result_list:
                if 'List' in i:
                    continue
                devices_info = i.split('\t')
                if devices_info[1] == 'device':
                    devices_list.append(devices_info[0])
            return devices_list
        else:
            return None


    def create_port_list(self,start_port):
        """
        创建可用端口
        :return:
        """
        port = Port()
        port_list=[]
        port_list = port.create_port_list(start_port,self.devices_list)
        return port_list

    def create_command_list(self,i):
        # appium -p 4700 -bp 4701 -U 127.0.0.1:21503
        write_file = WriteUserCommand()

        commamd_list = []
        appium_port_list = self.create_port_list(4700)
        bootstrap_port_list = self.create_port_list(4900)
        device_list =self.devices_list
        # for i in range(len(device_list)):#不能根据设备的个数写入
        commamd = "appium -p "+str(appium_port_list[i])+" -bp "+str(bootstrap_port_list[i])+" -U "+device_list[i]+" --no-reset --session-override --log D:\\PyWork\\HiRay\\HiRay\\log\\test_HiRay.log"
        commamd_list.append(commamd)
        self.write_file.write_data(i,device_list[i],str(bootstrap_port_list[i]),str(appium_port_list[i]))
        return commamd_list
    def start_server(self,i):
        self.start_list = self.create_command_list(i)
        print(self.start_list)
        self.dos.excute_cmd(self.start_list[0]) #start_server 中start_list是根据线程生成的 每次只有一个

    def kill_server(self):
        server_list = self.dos.excute_cmd_result('tasklist | find "node.exe"')
        if len(server_list)>0:  #证明有服务
            self.dos.excute_cmd("taskkill -F -PID node.exe")  #不需要结果
    def main(self):
        """
        控制执行多少次
        :return:
        """
        self.kill_server()
        self.write_file.clear_data()
        for i in range(len(self.devices_list)):
            appium_start = threading.Thread(target=self.start_server,args=(i,))
            appium_start.start()
            time.sleep(25)


if __name__ == '__main__':
    server = Server()
    # print(server.create_command_list())
    # print(server.get_devices())
    print(server.main())

