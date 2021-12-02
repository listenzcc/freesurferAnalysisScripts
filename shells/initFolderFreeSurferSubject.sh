#! /bin/sh

for i in $(seq 1 9)
do
    folder=$HOME/nfsHome/freesurfer/subjects/liuyeSubject$i
    echo $folder
    mkdir $folder/mri/orig -p
    ln -s $HOME/nfsHome/liuYeFmriDataAnalysis/analysis-$i/niiFiles/001.mgz $folder/mri/orig/001.mgz
    ls -l $folder/mri --rec
done
