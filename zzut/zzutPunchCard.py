# -*- coding: UTF-8 -*-
import json
from fake_useragent import UserAgent
import urllib.request
from datetime import datetime
import os
import sys
from apscheduler.schedulers.blocking import BlockingScheduler
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# __file__获取执行文件相对路径，整行为取上一级的上一级目录
sys.path.append(BASE_DIR)

from plugin.zzut.cookie import get_cookies
from plugin.zzut.add_record import add_record
from plugin.universal.send_mail import send_mail
from plugin.universal.read_json_file import read_json_file
# address当前位置名称
# class_and_grade 班级名称
# current_position_number 当前位置行政编码，不是邮编
# number 学号
# academy 学院
# animal_heat 体温元组
# 测试版


def add_zzut_values(address, class_and_grade, number, academy, current_position_number, name, animal_heat=['36.4', '36.8', '36.2']):
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
    return add_record(url=url, headers=headers, data=values)


# 已有函数仅可以在 zzut_zdxy_w1使用
def add_zzut_full_values(values):
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
    return add_record(url=url, headers=headers, data=values)


# 修改功能有，但绝壁不能乱给，改错了全完犊子
# value是完整的数据条，别想着乱搞，数据条有个id，那是指定哪一条数据的关键
def modify_zzut_full_values(cookie, **data):
    # 伪装成浏览器
    ua = UserAgent()
    url = 'http://sjgl.zzut.edu.cn/gx/gxxs/jkzk/saveOrEdit.json'

    # 设置请求头 告诉服务器请求携带的是json格式的数据
    # Referer防盗链参数，用于声明是从哪个页面转到这里的
    headers = {'Cookie': cookie, 'Accept-Encoding': 'gzip', 'Content-Type': 'application/json;charset=UTF-8', 'User-Agent': ua.random,
               'Referer': 'http://sjgl.zzut.edu.cn/vue/qyweixin/gx/gxxs/jkbg/jkbgFrom?id='}

    values = data['data']

    headers['Referer'] = headers['Referer'] + values['id']

    request = urllib.request.Request(url=url, headers=headers, data=json.dumps(
        values).encode(encoding='UTF8'))  # 需要通过encode设置编码 要不会报错

    response = urllib.request.urlopen(request)  # 发送请求

    logInfo = response.read().decode()  # 读取对象 将返回的二进制数据转成string类型
    return_code = json.loads(logInfo)
    return return_code


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
# results = add_zzut_values(address='地址', class_and_grade='班级',
#                            number='学号', academy='学院', current_position_number='所在地区行政编码', name='姓名')


# 打印日志
def write_log_file(number, results):
    if not os.path.exists(BASE_DIR+'\\zzut\\log'):
        os.makedirs(BASE_DIR+'\\zzut\\log')
    elif not os.path.isdir(BASE_DIR+'\\zzut\\log'):
        os.remove(BASE_DIR+'\\zzut\\log')
        os.makedirs(BASE_DIR+'\\zzut\\log')

    # 以追加形式打开日志文件
    log_file = open(BASE_DIR+'\\zzut\\log\\punchcard.log',
                    'a', encoding='UTF-8')
    log_file.write(number+'\t')
    log_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\t')
    log_file.write(analyse_status(results=results))
    log_file.write('\n')
    log_file.close()


def analyse_status(results):
    if 'code' in results:
        if results['code'] == "-1":
            if results['message'] == "此时间已经填报！":
                return "填报完成"
            else:
                return "填报失败"
        elif results['code'] == "1":
            return "填报完成"
        else:
            return"填报失败异常"
    else:
        return "填报失败"


def auto_add_zzut_full_values(file_path):

    name_table_full_values_json = read_json_file(file_path)

    inform_account_json_file = read_json_file(
        BASE_DIR+"\\zzut\\data\\mail_user.json")

    inform_content_head = "<table id=\"customers\"><tr><th>打卡学号</th><th>打卡时间</th><th>打卡状态</th></tr>"
    inform_content_tail = "</table>"
    # 循环执行打卡
    for values in name_table_full_values_json['names']:
        results = add_zzut_full_values(values)
        inform_content_head += "<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (
            values["xh"], datetime.now().strftime("%Y-%m-%d %H:%M:%S"), analyse_status(results=results))
        write_log_file(number=values["xh"], results=results)
    write_temp_report_file(content=inform_content_head+inform_content_tail)


def auto_add_zzut_values(file_path):

    name_table_value_json = read_json_file(file_path)

    inform_content_head = "<table id=\"customers\"><tr><th>打卡学号</th><th>打卡时间</th><th>打卡状态</th></tr>"
    inform_content_tail = "</table>"
    # 循环执行打卡
    for values in name_table_value_json['names']:
        results = add_zzut_values(address=values["dqwzmc"], class_and_grade=values["bjmc"], number=values["xh"],
                                  academy=values["szdwmc"], current_position_number=values["dqwz"], name=values["xm"])
        inform_content_head += "<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (
            values["xh"], datetime.now().strftime("%Y-%m-%d %H:%M:%S"), analyse_status(results=results))
        write_log_file(number=values["xh"], results=results)
    write_temp_report_file(content=inform_content_head+inform_content_tail)


def write_temp_report_file(content):

    file_name = datetime.now().strftime("%Y-%m-%d")
    file_name += "_report_file.txt"
    file_status = 0
    if not os.path.isfile(BASE_DIR+'\\zzut\\log\\'+file_name):
        file_status = 1

    # 以追加形式打开日志文件
    report_file = open(BASE_DIR+'\\zzut\\log\\'+file_name,
                       'a', encoding='UTF-8')
    if file_status == 1:
        inform_account_json_file = read_json_file(
            BASE_DIR+"\\zzut\\data\\mail_user.json")
        inform_content = inform_account_json_file["content_css"]
        report_file.write(inform_content)
    report_file.write(content)
    report_file.close()


# 发送报告邮件
def report_mail():
    file_name = datetime.now().strftime("%Y-%m-%d")
    file_name += "_report_file.txt"
    # 读取报告文件
    report_file = open(BASE_DIR+'\\zzut\\log\\' +
                       file_name, "r", encoding='UTF-8')
    report_file_str = ""
    for line in report_file:
        report_file_str = report_file_str+line
    report_file.close()

    inform_account_json_file = read_json_file(
        BASE_DIR+"\\zzut\\data\\mail_user.json")
    send_mail(server=inform_account_json_file["server"], user=inform_account_json_file["user"], passwd=inform_account_json_file["passwd"],
              subject=inform_account_json_file["subject"], to_user=inform_account_json_file["to_user"], content=report_file_str)


# 定时任务
# 程序起点
sched = BlockingScheduler()
sched.add_job(auto_add_zzut_values, 'cron',
              day_of_week='0-6', hour=6, minute=30, args=[BASE_DIR+"\\zzut\\data\\name_table_values.json"])
sched.add_job(report_mail, 'cron', day_of_week='0-6', hour=9, minute=0)
sched.start()
