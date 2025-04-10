##追赶法解线性方程组
import numpy as np
def goahead(A,d):
    n =A.shape
    n=n[1]
    a=[]
    b=[]
    c=[]
    X=[]
#取出对角元素
    b=A[range(0,n),range(0,n)]
#取出次对角元素
    a=A[range(1,n),range(0,n-1)]
    c=A[range(0,n-1),range(1,n)]
    w=[]
    g=[]
    w.append(c[0]/b[0])
    g.append(d[0]/b[0])
    for x in range(1,n-1): 
       w.append(c[x]/(b[x]-a[x-1]*w[x-1]))
       g.append((d[x]-a[x-1]*g[x-1])/(b[x]-a[x-1]*w[x-1]))
    g.append((d[n-1]-a[n-2]*g[n-2])/(b[n-1]-a[n-2]*w[n-2]))
    X.append(g[n-1])
    for x in range(1,n):
        X.append(g[n-x-1]-w[n-x-1]*X[x-1])
    return X[::-1]

s=np.array([[2, -1, 0, 0, 0, 0],[-1, 2 ,-1 ,0 ,0 ,0],[0, -1, 2, -1, 0, 0],[0 ,0, -1 ,2 ,-1, 0],[0 ,0, 0 ,-1 ,2, -1],[0 ,0, 0 ,0 ,-1, 2]])
d=np.array([1,0,1,0,0,1])
ddd=goahead(s,d)