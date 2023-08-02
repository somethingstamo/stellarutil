# Table of Contents
- ArchiveClass Class
    - [_tar_directory](#_tar_directory): Helper function.
    - [clean_directories](#clean_directories): Clean a simulation directory, a list of simulation directories, or a directory of multiple
simulation directories.
Run this after a simulation finishes.
Remove unnecessary run-time files, and tar directories (into a single tar-ball file) that we
generally do not need for post-processing analysis.
    - [delete_snapshots](#delete_snapshots): Delete all snapshots in simulation_directory/snapshot_directory/ that are within
snapshot_index_limits, except for those in snapshot_indices_subset list.
    - [tar_directories](#tar_directories): Use tar to combine simulation sub-directories into single tar-ball files.
Run this on a single simulation directory, a list of simulation directories,
or a directory of multiple simulation directories.
Run this after runing clean_directory(), to reduce the file count for archival/tape storage.
By default, this stores the original sub-directories after tar-ring them, but you can delete
the directories (if you are running this on the archival/tape server directly) by inputing
delete_directories=True.
To delete the tar-balls that this function creates (if you are on live scratch space),
simply input delete_tarballs=True.
- CompressClass Class
    - [_compress_snapshot](#_compress_snapshot): Compress a single snapshot (a single file or a directory with multiple files) named
snapshot_name in snapshot_directory, write to write_directory.
    - [compress_snapshots](#compress_snapshots): Read snapshots in input snapshot_directory, compress them,
write compressed snapshots to snapshot_directory + write_directory_modifier.
    - [init CompressClass](#init-compressclass)
    - [test_compression](#test_compression): Read headers from all snapshot files in simulation_directory + snapshot_directory to check
if files have been compressed.
- GlobusClass Class
    - [submit_transfer](#submit_transfer): Submit transfer of simulation files via Globus command-line utility.
Must initiate from Stampede2.

Install Globus CLI:
    conda install -c conda-forge globus-cli
Create bookmark:
    globus bookmark create '7961b534-3f0e-11e7-bd15-22000b9a448b:/' stampede
        '0c9d7c36-ea22-11e5-97d6-22000b9da45e:/share/wetzellab/' peloton-scratch
        'a90a2f92-c5ca-11e9-9ced-0edb67dd7a14:/fire2/public_release/' flatiron-fire2-public
    - [write_globus_batch_file_peloton](#write_globus_batch_file_peloton): Write a batch file that sets files to transfer via globus.
    - [write_globus_batch_file_public](#write_globus_batch_file_public): Write a batch file that sets files to transfer via globus,
for FIRE-2 public data release at Flatiron.
- RsyncClass Class
    - [init RsyncClass](#init-rsyncclass): .
    - [rsync_simulation_files](#rsync_simulation_files): Use rsync to copy (non-snapshot) files from remote machine to local directory.
Directory can be a single simulation directory or a directory of simulation directories.
    - [rsync_snapshot_files](#rsync_snapshot_files): Use rsync to copy snapshot files from a single simulations directory on a remote machine to
a local simulation directory.

## _tar_directory

### Description:
Helper function.


## clean_directories

### Description:
Clean a simulation directory, a list of simulation directories, or a directory of multiple
simulation directories.
Run this after a simulation finishes.
Remove unnecessary run-time files, and tar directories (into a single tar-ball file) that we
generally do not need for post-processing analysis.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| directories | str or list thereof |     directory[s] to run this on. can be a single simulation directory, a list of simulation<br />    directories, or a directory that contains multiple simulation directories for which this<br />    function will run recursively on each one | required |
| gizmo_directory | str |     directory of Gizmo source code | required |
| snapshot_directory | str |     output directory that contains snapshots | required |
| restart_directory | str |     directory within snapshot_directory that stores restart files | required |
| gizmo_out_file | str |     Gizmo 'out' file | required |
| gizmo_err_file | str |     Gizmo error file | required |
| snapshot_scalefactor_file | str |     file that contains snapshot scale-factors (only) | required |

## delete_snapshots

### Description:
Delete all snapshots in simulation_directory/snapshot_directory/ that are within
snapshot_index_limits, except for those in snapshot_indices_subset list.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| simulation_directory | str |     directory of simulation | required |
| snapshot_directory | str |     directory of snapshot files | required |
| snapshot_index_limits | list |     min and max snapshot indices to delete | required |
| delete_halos | bool |     whether to delete halo catalog files at the same snapshots | required |

## tar_directories

### Description:
Use tar to combine simulation sub-directories into single tar-ball files.
Run this on a single simulation directory, a list of simulation directories,
or a directory of multiple simulation directories.
Run this after runing clean_directory(), to reduce the file count for archival/tape storage.
By default, this stores the original sub-directories after tar-ring them, but you can delete
the directories (if you are running this on the archival/tape server directly) by inputing
delete_directories=True.
To delete the tar-balls that this function creates (if you are on live scratch space),
simply input delete_tarballs=True.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| directories | str or list thereof |     directory[s] to run this on. can be a single simulation directory, a list of simulation<br />    directories, or a directory that contains multiple simulation directories for which this<br />    function will run recursively on each one | required |
| snapshot_directory | str |     output directory that contains snapshot files | required |
| job_directory | str |     directory that contains slurm/pbs job files | required |
| ic_directory | str |     directory that contains initial condition files from MUSIC | required |
| particle_track_directory | str |     directory of particle tracking files | required |
| halo_directory | str |     directory of (all) halo files/directories | required |
| rockstar_directory | str |     directory of (all) Rockstar files/directories | required |
| rockstar_job_directory | str |     directory of Rockstar run-time log/job files | required |
| rockstar_catalog_directory | str |     directory of Rockstar (text) halo catalog + tree files | required |
| rockstar_hdf5_directory | str |     directory of post-processed catalog + tree hdf5 files | required |
| delete_directories | bool |     whether to delete the (raw) directories after tar-ing them into a single file | required |
| delete_tarballs | bool |     whether to delete existing tar-balls<br />    use this safely to clean the tar-balls that this function creates | required |
| proc_number | int |     number of parallel processes for tar-ing halo directories + snapshots | required |

## _compress_snapshot

### Description:
Compress a single snapshot (a single file or a directory with multiple files) named
snapshot_name in snapshot_directory, write to write_directory.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| snapshot_name | str |     name of snapshot (file or directory) | required |
| snapshot_directory | str |     directory to read existing snapshot files | required |
| write_directory | str |     directory to write compressed snapshots<br />    if same as snapshot_directory, over-write existing snapshots | required |

## compress_snapshots

### Description:
Read snapshots in input snapshot_directory, compress them,
write compressed snapshots to snapshot_directory + write_directory_modifier.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| simulation_directory | str |     directory of simulation | required |
| snapshot_directory | str |     directory of snapshots | required |
| write_directory | str |     directory to write compressed snapshots<br />    if same as snapshot_directory or '', over-write existing snapshots | required |
| snapshot_indices | list |     indices of snapshots to compress. If None or 'all', compress all in snapshot_directory. | required |
| proc_number | int |     number of parallel processes to use | required |

## init CompressClass

### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| analysis_directory | str |     directory of manipulate_hdf5 package | required |
| manipulate_hdf5_directory | str |     python executable to use to run compression script | required |

## test_compression

### Description:
Read headers from all snapshot files in simulation_directory + snapshot_directory to check
if files have been compressed.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| simulation_directory | str |     directory of simulation | required |
| snapshot_directory | str |     directory of compressed snapshot files | required |
| snapshot_indices | list |     indices of snapshots to test. If None or 'all', test all in snapshot_directory. | required |
| compression_level | int | None | required |
| verbose | bool | None | required |

## submit_transfer

### Description:
Submit transfer of simulation files via Globus command-line utility.
Must initiate from Stampede2.

Install Globus CLI:
    conda install -c conda-forge globus-cli
Create bookmark:
    globus bookmark create '7961b534-3f0e-11e7-bd15-22000b9a448b:/' stampede
        '0c9d7c36-ea22-11e5-97d6-22000b9da45e:/share/wetzellab/' peloton-scratch
        'a90a2f92-c5ca-11e9-9ced-0edb67dd7a14:/fire2/public_release/' flatiron-fire2-public


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| simulation_path_directory | str |     '.' or full path + directory of simulation | required |
| machine_name | str |     name of machine transfering files to | required |
| batch_file_name | str |     name of batch file to write | required |

## write_globus_batch_file_peloton

### Description:
Write a batch file that sets files to transfer via globus.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| simulation_directory | str |     directory of simulation | required |
| batch_file_name | str |     name of globus batch file in which to write files to transfer | required |
| snapshot_indices | array |     snapshot_indices to transfer | required |

## write_globus_batch_file_public

### Description:
Write a batch file that sets files to transfer via globus,
for FIRE-2 public data release at Flatiron.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| simulation_directory | str |     directory of simulation | required |
| batch_file_name | str |     name of globus batch file in which to write files to transfer | required |
| snapshot_indices | array |     snapshot_indices to transfer | required |

## init RsyncClass

### Description:
.


## rsync_simulation_files

### Description:
Use rsync to copy (non-snapshot) files from remote machine to local directory.
Directory can be a single simulation directory or a directory of simulation directories.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| machine_from | str |     name of (remote) machine to copy from: 'pfe', 'stampede', 'frontera', 'peloton' | required |
| directory_from | str |     directory to copy from | required |
| directory_to | str |     directory to copy files to | required |
| snapshot_index | int |     which snapshot to include | required |

## rsync_snapshot_files

### Description:
Use rsync to copy snapshot files from a single simulations directory on a remote machine to
a local simulation directory.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| machine_from | str |     name of (remote) machine to copy from: 'pfe', 'stampede', 'frontera', 'peloton' | required |
| directory_from | str |     directory to copy from | required |
| directory_to | str |     local directory to put snapshots | required |
| snapshot_indices | int or list |     index[s] of snapshots to transfer | required |
