# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 22:23:42 2023

@author: peipe
"""

# talib的指标库是自行安装的，提供一系列的技术指标
import os
import pandas as pd
import tushare as ts
# 初始化pro接口
pro = ts.pro_api('6981b94daa22fe173fabcf7c9963de3a47cf55132fb9e9b23f6091ab')

#读取所有文件
# path ='D:/China Stock Market Data orignal'
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
    
    df5=df5[df5['pct_change']>19]
     
    return df5

if __name__ == '__main__':
    date=20221013
    #d2=20220804
    posi_10=daprocess(date)
    
    posi_10.to_csv('D:/1stock/xingu_'+str(date)+'.csv',encoding='utf_8_sig')
    
    
    

        
        
        
        
        
