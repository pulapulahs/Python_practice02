# coding=utf-8
# 引入 webdriver 模块
from selenium import webdriver

# 打开浏览器
dr = webdriver.Chrome()
# 访问百度首页
dr.get("http://www.baidu.com")
# 输入框输入selenium
dr.find_element_by_id('kw').send_keys("婧")
# 点击搜索按钮
dr.find_element_by_id('su').click()
