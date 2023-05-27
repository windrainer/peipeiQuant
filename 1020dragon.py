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
    
    df5=df5.sort_values(by='Change_10').dropna()

    #df5.to_csv('D:/1stock/1020zhongjun_'+str(date)+'.csv',encoding='utf_8_sig')
    
    neg_10=df5.head(10)
    
    posi_10=df5.tail(10)
    
    df6=df5.sort_values(by='Change_20').dropna()
    
    posi_20=df6.tail(5)
    
    return neg_10, posi_10, posi_20

def iter_ch(df,d2):
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
    
    return df2

if __name__ == '__main__':
    date=20230505
    #d2=20220804
    neg_10, posi_10,posi_20=daprocess(date)
    
    #neg_10=iter_ch(neg_10,d2)
    #neg_10.to_csv('D:/1stock/zj_neg10_'+str(date)+'.csv',encoding='utf_8_sig')
    
    #posi_10=iter_ch(posi_10,d2)
    #print(posi)
    posi_10.to_csv('D:/1stock/zj_posi10_'+str(date)+'.csv',encoding='utf_8_sig')
    
    #posi_20=iter_ch(posi_20,d2)
    #print(posi)
    posi_20.to_csv('D:/1stock/zj_posi20_'+str(date)+'.csv',encoding='utf_8_sig')
    
    

        
        
        
        
        
