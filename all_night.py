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
"""
dataframeのcolumn数は4に固定
USBを抜いてからまた指すとカラムが入れ替わったりする　しゃあなくない？
ほかにつけたい機能は
・dataframeが空なら削除

mergeしたい機能は
・OCRで測定値読み取り
・振動で機械が動いてるか確認
・センサとGPIOを直接つないで測定(最終手段)
"""


N=4
sers=functions.get_ser()

alarm=[0.1]*N

#dataframe周り
columns_name=["Time"]+[str(i) for i in range(N)]


past=dt.datetime.now()
while True:
    now=dt.datetime.now()
    sers=functions.get_ser()
    bench=time.time()
    #値を取得 途中で通信が断絶しても動くようにしたい
    grams=[str(now)]
    for i in range(N):
        try:
            grams.append(functions.get_gram(sers[i]))
        except FileNotFoundError:
            grams.append(False)
        except IndexError:
            grams.append(False)
    
    if now.second!=past.second:
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
        
    
    #dataframe開いてメモ　なければ作る
    past=now
        
"""
USBを抜くとこのエラーが出る　serial.serialutil.SerialException
電源を消すと待機状態になる　これを検出するのが厄介そう
"""
