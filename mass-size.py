import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii
from astropy.table import join

data1 = ascii.read('table1.txt')
data2 = ascii.read('table2.txt')

cross = join(data1,data2, keys='Name')

logMHI = cross['logMHI']
MHI = 10**logMHI
FHI = cross['FHI']
D25 = cross['D25']

logMs = (logMHI - 9.71)/0.51 + 10
Mt = 10**logMHI + 10**logMs
logMt = np.log10(Mt)

D = np.sqrt(MHI/(2.356e5*FHI))
size = D25*0.000290888*D #Mpc
size = size*1000 #kpc

plt.scatter(logMt,size, label='O\'Neil et al. (2023)')
plt.scatter(np.log10(1.69e9),0.000145444*83.1*1000, label=r'J0613+52', c='orange')

plt.ylabel('size [kpc]')
plt.xlabel(r'$\log(M_\mathrm{total}/M_\odot)$')
plt.legend()
