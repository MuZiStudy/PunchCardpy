# -*- coding: UTF-8 -*-

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import json
import time


def get_login_cookie(login_url_number):
    # 页面cookie来源连接
    login_url_head = 'http://sjgl.zzut.edu.cn/vue/qyweixin/main?userAccount='
    login_url_tail = '&agentId=1000060'
    return get_cookies(login_url_head+login_url_number+login_url_tail)


def get_cookies(url):
    firefox_options = Options()
    # 不启动界面显示- linux下命令行模式必须启用
    firefox_options.add_argument('-headless')
    driver = Firefox(firefox_options=firefox_options)
    driver.get(url)
    time.sleep(2)
    driver.refresh()
    time.sleep(2)
    cookies = driver.get_cookies()
    driver.close()

    cookies_str = cookies[0]['name'] + \
        "=" + cookies[0]['value']
    return cookies_str
