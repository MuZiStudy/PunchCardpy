# -*- coding: UTF-8 -*-

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import json
import time
import urllib.request
import json
from fake_useragent import UserAgent

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


# 刷新cookie所属权
def refresh_cookie(login_url_number,cookie):
    # 伪装成浏览器
    ua = UserAgent()
    login_url_head = 'http://sjgl.zzut.edu.cn/vue/qyweixin/main?userAccount='
    login_url_tail = '&agentId=1000060'
    headers = {'Cookie': cookie, 'Accept-Encoding': 'gzip', 'Content-Type': 'application/json;charset=UTF-8', 'User-Agent': ua.random}
    request = urllib.request.Request(url=login_url_head+login_url_number+login_url_tail, headers=headers)  # 需要通过encode设置编码 要不会报错
    response = urllib.request.urlopen(request)  # 发送请求
    logInfo = response.read().decode()  # 读取对象 将返回的二进制数据转成string类型
    return logInfo

