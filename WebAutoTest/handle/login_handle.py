#coding=utf-8

from page.login_page import Login_Page
class LoginHandle():
    def __init__(self,driver):
        self.login_p = Login_Page(driver)

    #输入用户名
    def send_user_name(self,user_name):
        self.login_p.get_user_name().send_keys(user_name)

    #输入密码
    def send_user_password(self,password):
        self.login_p.get_user_password().send_keys(password)


    #点击dengl按钮
    def click_button(self):
        self.login_p.get_button().click()