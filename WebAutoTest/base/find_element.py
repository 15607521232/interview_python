#coding=utf-8

from util.read_ini import ReadIni
from selenium import webdriver
class FindElement():
    def __init__(self,driver):
        self.driver = driver

    def get_element(self,key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split(">")[0]
        value = data.split(">")[1]
        try:
            if by == "id":
                return self.driver.find_element_by_id(value)
            if by == "xpath":
                return self.driver.find_element_by_xpath(value)
        except:
            return None


if __name__ == '__main__':
    driver = webdriver.Chrome()
    fe = FindElement(driver)
    print(fe.get_element("LoginName"))


