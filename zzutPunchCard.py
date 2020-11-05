# -*- coding: UTF-8 -*-
import json
from plugin.zzut.cookie import get_cookies
from plugin.zzut.add_record import add_record
import plugin.zzut.add_record
from fake_useragent import UserAgent
import urllib.request


# address当前位置名称
# class_and_grade 班级名称
# current_position_number 当前位置行政编码，不是邮编
# number 学号
# academy 学院
# animal_heat 体温元组
# 已有函数仅可以在 zzut_zdxy_w1使用，并且最好这个也别用，用add_zzut_zdxy_w1_full_values
# 因为不同的地方的东西，我不晓得里边的其他内容内容一致（数据条拼音简写，我猜不出来）
def add_zzut_zdxy_w1(address, class_and_grade, number, academy, current_position_number, name, animal_heat=['36.4', '36.8', '36.2']):
    # 目前已知的url提交链接
    url = 'http://sjgl.zzut.edu.cn/gx/gxxs/jkzk/saveOrEdit.json'

    # 目前已知的部分数据串，不同班级或许有不同，内部包含大量数据，自行填写,最好将实际数据直接替换
    values = {"xy": 0, "mqjcs": "", "dysj": "", "counts": "", "jzqksm": "", "yc": "", "zmd": 0, "ycztArray": [], "yhsf": "", "id": "", "sfkyfx": "", "dqwz": current_position_number, "yy": "", "bjh": "", "qt": "", "wtb": "", "sfyc": "1", "zc": "", "ssnj": "", "selectedArea": current_position_number, "zj": 0, "zk": 0, "yczzArray": [], "dwh": "", "xbmc": "", "zwtw": animal_heat[1], "drtw": animal_heat[2], "xgsj": "",
              "shgh": "", "bh": "", "dwmc": "", "ny": 0, "dqwzmc": address, "fbrq": "", "bz": "", "shsj": "", "gd": 0, "sq": 0, "sfycmc": "", "shjg": "", "kfrq": "", "tb": "", "bjmc": class_and_grade, "xh": number, "yczz": "", "szdwmc": academy, "tbsj": "", "xm": name, "yddh": "", "zxhj": 0, "hb": 0, "xwtw": animal_heat[0], "fdyxm": "", "yczt": "", "fyq": 0}

    # 页面cookie来源连接
    login_url = 'http://sjgl.zzut.edu.cn/vue/qyweixin/main?userAccount=' + \
        number+'&agentId=1000060'

    # 请求头原型,可根据自己实际自行添加键值对{'Cookie': '', 'Accept-Encoding': '', 'Content-Type': '','User-Agent': ua.random, 'Referer': ''}
    # User-Agent伪装浏览器类型，默认随机
    # Referer防盗链参数，用于声明是从哪个页面转到这里的
    headers = {'Cookie': get_cookies(login_url), 'Accept-Encoding': 'gzip', 'Content-Type': 'application/json;charset=UTF-8',
               'Referer': 'http://sjgl.zzut.edu.cn/vue/qyweixin/gx/gxxs/jkbg/jkbgMain/jkbgList'}
    return add_record(url=url, headers=headers, values=values)


# 已有函数仅可以在 zzut_zdxy_w1使用
def add_zzut_zdxy_w1_full_values(values):
    # 目前已知的url提交链接
    url = 'http://sjgl.zzut.edu.cn/gx/gxxs/jkzk/saveOrEdit.json'

    # 页面cookie来源连接
    login_url = 'http://sjgl.zzut.edu.cn/vue/qyweixin/main?userAccount=' + \
        values['xh']+'&agentId=1000060'

    # 请求头原型,可根据自己实际自行添加键值对{'Cookie': '', 'Accept-Encoding': '', 'Content-Type': '','User-Agent': ua.random, 'Referer': ''}
    # User-Agent伪装浏览器类型，默认随机
    # Referer防盗链参数，用于声明是从哪个页面转到这里的
    headers = {'Cookie': get_cookies(login_url), 'Accept-Encoding': 'gzip', 'Content-Type': 'application/json;charset=UTF-8',
               'Referer': 'http://sjgl.zzut.edu.cn/vue/qyweixin/gx/gxxs/jkbg/jkbgMain/jkbgList'}
    return add_record(url=url, headers=headers, values=values)


# 修改功能有，但绝壁不能乱给，改错了全完犊子
# value是完整的数据条，别想着乱搞，数据条有个id，那是指定哪一条数据的关键
def modify_zzut_zdxy_w1_full_values(cookie, **values):
    # 伪装成浏览器
    ua = UserAgent()
    url = 'http://sjgl.zzut.edu.cn/gx/gxxs/jkzk/saveOrEdit.json'

    # 设置请求头 告诉服务器请求携带的是json格式的数据
    # Referer防盗链参数，用于声明是从哪个页面转到这里的
    headers = {'Cookie': cookie, 'Accept-Encoding': 'gzip', 'Content-Type': 'application/json;charset=UTF-8', 'User-Agent': ua.random,
               'Referer': 'http://sjgl.zzut.edu.cn/vue/qyweixin/gx/gxxs/jkbg/jkbgFrom?id='}
    headers['Referer'] = headers['Referer']+values['id']

    request = urllib.request.Request(url=url, headers=headers, data=json.dumps(
        values).encode(encoding='UTF8'))  # 需要通过encode设置编码 要不会报错

    response = urllib.request.urlopen(request)  # 发送请求

    logInfo = response.read().decode()  # 读取对象 将返回的二进制数据转成string类型
    print(logInfo)


# address当前位置名称
# class_and_grade 班级名称
# current_position_number 当前位置行政编码，不是邮编
# number 学号
# academy 学院
# animal_heat 体温元组
# 极度推荐modify_zzut_zdxy_w1_full_values，因为不同的地方的东西，我不晓得里边的其他内容内容一致（数据条拼音简写，我猜不出来）
# 因为很多数据互相绑定的，因为单人环境，所以需要多组对比数据条并加以修改代码、测试后使用
# 已有函数仅可以在 zzut_zdxy_w1使用
# 主要功能已经实现，接下来的使用体验，范围，自行实现哦,哈哈
results = add_zzut_zdxy_w1(address='地址', class_and_grade='班级',
                           number='学号', academy='学院', current_position_number='所在地区行政编码', name='姓名')

# 还是对比数据条，使用add_zzut_zdxy_w1_full_values靠谱

if ~('code' in results):
    if results['code'] == "-1":
        if results['message'] == "此时间已经填报！":
            print("填报完成")
        else:
            print("填报失败")
    elif results['code'] == "1":
        print("填报完成")
    else:
        print("填报失败异常")
else:
    print("填报失败")
