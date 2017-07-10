set terminal postscript eps enhanced color size 8.6cm, 6cm dl 3\
font "Helvetica, 16pt"
set output 'ph1_photon.eps'

unset key
unset bars
set xlabel 'Time ({/Symbol m}s)' enhanced
set ylabel 'Voltage (mV)' offset 2,0

plot 'ph1_model.dat' u ($1*1E6):($2*1E3) with lines lw 3 lc 'red'



