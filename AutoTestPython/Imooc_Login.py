#coding=utf-8
from selenium import webdriver
import time
import unittest

class IMooc_Login(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.imooc.com/")

    def tearDown(self) -> None:
        self.driver.close()


    def test_login_handle(self):
        self.driver.find_element_by_id("js-signin-btn").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="signup-form"]/div[1]/input').send_keys("15607521232@163.com")
        self.driver.find_element_by_xpath('//*[@id="signup-form"]/div[2]/input').send_keys("930819@lg")
        self.driver.find_element_by_xpath('//*[@id="signup-form"]/div[5]/input').click()


    def test_login(self):
        # self.test_login_handle()
        # login_fail = self.driver.find_element_by_id("signin-globle-error").text
        # self.assertIs("登录成功",login_fail,"登录失败")
        self.assertIsNone(self.test_login_handle())


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(IMooc_Login('test_login'))
    unittest.TextTestRunner().run(suite)



