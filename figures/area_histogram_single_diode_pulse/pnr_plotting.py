import numpy as np
from thres_poiss import *
import matplotlib.pyplot as plt
import matplotlib
# import scipy.constants as consts

matplotlib.rcParams.update({'font.size': 18})


def hist(data, bins=400, lims=None, label='', Plot=True, alpha=.5):
    """Creates and Plots numpy histogram, removing the last bin"""
    y, binEdges = np.histogram(data, bins, range=(lims))
    step = binEdges[1] - binEdges[0]
    bins = binEdges[:-1] + step / 2
    if Plot:
        y_err = np.sqrt(y)
        plt.bar(bins, y, yerr=y_err, alpha=alpha, width=step, label=label)
        plt.xlim(lims)
    return y, bins


data = np.loadtxt('areas_single_diode_pulse.dat')
freq, bins = hist(data, bins=200, lims=[0, 5], Plot=False)

# saving the histogram data to a DAT file for plotting with external program
with open('hist.dat', 'w') as f:
    f.write('#bin\tfrequency\n')
    [f.write('{:.5f}\t{}\n'.format(j, k))
     for j, k
     in zip(bins, freq)]

""" plotting part"""
plt.figure('histogram')
plt.errorbar(bins, freq, yerr=np.sqrt(freq), fmt='o')
plt.xlabel(r'Pulse Area (pVs)')
plt.ylabel('counts')
plt.ylim([0, 650])
plt.text(0.6, 600, 'n=0', ha='center', weight='bold')
plt.text(1.1, 450, 'n=1', ha='center', weight='bold')
plt.text(1.7, 250, 'n=2', ha='center', weight='bold')
plt.text(2.4, 100, 'n=3', ha='center', weight='bold')
plt.text(3, 22, 'n=4', ha='center', weight='bold')
plt.tight_layout
plt.savefig('area_histo.pdf')

""" histogram fitting """
h = np.array(np.histogram(data, bins=200, range=(0, 5)))
result = gauss_fit_interp(h, min_peak_sep=0.2, threshold=.015, weighted=True)
# result.plot()
bin_fit = np.linspace(0, 5, int(1e4))
freq_fit = result.eval(x=bin_fit)
n_peaks = len(result.components)
compon = result.eval_components(x=bin_fit)
compon = [j[1] for j in compon.items()]

# saving the histogram fit to a DAT file for plotting with external program
with open('fit.dat', 'w') as f:
    f.write(('#bin\tfrequency' +
             '\tpeak{}' * n_peaks + '\n').format(*range(n_peaks)))
    [f.write(('{:.5f}\t{}' + '\t{}' * n_peaks + '\n').format(*j))
     for j
     in zip(bin_fit, freq_fit, *compon)]


""" plotting part"""
plt.figure('histogram with fit')
plt.plot(bin_fit, freq_fit, 'r-')
plt.errorbar(bins, freq, yerr=np.sqrt(freq), fmt='o')
plt.xlabel(r'Pulse Area (pVs)')
plt.ylabel('counts')
plt.ylim([0, 650])
plt.text(0.6, 600, 'n=0', ha='center', weight='bold')
plt.text(1.1, 450, 'n=1', ha='center', weight='bold')
plt.text(1.7, 250, 'n=2', ha='center', weight='bold')
plt.text(2.4, 100, 'n=3', ha='center', weight='bold')
plt.text(3, 22, 'n=4', ha='center', weight='bold')
plt.tight_layout
plt.savefig('area_histo.pdf')

# print(result.fit_report())
thresholds = thresholds_N(h, min_peak_sep=0.2, threshold=.015, weighted=True)

with open('threshold.dat', 'w') as f:
    f.write('#ph_number\tthreshold\n')
    [f.write('{}\t{}\n'.format(n, t)) for n, t in enumerate(thresholds)]
print(thresholds)
print(r'Reduce $\xi^2$ = {}'.format(result.result.redchi))
# plt.show()
