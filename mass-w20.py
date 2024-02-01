import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii

datadir = 'table2.txt'
data = ascii.read(datadir)

W20 = data['W20']
logMHI = data['logMHI']

logMs = (logMHI - 9.71)/0.51 + 10
Mt = 10**logMHI + 10**logMs
logMt = np.log10(Mt)

#'O\'Neil et al. (2023)'
plt.scatter(logMHI,W20, label=r'$M_\mathrm{HI}$')
plt.scatter(logMs,W20, label=r'$M_\mathrm{total}$')
plt.scatter(np.log10(1.69e9),196, label=r'J0613+52', c='orange')
plt.errorbar(np.log10(1.69e9), 196, yerr=15, fmt="o", c='orange')
plt.ylabel(r'$W_{20}$ [km/s]')
plt.xlabel(r'$\log(M/M_\odot)$')
plt.legend()
#plt.xscale('log')


