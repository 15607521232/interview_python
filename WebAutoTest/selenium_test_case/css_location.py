#coding=utf-8

from selenium import  webdriver
from time import sleep

def run():
    dri = webdriver.Chrome()
    dri.get("https://www.tmall.com/")
    css_el = dri.find_element_by_css_selector('#content > div.main-nav > div > div > div > a:nth-child(2) > img')
    css_el.click()

def run_58():
    dri = webdriver.Chrome()
    dri.get("https://xa.58.com/")
    el = dri.find_element_by_link_text('租房')
    print(el)
    print("浏览器句柄:", dri.window_handles)
    print("点击前:", dri.current_url)
    el.click()
    sleep(2)
    print("浏览器句柄:", dri.window_handles)
    print("点击后:", dri.current_url)
    print("当前标题",dri.title)

    #保存句柄
    handle_list = dri.window_handles
    dri.switch_to.window(handle_list[1])
    print("当前标题", dri.title)

def run_126_iframe():
    dri = webdriver.Chrome()
    dri.get("https://mail.163.com/")
    #定位到表单
    div_el = dri.find_element_by_xpath("//div[@id='loginDiv']/iframe")
    #切换到表单
    dri.switch_to.frame(div_el)
    #登陆
    dri.find_element_by_name('email').send_keys('15607521232')
    dri.find_element_by_name('password').send_keys('930819l@g')
    dri.find_element_by_id("dologin").click()
    sleep(8)
    dri.close()







if __name__ == '__main__':
    # run_58()
    run_126_iframe()