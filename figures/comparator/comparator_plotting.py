import matplotlib
matplotlib.rcParams.update({'font.size': 18})
import matplotlib.pyplot as plt
import numpy as np
import pulse_discrimination as pd
from matplotlib.ticker import MaxNLocator

height_th = 7.7 #mV

trace = np.loadtxt('sample_500ns_sep_trace')
# comparator = np.loadtxt('sample_500ns_sep_trace_comparator')

time, signal = trace[:,0]*1e6, trace[:,1]*1e3
"""
Edge detection
"""
[mask_backward, clamp, edges, left_edges_backward, right_edges_backward] = pd.discriminator(time, 
    signal, 
    height_th,
    dt_left=0,
    dt_right=0,
    method = 2
    )

"""
Edge detection with manual limits
"""
[mask_area, clamp, edges, left_edges_area, right_edges_area] = pd.discriminator(time, 
    signal, 
    height_th,
    dt_left=0,
    dt_right=1300e-9*1e6, # us
    method = 2
    )

#saves comparator data
np.savetxt('sample_500ns_sep_trace_CompBackward.dat',mask_backward)
np.savetxt('sample_500ns_sep_trace_CompforArea.dat',mask_area)

height_th = 0.0077
f, (ax1,ax2,ax3) = plt.subplots(3, 1, sharex=True, figsize=(8,6))
plt.tight_layout
plt.xlim(-2,7.5)
ax1.plot(time,signal,color='blue')
ax1.axhline(7.7, linestyle='--',color='black')
ax1.text(5.5, 7.7, 'SET')
ax1.axhline(0, linestyle='--',color='black')
ax1.text(5.5, 0, 'RESET')
plt.xlabel(r'time ($\mu$s)')
ax1.set_ylabel('voltage (mV)')
ax1.yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(10))

ax1.axvline(time[left_edges_backward[0]],color='red',linestyle='--')
ax1.axvline(time[right_edges_backward[-1]],color='red',linestyle='--')
ax2.axvline(time[left_edges_backward[0]],color='red',linestyle='--')
ax2.axvline(time[right_edges_backward[-1]],color='red',linestyle='--')
ax3.axvline(time[left_edges_backward[0]],color='red',linestyle='--')

ax3.axvline(time[right_edges_backward[-1]],color='red',linestyle='--')
ax3.axvline(time[right_edges_area[-1]],color='black',linestyle='-.')
ax3.annotate("",
            xytext=(time[right_edges_backward[-1]], 1.1), 
            xy=(time[right_edges_area[-1]], 1.1), 
            arrowprops=dict(arrowstyle="<->")
            )
ax3.text((time[right_edges_backward[-1]]+time[right_edges_area[-1]])/2,1.15,'$\Delta$ t',ha='center')

ax2.set_ylim(-0.5,1.5)
ax2.yaxis.set_major_locator(MaxNLocator(integer=True))
ax2.set_ylabel('logic')
ax2.plot(time,mask_backward,color='red')

ax3.set_ylim(-0.5,1.5)
ax3.yaxis.set_major_locator(MaxNLocator(integer=True))
ax3.plot(time,mask_area,color='black')
ax3.set_ylabel('logic')

# plt.legend(bbox_to_anchor=(1, 1),
#            bbox_transform=plt.gcf().transFigure)
ax1.text(-1.7,20,'(a)')
ax2.text(-1.7,1,'(b)')
ax3.text(-1.7,1,'(c)')

plt.savefig('comparator_at_500ns.eps')

plt.show()