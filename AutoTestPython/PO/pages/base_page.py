#coding=utf-8

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from AutoTestPython.PO import settings
from PO import settings


class BasePage():
    def __init__(self,driver,url):
        self._driver = driver
        self._url = url

    def open(self):

        self._driver.get(url=self._url)

    def find_element(self,*locator,timeout=None):
        try:
            self._init_wait(timeout).until(EC.visibility_of_element_located(locator=locator))
        except(NoSuchElementException,TimeoutException):
            self._driver.quit()
            raise TimeoutException(msg="定位远胜于失败，方式为{}".format(locator))
    def send_keys(self,webElement,keys):
        webElement.clear()
        webElement.send_keys(keys)


    def _init_wait(self,timeout):
        if timeout is None:
            return WebDriverWait(driver=self._driver,timeout=settings.UI_WAIT_TIME)
        else:
            return WebDriverWait(driver=self._driver,timeout=settings.UI_WAIT_TIME)