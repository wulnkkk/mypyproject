##二分法
import numpy as np

def cir(x):
    y=np.sin(x)-x**2/4
    return y

err=1e-5
x1=1.5
x2=2
while abs(np.linalg.norm([cir(x1) ,cir(x2)])) > err :
    a=(x1+x2)/2
    if cir(a)*cir(x1)<=0:
        x2=a
    else:
        x1=a
    

