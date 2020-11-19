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
def refresh_cookie(login_url_number, cookie):
    # 伪装成浏览器
    ua = UserAgent()
    login_url = 'http://sjgl.zzut.edu.cn/vue/qyweixin/main?userAccount' + \
        login_url_number + '&agentId=1000060'
    headers = {'Cookie': cookie, 'Accept-Encoding': 'gzip',
               'Content-Type': 'application/json;charset=UTF-8', 'User-Agent': ua.random}

    login_request = urllib.request.Request(
        url=login_url, headers=headers)
    urllib.request.urlopen(login_request)  # 发送请求

    headers['Referer'] = login_url
    weiXinJsSdkApiAuthorize_json = {
        "url": login_url}
    weiXinJsSdkApiAuthorize_request = urllib.request.Request(
        url='http://sjgl.zzut.edu.cn/mobile/weiXinJsSdkApiAuthorize.json', headers=headers, data=json.dumps(weiXinJsSdkApiAuthorize_json).encode(encoding='UTF8'))
    urllib.request.urlopen(weiXinJsSdkApiAuthorize_request)  # 发送请求

    setUserInfo_json = {"userAccount": login_url_number}
    setUserInfo_request = urllib.request.Request(
        url='http://sjgl.zzut.edu.cn/mobile/setUserInfo.json', headers=headers, data=json.dumps(setUserInfo_json).encode(encoding='UTF8'))
    urllib.request.urlopen(setUserInfo_request)  # 发送请求

    findListByAgentIdCache_json = {"agentId": "1000060"}
    findListByAgentIdCache_request = urllib.request.Request(
        url='http://sjgl.zzut.edu.cn/mobile/sysMobileBusiness/findListByAgentIdCache.json', headers=headers, data=json.dumps(findListByAgentIdCache_json).encode(encoding='UTF8'))
    urllib.request.urlopen(findListByAgentIdCache_request)  # 发送请求
