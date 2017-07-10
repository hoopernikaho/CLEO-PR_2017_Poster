"""
Script
    plots amplitude noise projection onto timing axis
    uses average pulse and error of pulse to search for smallest jitter.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.size'] = 20


def find_idx(time_v, t0):
    return np.argmin(np.abs(time_v - t0))


data = np.loadtxt('1ph_model_with_errors_(signal_f).txt')
time_f, signal_f, signal_var_f = data[:, 0], data[:, 1] * 1e3, data[:, 2] * 1e3

"""Select only a region where the pulse is one-to-one"""
sig_top = (signal_f + signal_var_f)[(time_f > -1e-7) & (time_f < 1e-7)]
sig_bot = (signal_f - signal_var_f)[(time_f > -1e-7) & (time_f < 1e-7)]
sig = signal_f[(time_f > -1e-7) & (time_f < 1e-7)]
time_less = time_f[(time_f > -1e-7) & (time_f < 1e-7)]

# jitter = lambda h: time_less[
#     find_idx(sig_bot, h)] - time_less[find_idx(sig_top, h)]


def jitter(h):
    return time_less[
        find_idx(sig_bot, h)] - time_less[find_idx(sig_top, h)]


"""Plots jitter as a function of signal height"""
jitters = map(jitter, sig)
min_jitter_at = sig[np.argmin(jitters)]
print ('Minimum jitter is {}ns at height {}'.format(
    np.min(jitters) * 1e9, min_jitter_at))


"""Export data for plotting with external file"""
with open('jitter.dat', 'w') as f:
    f.write('#time\tsignal\tDelta_sig\n')
    [f.write('{}\t{}\t{}\n'.format(*a))
     for a
     in zip(time_f, signal_f, signal_var_f)]

"""Plots intrinsic jitter concept diagram"""
plt.figure(figsize=[10, 8])
plt.fill_between(time_f * 1e9,
                 signal_f + signal_var_f,
                 signal_f - signal_var_f,
                 color='grey')
plt.plot(time_f * 1e9, signal_f, linewidth=2, color='black')
xmin = -500
xmax = 3000
ymin = -5
ymax = 20
plt.ylim(ymin, ymax)
plt.xlim(xmin, xmax)
plt.xlabel('time (ns)')
plt.ylabel('voltage (mV)')

plt.hlines(min_jitter_at, xmin, xmax, linestyle='--')
plt.vlines(time_less[find_idx(sig_top, min_jitter_at)] *
           1e9, ymin, min_jitter_at, linestyle='--')
plt.vlines(time_less[find_idx(sig_bot, min_jitter_at)] *
           1e9, ymin, min_jitter_at, linestyle='--')

plt.annotate('',
             (time_less[find_idx(sig_top, min_jitter_at)] * 1e9, 0),
             (time_less[find_idx(sig_bot, min_jitter_at)] * 1e9, 0),
             arrowprops={'arrowstyle': '<->'})

# 22 ns from ./intrinsic_jitter_histogram/
plt.text(0, 0, r'FWHM$\approx$22 ns ', va='bottom', ha='left')
plt.tight_layout
plt.savefig('jitter.eps')
plt.show()
