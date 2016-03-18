#!/usr/bin/env python2.7

import sys
import os
import glob
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import rc
import math
import matplotlib.ticker
from mpl_toolkits.axes_grid1 import make_axes_locatable
import re

rc('text',usetex=True)
rc('font',family='serif')
rc('text.latex', preamble='\usepackage[dvipsnames]{xcolor}')

######## Path and Files Definition ################################
#impath = '/physics2/mscheuch/TVIR*/Output_files/Ts_outs/'
#impath = '/physics2/mscheuch/XVIR*/Output_files/Ts_outs/'
#impath = '/physics2/mscheuch/MFP*/Output_files/Ts_outs/'
#impath = '/physics2/mscheuch/ax*/Output_files/Ts_outs/'
#impath = '/physics2/mscheuch/POP*/Output_files/Ts_outs/'
impath = '/physics2/mscheuch/fstar*/Output_files/Ts_outs/'
#parameter = r'$T_{VIR}$' #Parameter studied here
#parameter = r'$Tvir_{X}$' #Parameter studied here
#parameter = r'$MFP$' #Parameter studied here
#parameter = r'$\alpha_{X}$' #Parameter studied here
#parameter = r'$POP_{early}$' #Parameter studied here
parameter = r'$f_{*}$' #Parameter studied here
#paroutfile = 'TVIR'
#paroutfile = 'TvirX'
#paroutfile = 'MFP'
#paroutfile = 'alphaX'
#paroutfile = 'POP'
paroutfile = 'fstar'
#parinname = True   # if true, set whichpar to change parval in "if (parinname)"
#whichpar = -3
#['', 'physics2', 'mscheuch', 'ax01', 'Output', 'files', 'Ts', 'outs', 'global', 'evolution', 'zetaIon31.50', 'Nsteps40', 'zstep1.000', '3.0e+55', '1.5', '1.0e+04', '2', '200', '300Mpc']
parinname = False
parval = ['0.05','0.15','0.1']
logx = 0
logy = 0
###################################################################

print '\n**********************************'
print '***** Start: plotglobal.py *********'
print '**********************************\n'

colors = ['black', 'red', 'blue', 'green', 'brown', 'orange', 'cyan', 'magenta', 'violet', 'limegreen', 'royalblue', 'yellowgreen', 'plum', 'yellow']
lines = ['-','--',':','-.']
#titles = ['zeta_10e55','zeta_10e57']

plt.ioff()
fig = plt.subplots(3,2, figsize=(15,20))
plt.subplots_adjust(bottom=0.15, hspace=0.001)
ax1 = plt.subplot(321)
ax2 = plt.subplot(323, sharex=ax1)
ax3 = plt.subplot(325, sharex=ax1)
ax4 = plt.subplot(322)
ax5 = plt.subplot(324, sharex=ax4)
ax6 = plt.subplot(326)

######### Reading in files #########
i=0
for filename in glob.glob(impath+'global_evolution*'):
    items = re.split('_zetaX|_alphaX|_TvirminX|_Pop|_|/',filename)
    if (parinname):
        parval = items[whichpar]
        setlabel = parameter + '=$%s$' %(parval)
        ax1.set_title('Study of ' +parameter+ '(DIM=$%s^{3}$)' %(items[-2]))

    else:
        setlabel = parameter + '=$%s$' %(parval[i])
        ax1.set_title('Study of ' +parameter+ '(DIM=$%s^{3}$)' %(items[-2]))

    print items
    data = np.genfromtxt(filename, unpack=True)
    z = data[0][1:]
    nf = data[1][1:]
    tk = data[2][1:]
    xe = data[3][1:]
    ts = data[4][1:]
    tb = data[5][1:]
    jalpha = data[6][1:]
    jstar = data[7][1:]
    jx = data[8][1:]
    xalpha = data[9][1:]
    xheat = -data[10][1:]
    xion = -data[11][1:]
    fcol = data[12][1:]
    if (i==0):
        leg1, = ax1.plot(z, ts, marker='',linestyle=lines[0],color=colors[i],linewidth=2)
        label1=r'$T_{s}$'
        leg2, = ax1.plot(z, tk, marker='',linestyle=lines[1],color=colors[i],linewidth=2)
        label2=r'$T_{k}$'
        leg3, = ax1.plot(z, tb, marker='',linestyle=lines[2],color=colors[i],linewidth=2)
        label3=r'$T_{\gamma}$'
        leg4, = ax2.plot(z, nf, marker='',linestyle=lines[0],color=colors[i],linewidth=2)
        label4=r'$X_{HI}$'
        leg5, = ax2.plot(z, xe, marker='',linestyle=lines[1],color=colors[i],linewidth=2)
        label5=r'$X_{e}$'
        leg6, = ax2.plot(z, fcol, marker='',linestyle=lines[2],color=colors[i],linewidth=2)
        label6=r'$f_{coll}$'
        leg7, = ax3.plot(z, jalpha, marker='',linestyle=lines[0],color=colors[i],linewidth=2)
        label7=r'$J_{\alpha}$'
        leg7, = ax3.plot(z, jstar, marker='',linestyle=lines[1],color=colors[i],linewidth=2)
        label10=r'$J_{\alpha,*}$
        leg10, = ax3.plot(z, jx, marker='',linestyle=lines[2],color=colors[i],linewidth=2)
        label11=r'$J_{\alpha,x}$'
        leg11, = ax4.plot(z, xheat, marker='',linestyle=lines[1],color=colors[i],linewidth=2)
        label8=r'$X_{heat}$'
        leg9, = ax5.plot(z, xion, marker='',linestyle=lines[3],color=colors[i],linewidth=2)
        label9=r'$X_{ion}$'
        ax1.plot([], [], marker='',linestyle=lines[0],label=setlabel,color=colors[i],linewidth=2)
        ax2.plot([], [], marker='',linestyle=lines[1],label=setlabel,color=colors[i],linewidth=2)
        ax3.plot([], [], marker='',linestyle=lines[0],label=setlabel,color=colors[i],linewidth=2)
        ax4.plot([], [], marker='',linestyle=lines[1],label=setlabel,color=colors[i],linewidth=2)
        ax5.plot([], [], marker='',linestyle=lines[3],label=setlabel,color=colors[i],linewidth=2)
    else:
        ax1.plot(z, ts, marker='',linestyle=lines[0],label=setlabel,color=colors[i],linewidth=2)
        ax1.plot(z, tk, marker='',linestyle=lines[1],color=colors[i],linewidth=2)
        ax1.plot(z, tb, marker='',linestyle=lines[2],color=colors[i],linewidth=2)
        ax2.plot(z, nf, marker='',linestyle=lines[0],color=colors[i],linewidth=2)
        ax2.plot(z, xe, marker='',linestyle=lines[1],label=setlabel,color=colors[i],linewidth=2)
        ax2.plot(z, fcol, marker='',linestyle=lines[2],color=colors[i],linewidth=2)
        ax3.plot(z, jalpha, marker='',linestyle=lines[0],label=setlabel,color=colors[i],linewidth=2)
        ax3.plot(z, jstar, marker='',linestyle=lines[1],label=setlabel,color=colors[i],linewidth=2)
        ax3.plot(z, jx, marker='',linestyle=lines[2],label=setlabel,color=colors[i],linewidth=2)
        ax4.plot(z, xheat, marker='',linestyle=lines[1],label=setlabel,color=colors[i],linewidth=2)
        ax5.plot(z, xion, marker='',linestyle=lines[3],label=setlabel,color=colors[i],linewidth=2)
    i=i+1

#ax1.set_xlabel('z')
ax1.set_ylabel(r'$\bar T [K]$')
ax1.set_yscale('log')
ax1.set_ylim([0,1000])
legend1 = ax1.legend([leg1,leg2,leg3],[label1,label2,label3],loc=4,frameon=True)
plt.gca().add_artist(legend1)
ax1.legend(loc=1,frameon=False)

ax2.set_xlabel('z')
ax2.set_ylabel(r'$\bar X $')
ax2.set_yscale('log')
legend2 = ax2.legend([leg4,leg5,leg6],[label4,label5,label6],loc=4,frameon=True)
plt.gca().add_artist(legend2)
ax2.legend(loc=1,frameon=False)

#ax3.set_xlabel('z')
ax3.set_ylabel(r'$J_{\alpha} [\gamma m^{-2} s^{-1} Hz^{-1} sr^{-1}]$')
ax3.set_yscale('log')
legend3 = ax3.legend([leg7, leg10, leg11],[label7, label10, label11],loc=4,frameon=True)
plt.gca().add_artist(legend3)
ax3.legend(loc=1,frameon=False)
#ax3.set_ylim([10**2,10**2])
#ax3.grid(True)

ax4.set_xlabel('z')
ax4.set_ylabel(r'$[\gamma_{X} s^{-1} Hz^{-1} baryon^{-1}]$')
ax4.set_yscale('log')
legend4 = ax4.legend([leg8],[label8],loc=4,frameon=True)
plt.gca().add_artist(legend4)
ax4.legend(loc=1,frameon=False)

#ax5.set_xlabel('z')
ax5.set_ylabel(r'$[\gamma_{X} s^{-1} Hz^{-1} baryon^{-1}]$')
ax5.set_yscale('log')
legend5 = ax5.legend([leg9],[label9],loc=4,frameon=True)
plt.gca().add_artist(legend5)
ax5.legend(loc=1,frameon=False)

ax6.axis('off')

#plt.set_title = 'Title'
xticklabels1 = ax1.get_xticklabels()
plt.setp(xticklabels1, visible=False)
xticklabels2 = ax2.get_xticklabels()
plt.setp(xticklabels2, visible=False)
xticklabels4 = ax4.get_xticklabels()
plt.setp(xticklabels4, visible=False)

plt.savefig('/physics2/mscheuch/' + paroutfile + '__plot.eps',bbox_inches='tight')

print '\n**********************************'
print '********** Finished **************'
print '**********************************\n'
