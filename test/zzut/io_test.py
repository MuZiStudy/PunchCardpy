# -*- coding: UTF-8 -*-

import json

name_file = open("./name_table.json", "r",encoding='UTF-8')
name_table_str=""
for line in name_file:
    name_table_str=name_table_str+line
name_table_json=json.loads(name_table_str)
for name in name_table_json['w1_names']:
    print(name['xm'])

