#coding=utf-8


Feature: Login User
  As a developer
  This is my first bdd project
  Scenario: open login website
    When open the login website "https://account.cnblogs.com/signin?returnUrl=https%3A%2F%2Fwww.cnblogs.com%2F"
    Then I expect that the title is "用户登录 - 博客园"


  Scenario: input username
    When I set with username "python_li"
    And  I set password "930819@g"
    And I click with loginbutton
    Then I expect that text "用户名或密码错误"







