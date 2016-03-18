#!/usr/bin/env python2.7

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
impath = '../Boxes/'
#impath = '../Boxes/zetaX5.0e+55/'
#files = 'delta_T*'
#files = 'updated_smoothed*'
files = 'fcol_*'
###################################################################


print '\n**********************************'
print '***** Start: plotboxes.py *********'
print '**********************************\n'

for filename in glob.glob(impath+files):
    plt.figure()
    ax = plt.gca()
    outfile = filename + '__plot.eps'
    data=np.fromfile(filename, dtype=np.float32)
    print 'Reading in file: %s' %filename
    items = re.split('_z0|_zetaX|_nf|_use|_avefcol|_',filename)
    print items
    if (files[0]=='u'):
        z = items[3]
        dim = int(items[4])
        print 'z= ' + str(items[3])
        print 'dim= ' + str(items[4])
        ax.set_title('$\Delta$ plot for z= ' + str(z))
    if (files[0]=='d'):
        z = items[4]
        nf = items[5]
        zetaX = items[7]
        dim = int(items[12])
        print 'z= ' + str(items[4])
        print 'nf= ' + str(items[5])
        print 'zetaX= ' + str(items[7])
        print 'dim= ' + str(items[12])
        ax.set_title('$\Delta$T plot for z= ' + str(z))
    if (files[0]=='f'):
        z = items[1]
        fcol = items[2]
        dim = int(items[8])
        print 'z= ' + str(items[1])
        print '<fcol>= ' + str(items[2])
        print 'dim= ' + str(items[8])
        ax.set_title('$f_{col}$ plot for z=%s and <fcol>=%s' % (z, fcol) )
    #print type(data)
    #print 'Array dimension reads: ' + str(data.shape)
    #print 'Array DTYPE:' + str(data.dtype)
    #dim = data.shape[0] ** (1/3.0)
    #print 'Dimension conversion to %d' %dim
    #dim = int(dim+1)
    #print 'Conversion to integer: %d' %dim
    data = data.reshape([dim, dim, dim])
    print 'Converted array dimension: ' + str(data.shape)
    mid = int(dim/2)
    slice = data[:,mid,:]
    
    im = ax.imshow(slice, origin='lower',cmap=cm.gnuplot2) #,cmap=cm.gist_rainbow,extent=(0, dim, 0, dim))
    divider = make_axes_locatable(ax)
    cax1 = divider.append_axes("bottom", size="5%", pad=0.05)
    cbar = plt.colorbar(im, cax = cax1, orientation='horizontal') #, orientation='horizontal',fraction=0.047, pad=0.02
    #cbar.add_lines(CF)
    #plt.axis('off')
    xticklabels = ax.get_xticklabels()
    plt.setp(xticklabels, visible=False)
    yticklabels = ax.get_yticklabels()
    plt.setp(yticklabels, visible=False)

    plt.savefig(outfile,bbox_inches='tight')
    print 'plot saved as: %s' %outfile
    #break

plt.close
print '\n**********************************'
print '********** Finished **************'
print '**********************************\n'
