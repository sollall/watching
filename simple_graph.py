import matplotlib
matplotlib.use("GTK3Agg")

import matplotlib.pyplot as plt
from pydub import AudioSegment
from pydub.playback import play
import datetime as dt

def display(x,y,alarm_value,audio_data=False):
    N=len(y)
    flag_alarm=False
    
    for i in range(N):
        #linesが使い回し変数なってるけどいいんか???
        
        big_lines[i].set_data(x,y[i])
        #ここらへんのせいで遅い？
        axes[i].set_xlim(x[0],x[-1])
        axes[i].set_ylim(min(y[i])*0.9,max(y[i])*1.1)        
        
        if abs(y[i][0]-y[i][-1])<alarm_value[i]:
            axes[i].set_facecolor("red")
            flag_alarm=True
        else:
            axes[i].set_facecolor("white")
        
    if False:
        play(audio_data)
    #ここ小さいほうが応答しやすい???
    plt.pause(0.0001)
    plt.cla()
    
    return 
    
fig,axes=plt.subplots(2)
big_lines=[]
for i in range(2):
    lines, =axes[i].plot([],[])
    big_lines.append(lines)

x=[0]
y=[[0],[0]]

if __name__=="__main__":
    while True:

        x.append(x[-1]+1)
        y[0].append(y[0][-1]+0.1)
        y[1].append(y[1][-1]+1)
        if len(x)>30:
            x.pop(0)
            y[0].pop(0)
            y[1].pop(0)

        display(x,y,[3,3],AudioSegment.from_mp3('/home/pi/Desktop/sample.mp3'))
        
        print(dt.datetime.now())
    
        
    
    