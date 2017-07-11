import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import MultipleLocator
matplotlib.rcParams.update({'font.size': 18})

# Import histograms
pnr_area = np.loadtxt('pnr_area.dat') # units of mVns
pnr_area_above_th = np.loadtxt('pnr_area_above_th.dat')
pnr_area_disc = np.loadtxt('pnr_area_disc.dat')

plt.figure(figsize=(8,6))
plt.step(pnr_area_disc[:,1], pnr_area_disc[:,0], where='mid', label='area (with \ndiscriminator)');
plt.step(pnr_area_above_th[:,1], pnr_area_above_th[:,0], where='mid', label='area (above \n$V_{th}$)');
plt.step(pnr_area[:,1],pnr_area[:,0], where='mid', label='area');
# plt.axvline(5604.84593463,color='black', label=r'$th_{01}$',linestyle='-.')
# plt.axvline(15921.253917,color='black', label=r'$th_{12}$', linestyle='--')
# limit plot range
plt.ylim(0,8000)
plt.xlim(0,40e3)

#change x axis scaling from mVns to mVus
ticks = (plt.gca().get_xticks()*10**-3).astype('int')
plt.gca().set_xticklabels(ticks)

plt.xlabel('area (mV $\mu$s)')
plt.ylabel('count')
plt.legend()

# plt.savefig('area_histos_comparison.eps')
plt.savefig('area_histos_comparison_with_thresholds.eps')

plt.show()