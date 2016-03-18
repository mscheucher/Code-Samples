#!/bin/sh -f

#  21cmFASTrun.sh
#  
#
#  Created by Markus Scheucher on 08/02/16.
#

#PBS -N IO-SIMULATOR
#PBS -o stdout_file
#PBS -e stderr_file
#PBS -j oe
#PBS -l walltime=23:59:00
#PBS -q bigmem
#   #PBS -l mem=512mb
#PBS -l nodes=1:ppn=64

cd $PBS_O_WORKDIR

##########################################
#                                        #
#   Output some useful job information.  #
#                                        #
##########################################

echo ------------------------------------------------------
echo -n 'Job is running on node '; cat $PBS_NODEFILE
echo ------------------------------------------------------
echo PBS: qsub is running on $PBS_O_HOST
echo PBS: originating queue is $PBS_O_QUEUE
echo PBS: executing queue is $PBS_QUEUE
echo PBS: working directory is $PBS_O_WORKDIR
echo PBS: execution mode is $PBS_ENVIRONMENT
echo PBS: job identifier is $PBS_JOBID
echo PBS: job name is $PBS_JOBNAME
echo PBS: node file is $PBS_NODEFILE
echo PBS: current home directory is $PBS_O_HOME
echo PBS: PATH = $PBS_O_PATH
echo ------------------------------------------------------
echo ' '
echo ' '

############################################################
#                                                          #
#    Execute the run.  Do not run in the background.       #
#                                                          #
############################################################


mpiexec ./iosim -N 81 -n 64 -s 1620 -m create TestFile-81-64-1620

exit
#
#
#