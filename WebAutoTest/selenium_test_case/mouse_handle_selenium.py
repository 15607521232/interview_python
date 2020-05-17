#coding=utf-8

from selenium.webdriver import ActionChains
from selenium import webdriver
import time

def mouse_handle():
    dri = webdriver.Chrome()
    dri.get("http://www.baidu.com")
    el_log = dri.find_element_by_xpath('//*[@id="s_lg_img_new"]')

    #鼠标右击
    ActionChains(dri).context_click(el_log).perform()
    time.sleep(3)

if __name__ == '__main__':
    mouse_handle()