import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
plt.rcParams ['font.sans-serif'] = ['Simhei'] #显示中文
plt.rcParams['axes.unicode_minus'] = False # 显示负号


#光谱定标

f0=open('D:\zty\Documents\mypyproject\大学物理实验\光谱仪的波长定标与色度测量\zty\zty0.DAT',"r")
f1=open('D:\zty\Documents\mypyproject\大学物理实验\光谱仪的波长定标与色度测量\zty\zty1.DAT',"r")

#读取数据
d0=f0.read() 
d1=f1.read()
#数据规整
d0=d0.split()
d1=d1.split() 
d0n=len(d0)
d0x=[]
d0y=[]
d1n=len(d1)
d1x=[]
d1y=[]
for i in range(0,d0n,2): #注意字符串转浮点
    d0x.append(eval(d0[i]))
    d0y.append(eval(d0[i+1]))
for i in range(0,d1n,2): #注意字符串转浮点
    d1x.append(eval(d1[i]))
    d1y.append(eval(d1[i+1]))

# 寻峰
# 使用 scipy.signal.find_peaks 寻找峰值,可以先画图再决定最低阈值
peaks, _ = find_peaks(d0y, height=2000, distance=10)
xp=[]
yp=[]
for peak in peaks:
    xp.append(d0x[peak])
    yp.append(d0y[peak])

peaks1, _ = find_peaks(d1y, height=5000, distance=10)
xp1=[]
yp1=[]
for peak in peaks1:
    xp1.append(d1x[peak])
    yp1.append(d1y[peak])
#作图
# plt.figure(dpi=200) #图片清晰度 
# plt.title("光谱仪第一次定标")
# plt.xlabel("波长$\lambda$(nm)")
# plt.ylabel('相对光强')
# plt.plot(d0x,d0y,label="汞的特征谱线")
# plt.scatter(xp,yp,15 ,color="r",marker='x', label='特征峰值')
# plt.text(xp[0]+1,yp[0]+100,"({:.2f}nm,{:})".format(404.66,yp[0]))
# plt.text(xp[1]+1,yp[1]+100,"({:.2f}nm,{:})".format(435.83,yp[1]))
# plt.text(xp[2]+1,yp[2]+100,"({:.2f}nm,{:})".format(546.07,yp[2]))
# plt.text(xp[3]-60,yp[3]+100,"({:.2f}nm,{:})".format(576.96,yp[3]))
# plt.text(xp[4],yp[4]+1000,"({:.2f}nm,{:})".format(579.07,yp[4]))
# plt.legend()
# plt.show()

# plt.figure(dpi=200) #图片清晰度 
# plt.title("光谱仪第二次定标")
# plt.xlabel("波长$\lambda$(nm)")
# plt.ylabel('相对光强')
# plt.plot(d1x,d1y,label="汞的特征谱线")
# plt.scatter(xp1,yp1,15 ,color="r",marker='x', label='特征峰值')
# plt.text(xp1[0]+1,yp1[0]+100,"({:.2f}nm,{:})".format(546.07,yp1[0]))
# plt.text(xp1[1]+1,yp1[1]+100,"({:.2f}nm,{:})".format(576.96,yp1[1]))
# plt.text(xp1[2]+1,yp1[2]+100,"({:.2f}nm,{:})".format(579.07,yp1[1]))
# plt.legend()
# plt.show()

#led灯的光谱

# 计算半高宽
def calculate_fwhm(wavelength, intensity, peak_index):
    peak_height = intensity[peak_index]
    half_height = peak_height / 2.0
    # 找到峰值两侧的半高点
    left_idx = np.where(intensity[:peak_index] <= half_height)[0][-1]
    right_idx = np.where(intensity[peak_index:] <= half_height)[0][0] + peak_index
    # 计算半高宽
    fwhm = wavelength[right_idx] - wavelength[left_idx]
    return fwhm, left_idx, right_idx

rd=open(r'D:\zty\Documents\mypyproject\大学物理实验\光谱仪的波长定标与色度测量\zty\red.DAT','r')
bd=open(r'D:\zty\Documents\mypyproject\大学物理实验\光谱仪的波长定标与色度测量\zty\bule.DAT','r')
yd=open(r'D:\zty\Documents\mypyproject\大学物理实验\光谱仪的波长定标与色度测量\zty\yelow.DAT','r')
#读取数据
r=rd.read() 
b=bd.read()
y=yd.read()
#数据规整
r=r.split()
b=b.split() 
y=y.split() 

rn=len(r)
rx=[]
ry=[]
bn=len(b)
bx=[]
by=[]
yn=len(y)
yx=[]
yy=[]
for i in range(0,rn,2): #注意字符串转浮点
    rx.append(eval(r[i]))
    ry.append(eval(r[i+1]))
for i in range(0,d1n,2): #注意字符串转浮点
    bx.append(eval(b[i]))
    by.append(eval(b[i+1]))
for i in range(0,d1n,2): #注意字符串转浮点
    yx.append(eval(y[i]))
    yy.append(eval(y[i+1]))
rx=np.array(rx)
ry=np.array(ry)
bx=np.array(bx)
by=np.array(by)
yx=np.array(yx)
yy=np.array(yy)
# 寻峰并计算半峰宽
# 使用 scipy.signal.find_peaks 寻找峰值,可以先画图再决定最低阈值
rpeaks, _ = find_peaks(ry, height=4.8e4, distance=100)
rxp=[]
ryp=[]
for peak in rpeaks:
    rxp.append(rx[peak])
    ryp.append(ry[peak])

bpeaks, _ = find_peaks(by, height=2.8e4, distance=100)
bxp=[]
byp=[]
for peak in bpeaks:
    bxp.append(bx[peak])
    byp.append(by[peak])

ypeaks, _ = find_peaks(yy, height=5.3e3, distance=200)
yxp=[]
yyp=[]
for peak in ypeaks:
    yxp.append(yx[peak])
    yyp.append(yy[peak])

# 遍历所有峰值，计算半高宽

rfwhm, rleft_idx, rright_idx = calculate_fwhm(rx,ry , rpeaks[0])
print(f"Peak at wavelength {rx[rpeaks[0]]:.2f} nm, FWHM: {rfwhm:.2f} nm")
bfwhm, bleft_idx, bright_idx = calculate_fwhm(bx,by , bpeaks[0])
print(f"Peak at wavelength {bx[bpeaks[0]]:.2f} nm, FWHM: {bfwhm:.2f} nm")
yfwhm, yleft_idx, yright_idx = calculate_fwhm(yx,yy , ypeaks[0])
print(f"Peak at wavelength {yx[ypeaks[0]]:.2f} nm, FWHM: {yfwhm:.2f} nm")
#作图
plt.figure(dpi=200) #图片清晰度 
plt.title("led红黄蓝光的光谱")
plt.xlabel("波长$\lambda$(nm)")
plt.ylabel('相对光强')
plt.plot(rx,ry,"red",label="红光的谱线")
plt.plot(bx,by,"blue",label="蓝光的谱线")
plt.plot(yx,yy,"yellow",label="黄光的谱线")
plt.axvline(rx[rleft_idx], color='b', linestyle='--', linewidth=1)
plt.axvline(rx[rright_idx], color='b', linestyle='--', linewidth=1)
plt.axvline(yx[yleft_idx], color='r', linestyle='--', linewidth=1)
plt.axvline(yx[yright_idx], color='r', linestyle='--', linewidth=1)
plt.axvline(bx[bleft_idx], color='orange', linestyle='--', linewidth=1)
plt.axvline(bx[bright_idx], color='orange', linestyle='--', linewidth=1)
plt.scatter([rxp,bxp,yxp],[ryp,byp,yyp],50 ,color="g",marker='x', label='特征峰值')
plt.text(rxp[0],ryp[0]+1000,"({:.2f}nm,{},{:.2f}nm)".format(rxp[0],int(ryp[0]),rfwhm))
plt.text(bxp[0],byp[0]+1000,"({:.2f}nm,{},{:.2f}nm)".format(bxp[0],int(byp[0]),bfwhm))
plt.text(yxp[0]-100,yyp[0]+1000,"({:.2f}nm,{},{:.2f}nm)".format(yxp[0],int(yyp[0]),yfwhm))
plt.legend()
plt.show()