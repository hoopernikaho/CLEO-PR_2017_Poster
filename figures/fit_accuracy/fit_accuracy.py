import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rc('font',size=18)

DataFastPulse = np.genfromtxt('20170405_TES5_SQ1_fit_accuracy_80mK_iBias_104uA_7.2GHZ_100kOhm_fit_accuracy.dat',names=True)
DataSlowPulse = np.genfromtxt('20170126_TES5_n012_distinguishibility_20MHz_tau_vs_offset_fit_accuracy.dat',names=True)

print DataFastPulse.dtype.names
print 'fast mean-fwhm:{}'.format(np.mean(DataFastPulse['fwhm'][1:]))
print 'slow mean-fwhm:{}'.format(np.mean(DataSlowPulse['fwhm'][1:]))

def plotter(data, ecolor='blue', label=None):
	plt.errorbar(
		data['diode_separation'],
		data['centers'],
		xerr=data['diode_widths']/2,
		yerr=data['fwhm']/2,
		fmt='.',
		ecolor=ecolor,
		label=label)

plt.figure()
plt.plot(np.arange(0,1000), np.arange(0,1000), color='black')
plotter(DataFastPulse[1:],'blue',r'$\tau_{rise}$ = 100 ns')
plotter(DataSlowPulse[1:],'green',r'$\tau_{rise}$ = 176 ns')
plt.xlim(-50,1000),plt.ylim(-50,1000)
plt.xlabel('diode pulse separation (ns)')
plt.ylabel('estimated pulse separation (ns)')
plt.legend()
plt.savefig('fitted_vs_actual_pulse_separation.eps')
plt.show()