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

######## Path and Files Definition ################################
#impath = '../Boxes/zetaX1.0e+55/'
impath = '../Output_files/Plot_files/'
files = ['*','Tb*','Ts*','XH*','fcol*']
logx = 0
logy = 0
###################################################################


print '\n**********************************'
print '***** Start: plotoverz.py *********'
print '**********************************\n'

colors = ['black','blue','red','green']
lines = ['-','--',':','-.']

######### Reading in files #########
for filename in glob.glob(impath + files[0]):
    data = np.loadtxt(filename, unpack=True)
    print 'Reading in file: %s' %filename
    presplit = re.split('/',filename)
    items = re.split('_',presplit[-1])
    z = data[0][:]
    y = data[1][:]
    var = str(items[0])
    dim = str(items[3])
    box = str(items[4])

    #break
    #### End reading in file #########

#sys.exit("Program interrupted by user")

    ######### Preparing plot #########
    plt.figure()
    ax = plt.gca()
    ax.plot(z, y, marker='.',linestyle=lines[0],label=var,color=colors[1],linewidth=2)
    ax.set_aspect(1./ax.get_data_ratio())

    ax.set_xlabel('z')
    ax.set_ylabel(var)
    if (logx):
        ax.set_xscale('log')
    if (logy):
        ax.set_yscale('log')
    #ax.set_xlim([0,1000])

    #ax.legend(loc=1,frameon=False)
    ax.set_title('%s over z. DIM=$%s^{3}$, Box=$%s^{3}$' %(var, dim, box))

    #xticklabels = ax.get_xticklabels()
    #plt.setp(xticklabels, visible=False)
    #yticklabels = ax.get_yticklabels()
    #plt.setp(yticklabels, visible=False)
    outfile = filename + '__plot.eps'
    print 'Plotting: %s' %outfile
    plt.savefig(outfile, bbox_inches='tight')
    plt.close

print '\n**********************************'
print '********** Finished **************'
print '**********************************\n'
