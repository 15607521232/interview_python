#coding=utf-8

from selenium import webdriver

def run():
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")


if __name__ == '__main__':
    run()
