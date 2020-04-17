#coding=utf-8

from handle.login_handle import LoginHandle
from page.login_page import Login_Page

class LoginBussiness():
    def __init__(self,driver):
        self.login_h = LoginHandle(driver)

    def user_base(self,user_name,password):
        self.login_h.send_user_name(user_name)
        self.login_h.send_user_password(password)
        self.login_h.click_button()


    #执行操作
    def login_success(self,user_name,password):
        self.user_base(user_name,password)

        if Login_Page.get_username_password_error() == None:
            return True
        else:
            return False

