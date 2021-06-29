# coding=utf-8
import configparser
# pip install configparser
import random
# 读取localElement.ini的信息
class ReadIni:
    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = 'D:/PyWork/HiRay/HiRay/config/LocalElement.ini'
        else:
            self.file_path = file_path
        self.data = self.read_ini()

    def read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path,encoding='UTF-8')
        return read_ini
        # 通过参数key获取对应的value

    def get_value(self, key, section=None):  # def get_value(self,section=None,key):出错
        if section == None:
            section = 'element'
        try:
            value = self.read_ini().get(section, key)
            return value
        except:
            value = None
        return value

if __name__ == '__main__':
    read_ini = ReadIni()
    print(read_ini.get_value('powerBtn_ba'))






