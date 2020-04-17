#coding=utf-8

from base.find_element import FindElement
from selenium import webdriver

class Login_Page():
    def __init__(self,driver):
        self.fe = FindElement(driver)

    #获取用户名
    def get_user_name(self):
        return self.fe.get_element("LoginName")


    #获取密码
    def get_user_password(self):
        return self.fe.get_element("Password")


    #获取button
    def get_button(self):
        return self.fe.get_element("submitBtn")


    #获取失败提示
    def get_username_password_error(self):
        return self.get_username_password_error('//*[@id="loginForm"]/div[4]/div/div')


if __name__ == '__main__':
    driver = webdriver.Chrome()
    lp = Login_Page(driver=driver)
    print(lp.get_user_name())


