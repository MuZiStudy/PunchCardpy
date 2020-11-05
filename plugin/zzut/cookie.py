# -*- coding: UTF-8 -*-

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import json
import time


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
