#coding=utf-8


from selenium.webdriver.common.by import By

from PO.pages.base_page import BasePage


class LoginPage(BasePage):
    Url = "https://account.cnblogs.com/signin?returnUrl=https%3A%2F%2Fwww.cnblogs.com%2F"
    UserName = (By.ID,"LoginName")
    PassWord = (By.ID,"Password")

    def __init__(self,driver):
        super().__init__(driver=driver,url=self.Url)

    def login(self):
        self.open()
        #*代表是一个元组的list
        self.send_keys(webElement=self.find_element(*self.UserName),keys="aa")
        self.send_keys(webElement=self.find_element(*self.PassWord),keys="bb")

