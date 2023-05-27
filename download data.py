# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 21:52:05 2022

@author: peipe
"""

#coding=utf-8 
import tushare as ts
import datetime

def today():
    today=datetime.date.today()
    return today
    
#读取对应数据，重新组合
def his_data(code,start,end):
    pro = ts.pro_api('6981b94daa22fe173fabcf7c9963de3a47cf55132fb9e9b23f6091ab')
    #下载基本数据
    #df= pro.daily(ts_code=code, start_date=start, end_date=end)
    #下载close价格带换手率和成交量的指标
    #df = pro.daily_basic(ts_code=code, start_date=start, end_date=end)
    df=pro.bak_daily(ts_code=code, start_date=start, end_date=end,
                     fields='''ts_code,trade_date,name,
                             close,pct_change,amount,industry,float_mv''')
    
    df=df.drop( index = df.amount[df.amount == 0].index )
    
    df=df.sort_index(ascending=False).reset_index(drop=True)
    
    df['Change_10'] = df['close'].pct_change(periods=10)*100
    df['Change_20'] = df['close'].pct_change(periods=20)*100
    
    return df

def main(code):
    df=his_data(code,start='20210101',end='today()')
    m='D:\\China Stock Market Data orignal\\'
    n=code
    
    df.to_csv(m+'\\'+n+'.csv',encoding='utf_8_sig')
    return df

if __name__ == '__main__':
    pro = ts.pro_api()
    data_list = pro.stock_basic(exchange='', list_status='L',
                           fields='ts_code,symbol,name,area,industry,list_date')
        

    for i in range(len(data_list)):
        try:
            target = data_list.iloc[i]['ts_code']
            main(target)
            
        except:
            IndexError
        




