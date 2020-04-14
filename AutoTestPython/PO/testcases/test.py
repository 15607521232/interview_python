#coding=utf-8
from PO.pages.browser_engine import BrowserEngine
from PO.pages.login_page import LoginPage


class Test():
    driver = BrowserEngine().init_driver()


    def test_login(self):
        LoginPage(driver=self.driver).login()


t = Test()
t.test_login()