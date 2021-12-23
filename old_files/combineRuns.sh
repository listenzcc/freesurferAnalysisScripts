#!/bin/bash

# The scripts will combine the subjects' all runs

count=1

for folder in `ls ./featdirs/analysis-2/*.feat -d`
do
    folders[$count]=$folder
    ((count++))
done

echo ${folders[1]} ${folders[2]} ${folders[3]}

# mris_preproc --out liuyeSubject2-lh.mgz --target fsaverage --hemi lh --mean \
#     --iv featdirs/analysis-2/5-task1_IPCAS2021012_FuXiaolan_20210929103715_5.feat/stats/zstat1.nii.gz

mris_preproc --out liuyeSubject2-lh.mgz --target fsaverage --hemi lh --mean \
    --iv ${folders[1]}/stats/zstat1.nii.gz ${folders[1]}/reg/freesurfer/anat2exf.register.dat \
    --iv ${folders[2]}/stats/zstat1.nii.gz ${folders[2]}/reg/freesurfer/anat2exf.register.dat \
    --iv ${folders[3]}/stats/zstat1.nii.gz ${folders[3]}/reg/freesurfer/anat2exf.register.dat \
