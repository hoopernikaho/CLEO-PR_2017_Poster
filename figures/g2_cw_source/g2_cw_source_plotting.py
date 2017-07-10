"""
g2 plotting with modelling for CW source.
"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 16})

data_source = '20161116_TES5_20MHz_bwl_diode_n012_height_optimised'
filename = 'results_cont_2nspp_reduced.dat'
# g2 = np.load('/workspace/projects/TES/analysis/20161116_TES5_20MHz_bwl_diode_n012_height_optimised_results/taus_fit_using_edges_by_diff_hys_mcmc.npy')
data = np.array(np.genfromtxt(filename,names=True))
print data.dtype.names
g2 = data['two_x_offset']-data['one_x_offset']

def hist(data,numbins=400,lims=None, label='', plot=True, alpha=.5):
    """Creates and Plots numpy histogram, removing the last bin""" 
    y, binEdges = np.histogram(data,numbins,range=(lims))
    if plot:
        y_err = np.sqrt(y)
        step = binEdges[1]-binEdges[0]
        _bins = binEdges[:-1]+step/2
        # plt.bar(_bins,y,yerr=y_err,alpha=alpha, width=step, label=label, align='center')
        plt.errorbar(_bins,y,yerr=y_err,fmt='.',color='blue')
        plt.xlim(lims)
        # np.savetxt('g2_cw_binsize_{:.0f}ns_range_{:.0f}ns.dat'.format(np.diff(_bins)[0],lims[1]),
        # 	np.array(zip(_bins,y)),
        # 	header="arrival_time_separation(ns)\tcounts")
    return y, _bins

def model(numdata, bins, lims, plot=False):
	"""
	Free running coherent state g2 (expected)
	    Fixed Trace length T of bins
	    g2 length g2_T of g2_bins
	"""
	g2_T = np.diff(lims)*1e-9 
	# 10000e-9
	g2_bins = bins
	# 20
	T = (10-1.99999994344)*1e-6 # trace length - discriminator window around average single photon pulse = trace lengths containing only integer number of pulses
	dT = g2_T/g2_bins #g2 scope / bins in g2 scope
	bins = T/dT #bins in a trace
	# nbar = lambda bins: 40e3/.47*.872*dT #APD rates/ APD eff / TES eff / trace length
	# poiss = lambda k, nbar: nbar**k*np.exp(-1*nbar)/math.factorial(k) 
	prob = lambda tau,bins: 2/bins**2*(T-tau)/(dT)
	taus = np.linspace(dT/2,g2_T-dT/2,g2_bins)#g2 scope, bins in g2 scope
	if plot:
		plt.plot(taus*1e9,prob(taus,bins)*numdata,'-', linewidth=2, color='black')
        # np.savetxt('g2_cw_model_binsize_{:.0f}ns_range_{:.0f}ns.dat'.format(np.diff(taus*1e9)[0],lims[1]),
        # 	np.array(zip(taus*1e9, prob(taus,bins)*numdata)),
        # 	header="arrival_time_separation(n/	s)\tcounts(model)")
	return prob(taus,bins)*numdata

def redchisq(x,y,yerr,f):
	return np.sum(np.abs(np.abs(f-y)/yerr/(len(y)-2)))

if __name__ == '__main__':
	# print data
	diff = (data['two_amplitude']-data['one_amplitude'])
	sums = (data['two_amplitude']+data['one_amplitude'])
	print np.mean(sums)
	print np.sum(diff!=0)/np.sum(diff==0)
	plt.figure()
	plt.title('A2-A1')
	plt.hist(diff[diff!=0],50,range=[-1.5,1.5])
	plt.savefig('Amplitude_Differences_(MCMC).pdf')
	plt.figure()
	plt.title('A2+A1')
	plt.hist(sums[diff!=0],50,range=[.5,3.5])
	plt.savefig('Amplitude_Sums_(MCMC).pdf')
	plt.figure()
	plt.title('(A2-A1)/(A2+A1)*100')
	plt.hist((diff[diff!=0]/sums[diff!=0])*100,50)
	plt.savefig('Amplitude_Differences_percentage(MCMC).pdf')
	plt.figure(figsize=(30,20))
	plt.scatter(diff[diff!=0], g2[diff!=0]*1e9,marker='.')
	plt.ylim([np.min(g2[diff!=0]*1e9),np.max(g2[diff!=0]*1e9)])
	plt.ylabel('t2-t1 (nsec)')
	plt.xlabel('A2-A1')
	plt.tight_layout
	plt.savefig('Amplitude_Differences_time_difference.pdf')
	plt.figure()
	plt.scatter(data['two_amplitude'][diff!=0],data['one_amplitude'][diff!=0])
	plt.figure()
	plt.scatter(diff,sums)
	plt.xlabel('Difference')
	plt.ylabel('Sum')
	plt.savefig('Sum_vs_Difference.pdf')
	plt.figure()
	plt.scatter(data['one_amplitude'],data['two_amplitude'])
	plt.savefig('A2vsA1.pdf')
	plt.show()
	# bin_duration = 25 # ns
	# numbins = int(1200/bin_duration)
	# lims = [0,1200] #units ns

	# plt.figure()
	# plt.title('data folder = {}\n processed datafile: {}\n bin size = {}ns'.format(data_source, filename,bin_duration))
	# y, bins = hist(np.abs(g2*1e9),numbins=numbins,lims=lims, plot=True)
	# y_model = model(len(g2), numbins, lims, plot=True)
	# print redchisq(bins, y, np.sqrt(y), y_model)
	# plt.xlabel('pulse separation (ns)')
	# plt.ylabel('counts')
	# plt.savefig('g2_cw_binsize_{:.0f}ns_range_{:.0f}ns.eps'.format(np.diff(bins)[0],lims[1]), bbox_inches='tight')
	

	# numbins = 50
	# lims = [0,10000] #units ns

	# fig, ax = plt.subplots(figsize=(7, 6))
	# y, bins = hist(np.abs(g2*1e9),numbins=numbins,lims=lims, plot=True)
	# y_model = model(len(g2), numbins, lims, plot=True)
	# print redchisq(bins, y, np.sqrt(y), y_model)
	# # ax = plt.gca()
	# # start, end = ax.get_xlim()
	# # ax.xaxis.set_ticks(np.arange(start, end, 2000))
	# ticks = ax.get_xticks()*1e-9*1e6
	# ax.set_xticklabels(ticks)
	# plt.xlabel(r'pulse separation ($\mu$s)')
	# plt.ylabel('counts')
	# plt.ylim(bottom=0)
	# plt.savefig('g2_cw_binsize_{:.0f}ns_range_{:.0f}ns.eps'.format(np.diff(bins)[0],lims[1]), bbox_inches='tight')
	# plt.show()

	# plt.figure();plt.plot(bins,y);plt.scatter(bins,y_model);plt.show()