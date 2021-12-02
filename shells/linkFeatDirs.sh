#! /bin/sh
# Soft link featdir to the featdirs,
# the subject is provided on $1,
# and the dir is the .feat folders under the subject's dir


featName=$1

echo Working with feat dir of $featName

mkdir ./featdirs/$featName

for folder in `ls -d ~/nfsHome/liuYeFmriDataAnalysis/$featName/niiFiles/*.feat`
do
    ln -s $folder ./featdirs/$featName -v
done
