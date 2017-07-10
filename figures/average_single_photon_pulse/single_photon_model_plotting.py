import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # data_folder = '/workspace/projects/TES/analysis/20161116_TES5_20MHz_bwl_diode_n012_height_optimised_results/'
    # data_folder =
    # '/workspace/projects/TES/data/20160906_TES5_MAGSQ1_7ns_double_pulse/20MHz_bw/results/'
    ph1_model = np.load('ph1_model.npy')
    time_f = ph1_model[:, 0]
    print('sampling rate = {:.2f} ns pp'.format((time_f[1] - time_f[0]) * 1e9))
    ph1_f = ph1_model[:, 1]
    plt.figure('Sample single pulse')
    # plt.xlim(xmax=400)
    plt.plot(time_f * 1e9, ph1_f)
    plt.ylabel('Voltage (V)')
    plt.xlabel('time (ns)')
    plt.savefig('sample_pulse_for_fitting.eps')
    plt.show()


with open('ph1_model.dat', 'w') as f:
    f.write('#time\tvoltage\n')
    [f.write('{}\t{}\n'.format(t, v))
     for t, v
     in zip(ph1_model[:, 0], ph1_model[:, 1])]
