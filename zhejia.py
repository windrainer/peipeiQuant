# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 导入tushare
import tushare as ts
import pandas as pd
# 初始化pro接口
pro = ts.pro_api('6981b94daa22fe173fabcf7c9963de3a47cf55132fb9e9b23f6091ab')

# 拉取数据
def down_data(date,d2):
    df = pro.limit_list_d(**{
        "trade_date": date,
        "ts_code": "",
        "limit_type": "D",
        "exchange": "",
        "start_date": "",
        "end_date": "",
        "limit": "",
        "offset": ""
    }, fields=[
        "trade_date",
        "ts_code",
        "name",
        "close",
        "pct_chg",
        "amount",
        "last_time",
        "limit_times"
    ])
    
    df['amount']=round(df['amount']/100000000,2)    
        
    df5=[]
    for i in range(len(df)):
        target = df.iloc[i]['ts_code']
        print(target)
        
        df1 = pro.daily(**{
        "ts_code": target,
        "trade_date": d2,
        "start_date": "",
        "end_date": "",
        "offset": "",
        "limit": ""
    }, fields=[
        "ts_code",
        "trade_date",
        "open",
        "close",
        "pct_chg",
        "amount",
        "pre_close"
    ])
        list1=[]
        list1=[df1]
        df5.extend(list1)
    df5=pd.concat(df5)
    
    df5['n_premium']=round((df5['open']-df5['pre_close'])/df5['pre_close']*100,2) 
    
    df5["pct_chg"]=round(df5["pct_chg"],2)

    df3=df5[["ts_code","n_premium","pct_chg"]]

    df3=df3.rename(columns={"pct_chg":"n_pct_chg"})    

    df2=pd.merge(df,df3,on=["ts_code"] )   
    df2.to_csv('D:/1stock/zhejia'+str(date)+'.csv',encoding='utf_8_sig')
    return df2

date=20230206
d2=20230207
df5=down_data(date,d2)
print("length")
print(len(df5))
print('next_premium')
print(round(df5['n_premium'].mean(),2))
print('next_pct_chg')
print(round(df5['n_pct_chg'].mean(),2))




