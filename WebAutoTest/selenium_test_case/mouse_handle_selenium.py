#coding=utf-8

from selenium.webdriver import ActionChains
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

def mouse_handle():
    dri = webdriver.Chrome()
    dri.get("http://www.baidu.com")
    el_log = dri.find_element_by_xpath('//*[@id="s_lg_img_new"]')

    #鼠标右击
    ActionChains(dri).context_click(el_log).perform()
    time.sleep(3)

def double_click():
    '''鼠标双击'''
    dri = webdriver.Chrome()
    dri.get("https://3w.huanqiu.com/a/170373/3yGx4MlBkYK?agt=20&tt_group_id=6827674596141957640")
    el_con = dri.find_element_by_xpath('//*[@id="article"]/h1/strong')

    #鼠标双击
    ActionChains(dri).double_click(el_con).perform()
    time.sleep(3)

def mouse_stop():
    """鼠标悬停"""
    dri = webdriver.Chrome()
    dri.get("https://www.jd.com/")
    el_jd = dri.find_elements_by_class_name('cate_menu_item')

    #鼠标悬停操作
    for el in el_jd:
        ActionChains(dri).move_to_element(el).perform()
        time.sleep(1)

def jianpan_case():
    """键盘操作"""
    dri = webdriver.Chrome()
    dri.get("https://cn.bing.com/")
    input_el = dri.find_element_by_id("sb_form_q")
    input_el.send_keys("python")
    time.sleep(3)

    #键盘操作
    input_el.send_keys(Keys.BACK_SPACE)
    time.sleep(3)

def tanchu_case():
    '''弹出框设置'''
    dri = webdriver.Chrome()
    dri.get("http://www.baidu.com")
    dri.find_element_by_id("s-usersetting-top").click()
    time.sleep(1)
    dri.find_element_by_xpath('//*[@id="s-user-setting-menu"]/div/a[1]').click()
    time.sleep(1)
    dri.find_element_by_xpath('//*[@id="se-setting-5"]/span[2]/label').click()
    time.sleep(1)
    dri.find_element_by_xpath('//*[@id="se-setting-7"]/a[2]').click()
    time.sleep(1)
    dri.switch_to.alert.accept()

def xiala_case():
    """下拉框"""
    dri = webdriver.Chrome()
    dri.get("http://www.baidu.com")

if __name__ == '__main__':
    # mouse_handle()
    # double_click()
    # mouse_stop()
    # jianpan_case()
    tanchu_case()