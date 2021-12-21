#! /bin/sh
# Register the feat,
# the featdir ($1) and freesurfer subject ($2) is required,
# the stats in the featdir is registered into freesurfer subject.

featdir=$1
subject=$2

echo Working with featdir: $featdir, subject: $subject

reg-feat2anat --feat $featdir --subject $subject

feat2surf --feat $featdir

echo Done