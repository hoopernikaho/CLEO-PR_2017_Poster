import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import MultipleLocator
matplotlib.rcParams.update({'font.size': 18})

# import area histogram
pnr_area_disc = np.loadtxt('pnr_area_disc.dat')
frequencies = pnr_area_disc[:,0]
x_val = pnr_area_disc[:,1] # all x vals are area in units mVns

# import fitted components
pnr_g1 = np.loadtxt('g1_area_component.dat')
pnr_g2 = np.loadtxt('g2_area_component.dat')
g1 = pnr_g1[:,0]
g2 = pnr_g2[:,0]

plt.figure(figsize=(8,6))
plt.errorbar(x_val,frequencies,
             yerr=np.sqrt(frequencies),
             linestyle='-',
             ecolor='black',
             color='black',
            label='$C(a)$'
            )
plt.plot(x_val,g1,color='blue',label='n=1')
plt.plot(x_val,g2,color='red',label='n=2')
plt.axvline(5604.84593463,color='black', label=r'$th_{01}$')
plt.axvline(15921.253917,color='black', label=r'$th_{12}$', linestyle='--')

plt.ylim(0,6000)
plt.xlim(0,30e3)

ticks = (plt.gca().get_xticks()*10**-3).astype('int')
plt.gca().set_xticklabels(ticks)

plt.xlabel('area (mV $\mu$s)')
plt.ylabel('count')

plt.legend()
plt.savefig('area_histo_with_fit.eps')

plt.show()

