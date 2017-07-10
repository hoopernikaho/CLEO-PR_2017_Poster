import numpy as np
import matplotlib.pyplot as plt

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
        plt.annotate('', (left, half_max), (right, half_max), arrowprops={'arrowstyle':'<->'})
        plt.text((left+right)/2, half_max, '{} ns'.format(fwhm), ha='center')
    return right-left #return the difference (full width)

def hist(data,bins=400,lims=None, label='', Plot=True, alpha=.3):
    """Creates and Plots numpy histogram, removing the last bin""" 
    y, binEdges = np.histogram(data,bins,range=(lims))
    if Plot:
        y_err = np.sqrt(y)
        step = binEdges[1]-binEdges[0]
        bins = binEdges[:-1]+step/2
        plt.bar(bins,y,yerr=y_err,alpha=alpha, width=step, label=label)
        plt.xlim(lims)
    return y, bins

plt.figure()
toa = np.loadtxt('time_of_arrival_at_0.00578330951457.txt')*1e9
toa = toa[(toa>-60) & (toa<60)]
freq, bins = hist(toa,bins=60,lims=[-70,50]) #2ns resolution = trace res
plt.xlabel('time of arrival (ns)')
plt.ylabel('count')
print FWHM(bins, freq)
plt.savefig('jitter_histo.eps')
plt.show()



