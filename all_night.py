#pandas実装どうしよう
import serial
import time
import datetime as dt

import matplotlib
matplotlib.use("Qt5Agg")

import matplotlib.pyplot as plt
import pandas as pd

import functions
import simple_graph        

"""__init__"""
"""シリアル通信の入り口は4つにしておくか　USBポートは4つまでなので"""
N=4
sers=functions.get_ser(N)

alarm=[0.1]*N

#dataframe周り
columns_name=["Time"]+[str(i) for i in range(N)]
print(columns_name)

past=dt.datetime.now()
while True:
    now=dt.datetime.now()
    sers=functions.get_ser(N)
    bench=time.time()
    #値を取得 途中で通信が断絶しても動くようにしたい
    grams=[str(now)]
    for i in range(N):
        try:
            grams.append(functions.get_gram(sers[i]))
        except:
            grams.append(False)
    
    if now.second!=past.second:
        print(sers)
        print(grams)
        
        csv_name=now.strftime("%Y-%m-%d")+".csv"
        try:
            df=pd.read_csv(csv_name, index_col=0)
            temp_df=pd.Series(grams, index = df.columns)
            df=df.append(temp_df,ignore_index=True)
        except FileNotFoundError:
            #起動時とか日をまたいだときとかにつくる
            df = pd.DataFrame( [grams], columns=columns_name)
        
        df.to_csv(csv_name)
        print(time.time()-bench)
    
    #dataframe開いてメモ　なければ作る
    past=now
        

    


