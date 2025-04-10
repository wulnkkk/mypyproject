###自制艾宾浩斯记忆表格
'''
20分钟后再重复一遍，1小时后，9小时后，1天后，2天后，5天后，8天后，14天后就会记得很牢
'''
import pandas as pd
import numpy as np
import re
import time
##常数
all_month=[1,3,5,7,8,10,12] ##31天的月份
day_list=[0,1,3,7,13]  ##记忆周期
##输入参数
unit_number=  50    ##需记忆的单元数（个）  
evynum= 1   ##      每天新记忆个数
number_period= unit_number/evynum+13 if unit_number%evynum==0 else unit_number//evynum+14    ##记忆一轮的周期（天）加上14天复习期间
##获取当前时间 格式为 03 28  2023
today=time.strftime("%m %d %Y",time.localtime())
today_list=today.split()
today_mon=int(today_list[0])
today_day=int(today_list[1])
today_year=int(today_list[2])

##or规定开始日期
# today_mon=3
# today_day=12
# today_year=2024


##生成一轮记忆的所有日期
#记忆一轮的所有日期
all_day_list=[]  
#用于循环的指针日期
temp_num=0 #该月份的天数
a=int(number_period)
b=today_day  #第一周的标志
c=today_year
d=today_mon
while (a>=1):     ## 将记忆周期按月划分并生成该月份的日期
    if d in all_month:# 判断是否为31天的月份
        if a<=32-b:
            temp_num=a
            a=0
        else:
            temp_num=32-b
            a=a-(32-b)
    elif d==2:   #二月
        if ((c%4==0) and (c%100!=0))or (c%400==0):  ##闰年
            if a<=30-b:
                temp_num=a
                a=0
            else:
                temp_num=30-b
            a=a-(30-b)   
        else:                                                                ##平年
            if a<=29-b:
                temp_num=a
                a=0
            else:
                temp_num=29-b
            a=a-(29-b)                  
    else:       #30天的月份
        if a<=31-b:
            temp_num=a
            a=0
        else:
            temp_num=31-b
            a=a-(31-b)
    for i in range(temp_num):
        all_day_list.append("{:}.{:}".format(d,b+i))
    if d<12:   ##月份递进
        d+=1
    else:
        d=1
        c+=1  ##年数递进
    b=1     ##第一月后清零    
    
    
##生成表格   
df=pd.DataFrame(columns=["daytime"]+all_day_list)   ##填入日期作为表头
df["daytime"]=[pd.NA]*(6*evynum)
newn=0 ##学习过的单元数
for i in range(1,len(all_day_list)+1):
    day_work=[]
    ##每天新学的任务
    s=evynum
    if i<=unit_number/evynum :
        while( newn<unit_number and s>0):
            newn+=1
            s-=1
            day_work.append("U{:}(学)".format(newn))
    elif unit_number%evynum!=0 and i==unit_number//evynum+1:
        while( newn<unit_number and s>0):
            newn+=1
            s-=1
            day_work.append("U{:}(学)".format(newn))
    ##每天复习的任务
    for x in day_list:
        if 1<=(i-x)<= (unit_number//evynum if unit_number%evynum==0 else unit_number//evynum+1):
            nrew=1
            while(nrew<=evynum):
                if (i-x-1)*evynum+nrew<=unit_number:
                    day_work.append("U{:}(复)".format((i-x-1)*evynum+nrew)) 
                nrew+=1
    df[all_day_list[i-1]]=pd.Series(day_work)           
df.to_excel("记忆曲线.xlsx")

