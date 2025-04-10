# -*- coding: utf-8 -*-
"""
Created on Mon May 16 15:18:05 2022

@author: Zeyu
"""
import numpy as np
import matplotlib.pyplot as plt

f = open("al.dos.dat")
line = f.readline()
E_f = float(line.split()[-2])
f.close()   

dos= np.loadtxt('al.dos.dat')
dos[:,0] = dos[:,0]-E_f # shifted to Fermi energy

plt.figure(dpi=300)
plt.plot(dos[:,0],dos[:,1],color='b',lw=1.5)

plt.xlabel('Energy (eV)',fontsize=18)
plt.ylabel('electrons/eV',fontsize=18)
#plt.xlim([-5,9])
plt.xlim([-15,10])
plt.plot([0,0],[0,0.8],'--k')
plt.ylim([0,0.8])


dos_windows = dos[(dos[:,0]<0)&(dos[:,0]>-14)]
e_0 = dos_windows[dos_windows[:,1]>1e-2][0,0]


dos_2 = dos_windows[dos_windows[:,0]>e_0]
fit_p  = np.polyfit(dos_2[:,0]-e_0, dos_2[:,1]**2, 1)
x_ = np.linspace(e_0,10)
plt.plot(x_,np.sqrt(fit_p[0]*(x_ - e_0)),color='red',lw = 2,label = 'Free electron gas')
plt.legend(fontsize=15,frameon=False)
'''
vbm = dos_windows[dos_windows[:,1]<1e-3][0,0]
cbm = dos_windows[dos_windows[:,1]<1e-3][-1,0]

print('The bandgap is %3.3f '%(cbm-vbm), 'eV')

plt.plot([cbm,cbm],[0,3],'--k',alpha=0.5)
plt.plot([vbm,vbm],[0,3],'--k',alpha=0.5)
'''
