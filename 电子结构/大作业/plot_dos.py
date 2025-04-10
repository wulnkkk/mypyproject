# -*- coding: utf-8 -*-
"""
Created on Mon May 16 15:18:05 2022

@author: Zeyu
"""
import numpy as np
import matplotlib.pyplot as plt

f = open("si.dos.dat")
line = f.readline()
E_f = float(line.split()[-2])
f.close()   

dos= np.loadtxt('si.dos.dat')
dos[:,0] = dos[:,0]-E_f # shifted to Fermi energy

plt.figure(dpi=300)
plt.plot(dos[:,0],dos[:,1],color='b',lw=2)

plt.xlabel('Energy (eV)',fontsize=18)
plt.ylabel('electrons/eV',fontsize=18)
plt.xlim([-5,9])
plt.ylim([0,3])

dos_windows = dos[(dos[:,0]<2)&(dos[:,0]>-2)]

vbm = dos_windows[dos_windows[:,1]<1e-3][0,0]
cbm = dos_windows[dos_windows[:,1]<1e-3][-1,0]

print('The bandgap is %3.3f '%(cbm-vbm), 'eV')

plt.plot([cbm,cbm],[0,3],'--k',alpha=0.5)
plt.plot([vbm,vbm],[0,3],'--k',alpha=0.5)

