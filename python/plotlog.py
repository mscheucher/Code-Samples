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

################## Path and Files Definition ####################
impath = '/physics2/mscheuch/iosim/'
impath2 = '*/'
file = 'Time*'
logx = 1
logy = 1
xlimmin = 0.6
xlimmax = 1.8
ylimmin = 0.6   #std: automatic
ylimmax = 1.8   #std: automatic
################## File Definition ##############################
def file_def(nodes, ppn, nfiles, nranks, nwriters, nitems, width, iperf):
    "++++++ USERDEF ++++++"
    x = nfiles      #nodes ppn nfiles nranks nwriters nitems width iperf
    return x;
def outfile_def():
    "++++++ USERDEF ++++++"
    paroutfile = 'Times_%s' %'nfiles01'
    return paroutfile;
################## File Selection criteria ######################
def par_select(file_nodes, file_ppn, file_nfiles, file_nranks, file_nwriters, file_nitems, file_width, file_iperf):
    "++++++ USERDEF ++++++"
    parameter = file_nitems*file_width     #[file_nodes file_ppn file_nfiles file_nranks file_nwriters file_nitems file_width file_iperf]
    return parameter;
"++++++ USERDEF ++++++"
parval = 3000000000
################## Plot Definitions ##################################
def title(parval):
    "++++++ USERDEF ++++++"
    #title = ''
    title = 'nitems= %.0e' %parval
    return title;
def xlabel_def():
    "++++++ USERDEF ++++++"
    #str = 'items / file'
    str = 'nfiles'
    return str;
#################################################################

print '\n**********************************'
print '***** Start: plotlog.py *********'
print '**********************************\n'

colors = ['black', 'red', 'blue', 'green', 'brown', 'orange', 'cyan', 'magenta', 'violet', 'limegreen', 'royalblue', 'yellowgreen', 'plum', 'yellow']
lines = ['-','--',':','-.']

plt.ioff()
fig = plt.subplots(3,1, figsize=(5,15))
#plt.subplots_adjust(bottom=0.15, top=0.15)#, hspace=0.001)
ax1 = plt.subplot(311)
ax2 = plt.subplot(312)#, sharex=ax1)
ax3 = plt.subplot(313)#, sharex=ax1)
#ax4 = plt.subplot(322)
#ax5 = plt.subplot(324, sharex=ax4)
#ax6 = plt.subplot(326, sharex=ax4)

######### Defining vectors #########
nodes = []
ppn = []
nfiles = []
nranks = []
nwriters = []
nitems = []
width = []
iperf = []
aveTcreate = []
aveTopen = []
aveTwrite = []
aveTread = []
aveTclose = []
x = []
fsize = []
######### Reading in files #########
i=0
ndir=0
for directory in glob.glob(impath+impath2):
    nel=0
    for filename in glob.glob(directory+impath2+file):
        items = re.split('_files|_ranks|_writers|_items|_of_width|_nod|_proc|/|-',filename)
        print filename
        file_nodes = int(items[4])
        file_ppn = int(items[5])
        file_nfiles = int(items[-5])
        file_nranks = int(items[-4])
        file_nwriters = int(items[-3])
        file_nitems = int(items[-2])
        file_width = int(items[-1])
        file_iperf = file_nitems*file_width/file_nfiles
        #['', 'physics2', 'mscheuch', 'iosim', '1', '64',
        #'Test', '10000', '64', '64', '1000000000', '3',
        #'Timelog', '10000', '64', '64', '1000000000', '3']
        parameter = par_select(file_nodes, file_ppn, file_nfiles, file_nranks, file_nwriters, file_nitems, file_width, file_iperf)
        if (parameter !=  parval):
            continue
        
        nodes.append(1)
        ppn.append(1)
        nfiles.append(1)
        nranks.append(1)
        nwriters.append(1)
        nitems.append(1)
        width.append(1)
        iperf.append(1)
        aveTcreate.append(1)
        aveTopen.append(1)
        aveTwrite.append(1)
        aveTread.append(1)
        aveTclose.append(1)
        fsize.append(1)

        nodes[i] = int(items[4])
        ppn[i] = int(items[5])
        nfiles[i] = int(items[-5])
        nranks[i] = int(items[-4])
        nwriters[i] = int(items[-3])
        nitems[i] = int(items[-2])
        width[i] = int(items[-1])
        iperf[i] = nitems[i]*width[i]/nfiles[i]
        fsize[i] = math.pow(math.log10(iperf[i]),4)/50
        print 'markersize = %s' %fsize[i]
    
        data = np.genfromtxt(filename, unpack=True)
        Task = data[0][1:]
        Tcreate = data[1][1:]
        Topen = data[2][1:]
        Twrite = data[3][1:]
        Tread = data[4][1:]
        Tclose = data[5][1:]

        aveTcreate[i] = np.mean(Tcreate)
        aveTopen[i] = np.mean(Topen)
        aveTwrite[i] = np.mean(Twrite)
        aveTread[i] = np.mean(Tread)
        aveTclose[i] = np.mean(Tclose)

        print 'nodes %s' %nodes[i]
        print 'ppn %s' %ppn[i]
        print 'nfiles %.0e' %float(nfiles[i])
        print 'nranks %s' %nranks[i]
        print 'nwriters %s' %nwriters[i]
        print 'nitems %.0e' %float(nitems[i])
        print 'width %s' %width[i]
        print 'i/f %.0e' %float(iperf[i])

        print 'aveTcreate %s' %aveTcreate[i]
        print 'aveTopen %s' %aveTopen[i]
        print 'aveTwrite %s' %aveTwrite[i]
        print 'aveTread %s' %aveTread[i]
        print 'aveTclose %s' %aveTclose[i]

        nel=nel+1
        i=i+1
        
    ndir=ndir+1
print '++++++++ files read in ++++++++'
print 'nel=%s' %nel
print 'ndir=%s' %ndir

#goto .end

x = file_def(nodes, ppn, nfiles, nranks, nwriters, nitems, width, iperf)
paroutfile = outfile_def()

for j in range(ndir):
    ax1.scatter(x[0+(j*nel):(nel)+(j*nel)], aveTcreate[0+(j*nel):(nel)+(j*nel)],
             marker='o', alpha=0.8, s=fsize[0+(j*nel):(nel)+(j*nel)],
             label='nodes:ppn %s:%s, nranks %s, nwriters %s'%(nodes[0+(j*nel)],ppn[0+(j*nel)],nranks[0+(j*nel)],nwriters[0+(j*nel)]),
             color=colors[j], edgecolor=colors[0], linewidth='0.1')
    ax2.scatter(x[0+(j*nel):(nel)+(j*nel)], aveTwrite[0+(j*nel):(nel)+(j*nel)],
             marker='o', alpha=0.8, s=fsize[0+(j*nel):(nel)+(j*nel)],
             label='nodes:ppn %s:%s, nranks %s, nwriters %s'%(nodes[0+(j*nel)],ppn[0+(j*nel)],nranks[0+(j*nel)],nwriters[0+(j*nel)]),
             color=colors[j], edgecolor=colors[0], linewidth='0.1')
    ax3.scatter(x[0+(j*nel):(nel)+(j*nel)], aveTclose[0+(j*nel):(nel)+(j*nel)],
             marker='o', alpha=0.8, s=fsize[0+(j*nel):(nel)+(j*nel)],
             label='nodes:ppn %s:%s, nranks %s, nwriters %s'%(nodes[0+(j*nel)],ppn[0+(j*nel)],nranks[0+(j*nel)],nwriters[0+(j*nel)]),
             color=colors[j], edgecolor=colors[0], linewidth='0.1')

#    if (j==1):
#        break


ymin1 = np.min(aveTcreate)*ylimmin
ymax1 = np.max(aveTcreate)*ylimmax
ymin2 = np.min(aveTwrite)*ylimmin
ymax2 = np.max(aveTwrite)*ylimmax
ymin3 = np.min(aveTclose)*ylimmin
ymax3 = np.max(aveTclose)*ylimmax
xmin1 = np.min(x)*xlimmin
xmax1 = np.max(x)*xlimmax
xmin2 = np.min(x)*xlimmin
xmax2 = np.max(x)*xlimmax
xmin3 = np.min(x)*xlimmin
xmax3 = np.max(x)*xlimmax

ax1.set_xlabel(xlabel_def())
ax1.set_ylabel(r'$T_{create}$ [s]')
#ax1.set_xscale('log')
#ax1.set_yscale('log')
ax1.set_ylim([ymin1,ymax1])
ax1.set_xlim([xmin1,xmax1])
ax1.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

ax2.set_xlabel(xlabel_def())
ax2.set_ylabel(r'$T_{write}$ [s]')
#ax2.set_xscale('log')
#ax2.set_yscale('log')
ax2.set_ylim([ymin2,ymax2])
ax2.set_xlim([xmin2,xmax2])
ax2.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

ax3.set_xlabel(xlabel_def())
ax3.set_ylabel(r'$T_{close}$ [s]')
#ax3.set_xscale('log')
#ax3.set_yscale('log')
ax3.set_ylim([ymin3,ymax3])
ax3.set_xlim([xmin3,xmax3])
ax3.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#ax3.grid(True)

if (logx == 1):
    ax1.set_xscale('log')
    ax2.set_xscale('log')
    ax3.set_xscale('log')
if (logy == 1):
    ax1.set_yscale('log')
    ax2.set_yscale('log')
    ax3.set_yscale('log')

ax1.set_title(title(parval))
#xticklabels1 = ax1.get_xticklabels()
#plt.setp(xticklabels1, visible=False)
#xticklabels2 = ax2.get_xticklabels()
#plt.setp(xticklabels2, visible=False)

outfile = impath + paroutfile + '__plot.pdf'
plt.savefig(outfile, bbox_inches='tight')

print '\n**********************************'
print 'output: %s' %outfile
print '\n**********************************'
print '********** Finished **************'
print '**********************************\n'
