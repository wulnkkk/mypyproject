import pandas as pd ,numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import norm 
from scipy.optimize import curve_fit
from scipy.signal import find_peaks ,peak_widths
plt.rcParams ['font.sans-serif'] = ['Simhei']

df=pd.read_csv(r"D:\zty\Documents\mypyproject\现代实验\实验七穆斯堡尔效应实验\能谱数据8.csv",encoding="ANSI",header=5)
plt.title("")
plt.xlabel("道址")
plt.ylabel("计数")
plt.scatter(df["通道1道址"],df["通道1计数"],3)
plt.plot(df["通道1道址"],df["通道1计数"])
plt.show()