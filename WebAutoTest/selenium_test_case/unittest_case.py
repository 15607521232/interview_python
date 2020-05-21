#coding=utf-8

import unittest
from selenium import webdriver
import time

class Unittest_case(unittest.TestCase):

    # def __init__(self):
    #     self.dri = webdriver.Chrome()

    #espace

    def setUp(self) -> None:
        self.dri = webdriver.Chrome()

    def test_run_01(self):
        self.dri.get("http://www.baidu.com")
        title = self.dri.title
        print(title)
        # self.assertEqual("百度一下，你就知道","百度一下，你就知道","success")
        self.assertIn("百度一下","百度一下，你就知道","success")

    def tearDown(self) -> None:
        self.dri.close()



if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Unittest_case('test_run_01'))
    unittest.TextTestRunner().run(suite)

    # uc = Unittest_case()
    # uc.test_run_01()