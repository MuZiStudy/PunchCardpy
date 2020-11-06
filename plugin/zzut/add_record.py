# -*- coding: UTF-8 -*-

import urllib.request
import json
from fake_useragent import UserAgent
from plugin.zzut.cookie import get_cookies

# 用于添加当前时间点的打卡记录的


def add_record(url, headers, **data):
    # 伪装成浏览器
    ua = UserAgent()
    values = data['data']
    if ~('User-Agent' in headers):
        headers['User-Agent'] = ua.random

    request = urllib.request.Request(url=url, headers=headers, data=json.dumps(
        values).encode(encoding='UTF8'))  # 需要通过encode设置编码 要不会报错

    response = urllib.request.urlopen(request)  # 发送请求

    logInfo = response.read().decode()  # 读取对象 将返回的二进制数据转成string类型

    return_code = json.loads(logInfo)
    return return_code
