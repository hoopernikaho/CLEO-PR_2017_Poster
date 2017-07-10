set terminal postscript eps enhanced color size 8.6cm, 6cm dl 3\
font "Helvetica, 16pt"
set output 'jitter.eps'

unset key
unset bars
set xlabel 'Time ({/Symbol m}s)' enhanced
set ylabel 'Voltage (mV)' offset 2,0
set xrange [-2:6]

# plot for [data in FILES] data u ($1*1e6):($2*1e3) every 10 w lines lw .1 lc rgb "#110000FF"
set style fill solid 1

plot 'jitter.dat' u ($1 * 1E6) :($2 - $3):($2 + $3) w filledcurves fs solid lc 'grey', \
    'jitter.dat' u ($1 * 1E6):2 w lines lw 2 lc 'blue'