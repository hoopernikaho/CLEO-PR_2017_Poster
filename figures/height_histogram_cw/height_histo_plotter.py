import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import MultipleLocator
matplotlib.rcParams.update({'font.size': 18})

pnr_height = np.loadtxt('pnr_height.dat')
pnr_height_g0 = np.loadtxt('g0_component.dat')
pnr_height_g1 = np.loadtxt('g1_component.dat')

frequencies = pnr_height[:,0]
x_val = pnr_height[:,1]
g0 = pnr_height_g0[:,0]
g1 = pnr_height_g1[:,0]

plt.figure(figsize=(8,6))
plt.errorbar(x_val*1e3,frequencies,yerr=np.sqrt(frequencies),linestyle='',ecolor='black')
plt.plot(x_val*1e3,g0,color='blue',label='n = 0')
plt.plot(x_val*1e3,g1,color='red',label='n > 0')
plt.xlim(0,25)
plt.ylabel('counts')
plt.xlabel('height (mV)')
plt.axvline(0.00771864268507*1e3,linestyle='--',color='black', label='$V_{th}$ (SET)')
# plt.text(5,650,'n=0',ha='center')
# plt.text(16,100,'n>0',ha='center')
plt.tight_layout
plt.legend()

plt.savefig('height_histo.eps')
plt.show()