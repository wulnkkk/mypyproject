from scipy.constants import *
def fun(x):
    return (1-x/40)*(1-x/80)

R=[]
S=[]
for i in range(0,130):
    if fun(i)<0 or fun(i)>1:
        R.append(i)
    else:
        S.append(i)