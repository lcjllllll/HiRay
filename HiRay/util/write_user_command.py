#coding=utf-8
import yaml
class WriteUserCommand:
    def read_data(self):
        """
        :return:
        """
        with open("../config/config.yaml") as fr:
            data = yaml.load(fr)
        return data
        # print(data['user_info_0']['bp'])

    def get_value(self,key,port):
        """
        获取value
        :return:
        """
        data = self.read_data()
        value = data[key][port]
        return value

    # def write_data(self,data):
    #     """
    #     写入数据
    #     :param data:
    #     :return:
    #     """
    #     with open("../config/config.yaml","a") as fr:
    #         yaml.dump(data,fr)
    def write_data(self,i,device,bp,port):
        """
        写入数据
        :param data:
        :return:
        """
        data = self.join_data(i,device,bp,port)
        with open("../config/config.yaml","a") as fr:
            yaml.dump(data,fr)

    def join_data(self,i,device,bp,port):
        data = {
            "device_info_"+str(i):{
                "deviceName":device,
                "bp":bp,
                "port":port
            }
        }
        return data

    def clear_data(self):
        #清理yaml数据
        with open("../config/config.yaml","w") as fr:
            fr.truncate()
        fr.close()

    def get_file_lines(self):
        """获取yaml质点大小（行数）"""
        data = self.read_data()
        return len(data)



if __name__ == '__main__':
    write_file = WriteUserCommand()
    # print(write_file)
