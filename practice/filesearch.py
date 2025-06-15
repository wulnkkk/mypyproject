import pandas as pd
import numpy as np
import re
try:
    df=pd.read_excel(r"C:\Users\zty\Downloads\2201班暑期实习统计（收集结果）.xlsx") #输入文件路径
except FileNotFoundError :                                      #异常处理
    print("未找到文件，请检查文件路径是否正确。")           
else:
    df.info()

#  保存  df.to_excel(r"C:\Users\86151\OneDrive\桌面\物理2201班4、6级成绩.xlsx")

'''   姓名自动填充
df需填充表，df1对照标准表


for i in range(len(df.姓名)):
    if df.姓名[i]=="-":
        for x in range(len(df1['提交者（自动）'])):
            if  df1["提交者（自动）"][x]==df["提交者（自动）"][i]:
                df["姓名"][i]=df1["姓名"][x]
                break
'''
'''
姓名学号分离


name=[]
index=[]
a=re.compile("学生：(\S+)-(\S+)-")
for i in df["姓名"]:
    if i=="-":
      name.append("-")
      index.append("-")
    else:
        name.append(a.findall(i)[0][0])
        index.append(a.findall(i)[0][1])
'''

'''
#随机数生成
print(df.simple())


'''