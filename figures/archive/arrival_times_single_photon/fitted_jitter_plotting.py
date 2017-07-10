import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.size']=20
def FWHM(X,Y,plot=True):
    X=np.array(X)
    Y=np.array(Y)
    half_max = np.max(Y) / 2
    #find when function crosses line half_max (when sign of diff flips)
    #take the 'derivative' of signum(half_max - Y[])
    d = np.sign(half_max - np.array(Y[0:-1])) - np.sign(half_max - np.array(Y[1:]))
    #plot(X,d) #if you are interested
    #find the left and right most indexes
    
    left_idx = np.where(d > 0)
    right_idx = np.where(d < 0)

    left = X[left_idx][0]
    right = X[right_idx][-1]
    print left, right
    fwhm = right-left
    if plot:
        plt.annotate('', (left, half_max), (right, half_max), arrowprops={'arrowstyle':'<->'}, weight='5')
        plt.text((left+right)/2, half_max, '{:.0f} ns'.format(fwhm), ha='center', va='bottom', weight='bold')
    return right-left #return the difference (full width)

shifts_f=np.load('single_photon_arrival_times_using_horizontal_offset_corrected_model.npy')
"""Arrival Times"""
plt.figure(figsize=[10,8])
t_hist = np.histogram(np.array(shifts_f)*1e9, bins=100, range=[200,600])
# plt.hist(np.array(shifts_f)*1e9, bins=100, range=[200,600], alpha=0.5, label='with shift', histtype='step')
freq = t_hist[0]
bins = t_hist[1][:-1]+np.diff(t_hist[1])[0]/2
plt.bar(bins, freq, yerr=np.sqrt(freq), width=np.diff(bins)[0], align='center',color='blue',edgecolor='blue', ecolor='black',linewidth=None)
plt.title('')
plt.xlabel('time of arrival (ns)')
plt.ylabel('counts')
# plt.legend()
FWHM(bins, freq, plot=True)
plt.xlim(250,450)
# plt.semilogy()
plt.savefig('arrival_time_for_single_photons.pdf')
plt.show()