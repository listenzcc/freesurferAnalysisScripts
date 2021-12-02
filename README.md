# FreeSurfer Analysis Trace

The project records the analysis trace for the `FreeSurfer` analysis.

---

## Prepare Data

The `T1 MRI Image` is required to make the cortex surfer.
The first step is fit the data into the format of `FreeSurfer`.

1. To do that, it is required to make the private `subject` folder in the `$FreeSurfer_HOME/Subjects` dir;
2. And generate the structure as `{subject}/mri/orig`;
3. Put the `T1 Image` into it, and name it like `001.mgz`,
   the script of [./shells/initFolderFreeSurferSubject.sh](./shells/initFolderFreeSurferSubject.sh) is generated to do the stuff;
4. The `.mgz` file is converted from `.nii` format by the shell tools named as `mri_convert`;
    ```sh
    # Convert the T1 MRI image <src> into <dst> file
    # The <src> file can be .nii file
    # Make sure the <dst> ends with .mgz
    mri_convert <src> <dst>
    ```
5. Finally, just operate the magic command `recon-all -s {subject} -all` and the jobs will be done;
6. Beware that the operation costs times, like **hours**;
7. After the operation, the `{subject}` folder will be filled with the files ready for everything.

If everything is alright,
The `{subject}` folder will follow the structure as below

| name | path                 | description |
| ---- | -------------------- | ----------- |
|      | ./scripts            |             |
|      | ./mri                |             |
|      | ./mri/transforms     |             |
|      | ./mri/transforms/bak |             |
|      | ./mri/orig           |             |
|      | ./surf               |             |
|      | ./tmp                |             |
|      | ./label              |             |
|      | ./touch              |             |
|      | ./stats              |             |
|      | ./trash              |             |

I will fill the blank table in later, (maybe not).

---

## Cortex visualization

The `freeview` tool provides amazing GUI to display the cortex surface.

---

## FSL portable

If you prefer using the `FSL` to do the fMRI analysis,
it provides the registration method to register the `feat` into cortex surface.

I use 2-steps operation to do the job

1. Link the directory of feat of `FSL`,
   use the script of [./shells/linkFeatDirs.sh](./shells/linkFeatDirs.sh);

2. Register the .nii.gz files in the feat directory to the subject of `FreeSurfer`,
   use the script of [./shells/registerFeatdir.sh](./shells/registerFeatdir.sh).
