# -*- coding: utf-8 -*-
"""
Created on Tue May 17 11:04:52 2022

@author: Zeyu
"""
import numpy as np
import matplotlib.pyplot as plt

f=open('si.bands.dat')
ymin=-13
ymax=10
nband=4 # this is the valence band number, for insulators only

line=f.readline()
nbnd=int(line.split(',')[0].split('=')[1])
nks=int(line.split(',')[1].split('=')[1].split('/')[0])


eig=np.zeros((nks,nbnd),dtype=float)
q = np.zeros([nks,3])
for i in range(nks):
    l=f.readline()
    q[i] = np.float_(l.split())
    count=0
    if nbnd%10==0:
        n=nbnd//10
    else:
        n=nbnd//10+1
    for j in range(n):
        l=f.readline()
        for k in range(len(l.split())):
            eig[i][count]=l.split()[k]
            count=count+1
            
f.close()

eig_vbm=max(eig[:,nband-1])
eig_cbm=min(eig[:,nband])
Gap=eig_cbm-eig_vbm

lw=2
plt.figure(dpi=300)
for i in range(nbnd):
    line1=plt.plot( eig[:,i]-eig_vbm,color='r',linewidth=lw )
plt.ylim([ymin,ymax])
plt.xlim([0,nks-1]) 

labels = ['L','G','X','U','G']
points = [0,20,50,60,90]

for i in points[1:-1]:
    plt.plot([i,i],[ymin,ymax],'--k')

plt.xticks( points,labels )

plt.title("Band gap: %3.3f "%(Gap) + " eV")  # for insulators only
plt.ylabel('Energy (eV)',fontsize=18)

'''
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

p1=plt.subplot(1, 1, 1)

F=plt.gcf()
F.set_size_inches([3,5])
lw=1.2 # line width

plt.xlim([0,nks-1]) # 201 points
plt.ylim([ymin,ymax])
#plt.xlabel(r'$k (\AA^{-1})$',fontsize=16)
plt.ylabel(r' E (eV) ',fontsize=16)

eig_vbm=max(eig[:,nband-1])
eig_cbm=min(eig[:,nband])
Gap=eig_cbm-eig_vbm

plt.title("Band gap="+str(Gap)[0:8]+" eV")  # for insulators only
for i in range(nbnd):
    line1=plt.plot( eig[:,i]-eig_vbm,color='r',linewidth=lw ) 

vline=dline
while vline<nks-1:
    plt.axvline(x=vline, ymin=ymin, ymax=ymax,linewidth=lw,color='black')
    vline=vline+dline

plt.xticks( (0,30,60), ('X', r'${\Gamma}$', 'L') )
'''
