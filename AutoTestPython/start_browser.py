#coding=utf-8

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://account.cnblogs.com/signin?returnUrl=https%3A%2F%2Fwww.cnblogs.com%2F")
driver.find_element_by_id("LoginName").send_keys("aa")
driver.find_element_by_xpath()
driver.find_element_by_id("Password").send_keys("bb")
time.sleep(2)
driver.close()
