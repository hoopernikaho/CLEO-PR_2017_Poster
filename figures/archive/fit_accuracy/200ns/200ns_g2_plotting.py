import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 20})
def hist(data,bins=200,lims=None, label='', Plot=True, alpha=.5):
    """Creates and Plots numpy histogram, removing the last bin""" 
    y, binEdges = np.histogram(data,bins,range=(lims))
    if Plot:
        y_err = np.sqrt(y)
        step = binEdges[1]-binEdges[0]
        bins = binEdges[:-1]+step/2
        plt.bar(bins,y,yerr=y_err,alpha=alpha, width=step, label=label)
        plt.xlim(lims)
    return y, bins

data=np.array(np.genfromtxt('200ns_separation_offset_amplitude_init_data.txt',names=True))
tau = np.abs(data['one_x_offsets_init']-data['two_x_offsets_init'])*1e9
plt.figure()
# hist(tau,lims=[-10,10])
hist(tau,lims=[0,400])
plt.ylim(0,400)
plt.xlabel('TES pulse separation (ns)')
plt.ylabel('counts')

# def gauss_fit_three(tau,amps,sigmas,offsets):
# 	from lmfit.models import GaussianModel
# 	p = Parameters()
# 	    [p.add('g{}_center'.format(k + 2),
#            j,
#            # expr='g{}_center + Delta_E'.format(k + 1)
#            )
#      for k, j
#      in enumerate(offsets]

#     # amplitudes
#     [p.add('g{}_amplitude'.format(k),
#            j * min_peak_sep / np.sqrt(2),
#            expr='A * exp(-n_bar) * n_bar**{} / factorial({})'.format(k, k),
#            min=0)
#      for k, j
#      in enumerate(amps)]

#     # fixed width
#     [p.add('g{}_sigma'.format(k + 1),
#            min_peak_sep / np.sqrt(2) / np.pi,
#            min=0,
#            # expr='sigma_p * sqrt({})'.format(k + 1)
#            expr='sigma_p'
#            )
#      for k, _
#      in enumerate(sigmas]

# plt.semilogy()
plt.savefig('200ns_g2_bayesian.pdf')
plt.show()
# print data

