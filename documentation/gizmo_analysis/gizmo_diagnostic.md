# Table of Contents
 - [plot_scaling](#plot_scaling): Print simulation run times (wall or core).
'speedup' := WT(1 CPU) / WT(N CPU) =
'efficiency' := WT(1 CPU) / WT(N CPU) / N = CT(1 CPU) / CT(N CPU)
 - [print_galaxy_properties](#print_galaxy_properties): Print properties of galaxy at input snapshot.
 - [print_particle_properties_statistics](#print_particle_properties_statistics): For each property of each species in particle catalog, print range and median.
 - [print_particle_property_extrema_across_snapshots](#print_particle_property_extrema_across_snapshots): For each input property, get its extremum at each snapshot.
Print statistics of property across all snapshots.
 - [print_summary](#print_summary): Print the most useful diagnostics.
 - [test_stellar_mass_loss](#test_stellar_mass_loss): .
- ContaminationClass Class
    - [print_plot_contamination_v_distance](#print_plot_contamination_v_distance): Print [and plot] contamination from low-resolution particles v distance from center.
    - [print_plot_contamination_v_distance_both](#print_plot_contamination_v_distance_both): Print [and plot] contamination from low-resolution dark-matter particles around halo/galaxy
as a function of distance.
- RuntimeClass Class
    - [get_cpu_numbers](#get_cpu_numbers): Get number of MPI tasks and OpenMP threads from run-time file.
If cannot find any, default to 1.
    - [get_scalefactor_string](#get_scalefactor_string)
    - [init RuntimeClass](#init-runtimeclass)
    - [print_run_times](#print_run_times): Print wall [and CPU] times (based on average per MPI task from cpu.txt) at scale-factors,
for Gizmo simulation.
    - [print_run_times_ratios](#print_run_times_ratios): Print ratios of wall times and CPU times (based on average per MPI taks from cpu.txt) at
scale-factors, from different simulation directories, for Gizmo simulations.
'reference' simulation is first in list.

## plot_scaling

### Description:
Print simulation run times (wall or core).
'speedup' := WT(1 CPU) / WT(N CPU) =
'efficiency' := WT(1 CPU) / WT(N CPU) / N = CT(1 CPU) / CT(N CPU)


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| scaling_kind | str |     'strong', 'weak' | required |
| time_kind | str |     'node', 'core', 'wall', 'speedup', 'efficiency' | required |
| axis_x_log_scale | bool |     whether to use logarithmic scaling for x axis | required |
| axis_y_log_scale | bool |     whether to use logarithmic scaling for y axis | required |
| file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |
| directory | str |     directory to write figure file | required |

## print_galaxy_properties

### Description:
Print properties of galaxy at input snapshot.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| part | dict |     catalog of particles at snapshot | required |
| species | str |     name of particle species to get properties of | required |
| snapshot_value_kind | str |     snapshot number kind: 'index', 'redshift', 'scalefactor' | required |
| snapshot_value | int or float |     snapshot number kind: 'index', 'redshift', 'scalefactor' | required |
| simulation_directory | str |     directory of simulation | required |
| snapshot_directory | str |     directory of snapshot files within simulation_directory | required |
| track_directory | str |     directory of files for particle pointers, formation coordinates, and host coordinates | required |

## print_particle_properties_statistics

### Description:
For each property of each species in particle catalog, print range and median.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| species | str or list |     name[s] of particle species to print | required |
| snapshot_value_kind | str |     snapshot number kind: 'index', 'redshift', 'scalefactor' | required |
| snapshot_value | int or float |     snapshot number kind: 'index', 'redshift', 'scalefactor' | required |
| simulation_directory | str |     directory of simulation | required |
| snapshot_directory | str |     directory of snapshot files within simulation_directory | required |
| track_directory | str |     directory of files for particle pointers, formation coordinates, and host coordinates | required |

## print_particle_property_extrema_across_snapshots

### Description:
For each input property, get its extremum at each snapshot.
Print statistics of property across all snapshots.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| simulation_directory | str |     directory of simulation | required |
| snapshot_directory | str |     directory of snapshot files | required |
| track_directory | str |     directory of files for particle pointers, formation coordinates, and host coordinates | required |
| property_dict | dict |     keys = species, values are string or list of property[s] | required |
| snapshot_indices | list |     snapshots indices to read | required |

## print_summary

### Description:
Print the most useful diagnostics.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| snapshot_value_kind | str |     snapshot number kind: 'index', 'redshift', 'scalefactor' | required |
| snapshot_value | int or float |     snapshot number kind: 'index', 'redshift', 'scalefactor' | required |
| simulation_directory | str |     directory of simulation | required |
| snapshot_directory | str |     directory of snapshot files within simulation_directory | required |
| track_directory | str |     directory of files for particle pointers, formation coordinates, and host coordinates | required |

## test_stellar_mass_loss

### Description:
.


## print_plot_contamination_v_distance

### Description:
Print [and plot] contamination from low-resolution particles v distance from center.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| part | dict |     catalog of particles at snapshot | required |
| distance_limits | list |     min and max limits for distance from galaxy | required |
| distance_bin_width | float |     width of each distance bin (in units of distance_scaling) | required |
| distance_log_scale | bool |     whether to use log scaling for distance bins | required |
| halo_radius | float |     radius of halo [kpc physical] | required |
| scale_to_halo_radius | bool |     whether to scale distance to halo_radius | required |
| virial_kind | str |     virial overdensity to set halo radius | required |
| center_position | array |     position of galaxy/halo center | required |
| host_index | int |     index of host halo to get position of (if not input center_position) | required |
| axis_y_limits | list |     min and max limits for y axis | required |
| axis_y_log_scale | bool |     whether to use logarithmic scaling for y axis | required |
| verbose | bool |     verbosity flag | required |
| plot_file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |
| directory | str |     directory in which to write figure file | required |
| figure_index | int |     index of figure for matplotlib | required |

## print_plot_contamination_v_distance_both

### Description:
Print [and plot] contamination from low-resolution dark-matter particles around halo/galaxy
as a function of distance.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| snapshot_value_kind | str |     snapshot number kind: 'index', 'redshift', 'scalefactor' | required |
| snapshot_value | int or float |     snapshot number kind: 'index', 'redshift', 'scalefactor' | required |
| simulation_directory | str |     directory of simulation | required |
| snapshot_directory | str |     directory of snapshot files within simulation_directory | required |
| track_directory | str |     directory of files for particle pointers, formation coordinates, and host coordinates | required |
| virial_kind | str |     virial overdensity to set halo radius | required |
| verbose | bool |     verbosity flag | required |
| plot_file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |

## get_cpu_numbers

### Description:
Get number of MPI tasks and OpenMP threads from run-time file.
If cannot find any, default to 1.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| simulation_directory | str |     top-level directory of simulation | required |
| gizmo_out_file_name | str |     name of Gizmo run-time file | required |

## get_scalefactor_string

## init RuntimeClass

## print_run_times

### Description:
Print wall [and CPU] times (based on average per MPI task from cpu.txt) at scale-factors,
for Gizmo simulation.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| simulation_directory | str |     directory of simulation | required |
| snapshot_directory | str |     directory of snapshot files and Gizmo output files | required |
| gizmo_out_file_name | str |     name of Gizmo run-time file | required |
| gizmo_cpu_file_name | str |     name of Gizmo timing file | required |
| core_number | int |     total number of CPU cores (input instead of reading from run-time file) | required |
| wall_time_restart | float |     wall time [sec] of previous run (if restarted from snapshot) | required |
| scalefactors | array-like |     list of scale-factors at which to print run times | required |

## print_run_times_ratios

### Description:
Print ratios of wall times and CPU times (based on average per MPI taks from cpu.txt) at
scale-factors, from different simulation directories, for Gizmo simulations.
'reference' simulation is first in list.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| simulation_directories | str or list |     top-level directory[s] of simulation[s] | required |
| snapshot_directory | str |     directory of snapshot files and Gizmo output files | required |
| gizmo_out_file_name | str |     name of Gizmo run-time file | required |
| wall_times_restart | float or list |     wall time[s] [sec] of previous run[s] (if restart from snapshot) | required |
| scalefactors | array-like |     list of scale-factors at which to print run times | required |
