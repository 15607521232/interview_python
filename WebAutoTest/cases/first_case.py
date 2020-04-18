#coding=utf-8
from bussiness.login_bussiness import LoginBussiness
from selenium import webdriver
import HTMLTestRunner
class First_Case():

    def __init__(self):
        driver = webdriver.Chrome()
        url = "https://account.cnblogs.com/signin?returnUrl=https%3A%2F%2Fwww.cnblogs.com%2F"
        driver.get(url)
        self.login = LoginBussiness(driver)


    def test_login_success(self):
        login_success = self.login.login_success("python_li","930819l@g")
        if login_success == True:
            print("登录成功")




def main():
    first_case = First_Case()
    first_case.test_login_success()

if __name__ == '__main__':
    main()