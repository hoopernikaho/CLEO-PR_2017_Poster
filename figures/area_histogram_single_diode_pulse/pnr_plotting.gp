set terminal postscript eps enhanced color size 8.6cm, 6cm dl 3\
font "Helvetica, 16pt"
set output 'area_histo.eps'

unset key
unset bars
set xlabel 'area (mV ns)' enhanced
set ylabel 'counts' offset 2,0
set xrange [0:5]

set label 10 'n=0' font 'Helvetica,24' center at .35, 650
set label 11 'n=1' font 'Helvetica,24' center at 1.05, 500
set label 12 'n=2' font 'Helvetica,24' center at 1.7, 400
set label 13 'n=3' font 'Helvetica,24' center at 2.35, 300
set label 14 'n=4' font 'Helvetica,24' center at 3.05, 200
set label 15 'n{/Symbol \263}5' font 'Helvetica,24' center at 4, 100

# plt.text(0.6, 600, 'n=0', ha='center', weight='bold')
# plt.text(1.1, 450, 'n=1', ha='center', weight='bold')
# plt.text(1.7, 250, 'n=2', ha='center', weight='bold')
# plt.text(2.4, 100, 'n=3', ha='center', weight='bold')
# plt.text(3, 22, 'n=4', ha='center', weight='bold')


plot 'fit.dat' u 1:2 w lines lc 'red' lw 2 notitle, \
    'hist.dat' u 1:2:(sqrt($2)) w yerrorbar pt 6 lc 'blue' lw 2 ps .7 notitle, \
    'threshold.dat' using 2:(700) with impulses lc rgb 'grey' lw 1.5 #,\
    # 'threshold.dat' using ($2 - .7 ):(650) w label
    # for [cf=2:6] 'fit.dat' u 1:(column(cf)) w lines lc 'black' lw 1 notitle