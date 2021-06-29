#coding=utf-8
from util.read_init import ReadIni
class GetByLocal:
    def __init__(self,driver):
        self.driver = driver

    def get_element(self,key):
        read_ini = ReadIni()
        local = read_ini.get_value(key)
        try:
            if local!=None:
                by = local.split('>')[0]
                local_by = local.split('>')[1]
                if by == 'id':
                    return self.driver.find_element_by_id(local_by)
                elif by == 'class':
                    return self.driver.find_element_by_class_name(local_by)
                else:
                    return self.driver.find_element_by_xpath(local_by)
        except:
            self.driver.save_screenshot("../jpg/HiRay01.png")  # 找不到元素
            return None

        else:
            return None
if __name__ == '__main__':
    get_text=GetByLocal()
    get_text.get_element("title_guild")
