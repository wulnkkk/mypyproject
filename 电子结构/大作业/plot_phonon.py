# -*- coding: utf-8 -*-
"""
Created on Tue May 17 13:36:11 2022

@author: Zeyu
"""

import numpy as np
import matplotlib.pyplot as plt

freq = np.loadtxt('si.freq.gp')

plt.figure(dpi=300)
lw = 2
ymin=0
ymax=500 

for i in range(1,freq.shape[1]):
    plt.plot(freq[:,0],freq[:,i],color='r',lw=lw)

plt.xlim([0,freq[-1,0]])
plt.ylim([0,ymax])
plt.ylabel(r'Frquency ($\mathrm{cm}^{-1}$)',fontsize=18)

labels = ['G','X','K','G','L']
points = [0,30,40,60,90]


for i in points[1:-1]:
    plt.plot([freq[i,0],freq[i,0]],[ymin,ymax],'--k')

plt.xticks( freq[points,0],labels,fontsize=13)
