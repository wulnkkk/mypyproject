s1=open(r"Constant1.txt").read()
s2=open(r"Constant2.txt").read()
n=0
ss1=''
for i in s1:
    if 1<n<132:
        ss1+=i
    n+=1
n=0
ss2=''
for i in s2:
    if 1<n<132:
        ss2+=i
    n+=1
n=0
s=''
a=[]
for i in ss1:
    if n<5:
       s+=i
       n+=1
    else:
       a.append(s)
       s=i
       n=1
else:
       a.append(s)
n=0
s=''
b=[]
for i in ss2:
    if n<5:
       s+=i
       n+=1
    else:
       b.append(s)
       s=i
       n=1
else:
       b.append(s)