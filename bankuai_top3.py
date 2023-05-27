# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 08:46:52 2023

@author: peipe
"""
# 导入tushare
import tushare as ts
import pandas as pd
import os
# 初始化pro接口
pro = ts.pro_api('6981b94daa22fe173fabcf7c9963de3a47cf55132fb9e9b23f6091ab')

# 拉取数据
def downloadbankuai(code):
    #code="885556.TI"
    df1 = pro.ths_member(**{
        "ts_code": code,
        "code": "",
        "limit": "",
        "offset": ""
    }, fields=[
        "ts_code",
        "code",
        "name"
    ])
    
    df1=df1.rename(columns={"ts_code":"bankuai"})
    df1=df1.rename(columns={"code":"ts_code"})    
    return df1

def get_file(path):                   
    # read the file in local pc
    files =os.listdir(path)
    files.sort() 
    
    #create an empty list
    list1= []
    for file in files:
        if not  os.path.isdir(path +file):  #判断该文件是否是一个文件夹       
            f_name = str(file)        
            #print(f_name)
            tr = '\\'   #多增加一个斜杠
            filename = path + tr + f_name        
            list1.append(filename)  
    return list1

def daprocess(date):
    path ='D:/China Stock Market Data orignal'
    list1=get_file(path)

    df5=[]
    for i in range(len(list1)):
        list2=[]
        df1=pd.read_csv(list1[i])
        df1=df1[df1['trade_date']==date]
        list2=[df1]
        df5.extend(list2)
    
    df5=pd.concat(df5)
    print('hangshu')
    print(len(df5))
         
    return df5

def congzu(date,code):
    df1=downloadbankuai(code)
    df2=daprocess(date)
    df3=pd.merge(df1, df2, on='ts_code')
    
    df3=df3[["trade_date","bankuai","ts_code","name_x","Change_10","pct_change",
             "close","amount","industry","float_mv","Change_20"]]
    
    #df3["Change_10"]=round(df3["Change_10"],2)
    
    df3=df3.sort_values(by='Change_10', ascending=False)

    df3.to_csv('D:/1stock/'+str(code)+'_'+str(date)+'.csv',encoding='utf_8_sig')
    return df3

date=20230504
code="881175.TI"
congzu(date,code)
