import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.size']=20

def srlatch(_signal,reset_th, set_th):
    """
    Implements a two level discriminator, returning a mask
    """
    s=[_signal>set_th][0]
    r=[_signal<reset_th][0]
    L = len(_signal)
    q=np.zeros(L)
    qrev=np.zeros(L)
    # print s,r,q
    for i in np.arange(L):
        if ((s[i]==0)&(r[i]==0)&(i>0)):
            q[i]=q[i-1]
        elif ((s[i]==0)&(r[i]==1)):
            q[i]=0
        elif ((s[i]==1)&(r[i]==0)):
            q[i]=1
        else:
            q[i]==-1 #error
    return np.array(q)

def FWHM(X,Y,plot=True):
    half_max = np.max(Y)/2
    logic = srlatch(Y, reset_th=half_max, set_th=half_max)
    # plt.scatter(X,logic*0.04,label='logic')
    # plt.plot(X[1:],np.diff(logic)*0.04,label='difflogic')
    left = X[1:][np.diff(logic)==1][0]
    right = X[1:][np.diff(logic)==-1][-1]
    print left, right, half_max
    fwhm = right-left
    if plot:
        plt.annotate('', (left, half_max), (right, half_max), 
            arrowprops={'arrowstyle':'<->'}, weight='5')
        plt.text((left+right)/2, half_max, '{:.1f} ns'.format(float(fwhm)), 
            ha='center', va='bottom')
    return fwhm

def histbincenters(data,numbins,binrange):
    """
    creates histogram but returns bin centers instead of edges
    """
    freq, bins = np.histogram(data, bins=numbins, range=binrange, normed=True)
    bins = bins[:-1]+np.diff(bins)[0]/2 #bin centers = upshift bin edges by half a bin size, pop last. 
    return bins, freq

fastpulse_arrivaltimes=np.loadtxt('20170405_TES5_SQ1_fit_accuracy_80mK_iBias_104uA_7.2GHZ_100kOhm_single_photon_arrival_times.dat')*1e9
slowpulse_arrivaltimes=np.loadtxt('20170126_TES5_n012_distinguishibility_20MHz_tau_vs_offset_single_photon_arrival_times.dat')*1e9

numbins = 100
binrange = [270,450]

plt.figure()
plt.hist(fastpulse_arrivaltimes,
    bins=numbins,
    range=binrange,
    histtype='step',
    normed=True,
    label=r'$\tau_{rise}=$100 ns, $\sigma_0$= 2.0mV')
FWHM(*histbincenters(fastpulse_arrivaltimes,numbins=numbins,binrange=binrange))

plt.hist(slowpulse_arrivaltimes,
    bins=numbins,
    range=binrange,
    histtype='step',
    normed=True,
    label=r'$\tau_{rise}=$176 ns, $\sigma_0$= 1.5mV')

FWHM(*histbincenters(slowpulse_arrivaltimes,numbins=numbins,binrange=binrange))

plt.xlabel('arrival time (ns)')
plt.ylabel('probability')
plt.ylim(top=0.06)
plt.legend()
plt.savefig('arrival_time_for_single_photons.eps')
plt.show()
