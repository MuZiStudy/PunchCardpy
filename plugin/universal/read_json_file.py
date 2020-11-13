# -*- coding: UTF-8 -*- 
import json

# 读取json文件
def read_json_file(file_path):
    # 读取json文件
    json_file = open(file_path, "r", encoding='UTF-8')
    json_file_str = ""
    for line in json_file:
        json_file_str = json_file_str+line
    json_file.close()

    # 转化为json对象
    file_tostr_json = json.loads(json_file_str)
    return file_tostr_json