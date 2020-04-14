#coding=utf-8

from selenium import webdriver

class BrowserEngine():

    def init_driver(self):
        driver = webdriver.Chrome()
        return driver

