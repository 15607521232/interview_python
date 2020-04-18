#coding=utf-8


from behave import *
import time
use_step_matcher('re')

@when('open the login website "([^"]*)"')
def step_login(context,url):
    context.driver.get(url)


@then('I expect that the title is "([^"]*)"')
def step_login1(context,title_name):
    title = context.driver.title
    assert title_name in title


@when('I set with username "([^"]*)"')
def step_login2(context,username):
    context.driver.find_element_by_id("LoginName").send_keys(username)


@when('I set password "([^"]*)"')
def step_login3(context,password):
    context.driver.find_element_by_id("Password").send_keys(password)

@when('I click with loginbutton')
def step_login4(context):
    context.driver.find_element_by_id("submitBtn").click()

@then('I expect that text "用户名或密码错误"')
def step_login5(context,code_text):
    text = context.driver.find_element_by_xpath('//*[@id="loginForm"]/div[4]/div/div').text
    time.sleep(10)
    assert code_text in text

