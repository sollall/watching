import serial
import time
import datetime

def test_time():
    temp=time.time()
    return temp


def get_ser(num):
    sers=[]
    for i in range(num):
        try:
            temp=serial.Serial("/dev/ttyUSB"+str(num), 2400)
            sers.append(temp)
        except:
            sers.append(False)
    
    return sers

def get_gram(ser):
    temp=list(ser.readline())
    temp=list(map(int,temp))
    
    ans=temp[4:12]
    
    for i in range(len(ans)):
        if ans[i]>=176:
            ans[i]-=176
        elif ans[i]>=48:
            ans[i]-=48
        else:
            ans[i]="."
        ans[i]=str(ans[i])
    
    if ans:
        return float("".join(ans))
    else:
        return float("")
    
    
    