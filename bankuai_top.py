# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 08:46:52 2023

@author: peipe
"""
# 导入tushare
import tushare as ts
# 初始化pro接口
pro = ts.pro_api('6981b94daa22fe173fabcf7c9963de3a47cf55132fb9e9b23f6091ab')

# 拉取数据
df = pro.ths_member(**{
    "ts_code": "885800.TI",
    "code": "",
    "limit": "",
    "offset": ""
}, fields=[
    "ts_code",
    "code",
    "name"
])
print(df)
