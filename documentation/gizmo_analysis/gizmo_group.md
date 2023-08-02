# Table of Contents
 - [plot_number_v_distance](#plot_number_v_distance): Plot number (cumulative or differential) of groups v host distance.
 - [plot_number_v_mass](#plot_number_v_mass): Plot number (cumulative or differential) of groups v mass_name.
 - [plot_property_v_distance](#plot_property_v_distance): Plot property v distance, in bins of mass_name.
 - [plot_property_v_property](#plot_property_v_property): Plot property v property.
 - [print_properties](#print_properties): Print useful properties of groups[s].
- GroupDictionaryClass Class
    - [get_indices](#get_indices): Get indices of groups that satisfy input selection limits.
    - [init GroupDictionaryClass](#init-groupdictionaryclass)
    - [prop](#prop): Get property, either from self dictionary or derive.
If several properties, need to provide mathematical relationship.
- IOClass Class
    - [_generate_write_group_catalog](#_generate_write_group_catalog): Utility function.
    - [_get_group_file_names_and_indices](#_get_group_file_names_and_indices): Get name[s] and snapshot index[s] of group catalog file[s].
    - [_io_group_catalog](#_io_group_catalog): Read/write a catalog of groups at a snapshot to/from HDF5 file.
If reading, return as dictionary.
    - [generate_group_catalog](#generate_group_catalog): Generate and get dictionary catalog of FoF groups of particles of input species.
    - [generate_write_group_catalogs](#generate_write_group_catalogs): Read particles from snapshot[s], generate FoF group catalog of particle species
write FoF group catalog to HDF5 file.
By default, set up to run from within the base directory of a simulation.
    - [init IOClass](#init-ioclass): .
    - [read_group_catalogs](#read_group_catalogs): Read catalog[s] of groups at snapshot[s].
Return as dictionary or list of dictionaries.

## plot_number_v_distance

### Description:
Plot number (cumulative or differential) of groups v host distance.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| grps | dict or list |     catalog[s] of groups at a snapshot | required |
| mass_name | str |     group mass kind to plot | required |
| mass_limitss | list or list of lists |     min and max limits of mass_name | required |
| distance_limits | list |     min and max distance from host [kpc physical] | required |
| distance_bin_width | float |     width of distance bin | required |
| distance_log_scale | bool |     whether to use logarithmic scaling for distance bins | required |
| grp_indicess | array or list of arrays |     prior indices of groups | required |
| number_kind | str |      number kind to plot: 'sum', 'sum.cum', 'fraction', 'fraction.cum', 'density' | required |
| number_limits | list |     min and max limits to impose on y-axis | required |
| number_log_scale | bool |     whether to use logarithmic scaling for y axis | required |
| plot_file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |
| plot_directory | str |     directory in which to write figure file | required |
| figure_index | int |     index of figure for matplotlib | required |

## plot_number_v_mass

### Description:
Plot number (cumulative or differential) of groups v mass_name.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| grps | dict or list |     catalog[s] of groups at a snapshot | required |
| mass_name | str or list |     mass kind[s] to plot | required |
| mass_limits | list |     min and max limits for mass_name | required |
| mass_width | float |     width of mass_name bin | required |
| mass_log_scale | bool |     whether to use logarithmic scaling for mass_name bins | required |
| host_distance_limitss | list or list of lists |     min and max limits of distance to host [kpc physical] | required |
| grp_indicess | array or list of arrays |     group indices to plot | required |
| number_kind | str |     mass function kind to plot: 'number',  'number.dif', 'number.cum' | required |
| number_limits | list |     min and max limits to impose on y-axis | required |
| number_log_scale | bool |     whether to use logarithmic scaling for y axis | required |
| include_above_limits | bool |     whether to include mass_name values above limits for cumulative | required |
| plot_file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |
| plot_directory | str |     directory in which to write figure file | required |
| figure_index | int |     index of figure for matplotlib | required |

## plot_property_v_distance

### Description:
Plot property v distance, in bins of mass_name.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| grps | dict or list |     catalog[s] of groups at snapshot | required |
| mass_name | str |     mass kind to plot | required |
| mass_limitss | list or list of lists |     min and max limits of group mass | required |
| distance_limits | list |     min and max distance from host [kpc physical] | required |
| distance_bin_width | float |     width of distance bin | required |
| distance_log_scale | bool |     whether to use logarithmic scaling for distance bins | required |
| property_name | str |     name of property to plot | required |
| statistic | str |     statistic of property to plot | required |
| property_limits | list |     min and max limits to impose on y-axis | required |
| property_log_scale | bool |     whether to use logarithmic scaling for y axis | required |
| grp_indicess | array or list of arrays |     prior indices of groups to include | required |
| plot_file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |
| plot_directory | str |     directory in which to write figure file | required |
| figure_index | int |     index of figure for matplotlib | required |

## plot_property_v_property

### Description:
Plot property v property.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| grps | dict |     catalog[s] of groups at snapshot | required |
| x_property_name | str |     name of property for x-axis | required |
| x_property_limits | list |     min and max limits to impose on x_property_name | required |
| x_property_log_scale | bool |     whether to use logarithmic scaling for x axis | required |
| y_property_name | str |     name of property for y-axis | required |
| y_property_limits | list |     min and max limits to impose on y_property_name | required |
| y_property_log_scale | bool |     whether to use logarithmic scaling for y axis | required |
| host_distance_limitss | list |     min and max limits for distance from galaxy | required |
| grp_indicess | array or list of arrays |     prior indices of groups to select | required |
| plot_kind | str |     what kind of plot to make (can include multiple): 'point', 'histogram', 'statistic' | required |
| histogram_bin_number | int |     number of bins along each axis (if histogram) | required |
| statistic_bin_width | float |     width of x_property_name bin for computing statistics | required |
| plot_file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |
| plot_directory | str |     directory in which to write figure file | required |
| figure_index | int |     ndex of figure for matplotlib | required |

## print_properties

### Description:
Print useful properties of groups[s].


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| grp | dict |     catalog of groups | required |
| grp_indices | int or array |     index[s] of groups[s] | required |
| properties | str or list |     name[s] of properties to print | required |
| digits | int |     number of digits after period | required |

## get_indices

### Description:
Get indices of groups that satisfy input selection limits.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| particle_number_min | int |     minimum number of member particles | required |
| mass_limits | list |     min and max limits for total mass [M_sun] | required |
| density_limits | list |     min and max limits for average mass density within R_50 [M_sun / kpc^3] | required |
| host_distance_limits | list |     min and max limits for distance to host [kpc physical] | required |
| object_kind | str |     [unused placeholder for now] | required |
| prior_indices | array |     prior indices of groups to impose | required |

## init GroupDictionaryClass

## prop

### Description:
Get property, either from self dictionary or derive.
If several properties, need to provide mathematical relationship.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| property_name | str |     name of property | required |
| indices | array |     list of indices to select on (of arbitrary dimensions) | required |
| _dict_only | bool |     require property_name to be in self's dict - avoids endless recursion | required |

## _generate_write_group_catalog

### Description:
Utility function.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| species_name | str |     name of particle species to generate groups of | required |
| linking_length | float |     FoF linking length [pc physical] | required |
| particle_number_min | int |     minimum number of member particles to keep a group | required |
| property_select | dict |     properties to select particles on: names as keys and limits as values | required |
| snapshot_index | int |     index of snapshot | required |
| simulation_directory | string |     base directory of simulation | required |
| group_directory | str |     directory (within a simulation_directory) of group catalog files | required |
| verbose | bool |     whether to print each property read/written | required |

## _get_group_file_names_and_indices

### Description:
Get name[s] and snapshot index[s] of group catalog file[s].


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| species_name | str |     name of particle species: 'gas', 'star', 'dark' | required |
| linking_length | float |     FoF linking length [pc physical] | required |
| simulation_and_group_directory | string |     directory (including path of base simulation_directory) of group catalog files | required |
| snapshot_indices | int or array thereof |     index of snapshot[s] | required |

## _io_group_catalog

### Description:
Read/write a catalog of groups at a snapshot to/from HDF5 file.
If reading, return as dictionary.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| species_name | str |     name of particle species: 'gas', 'star', 'dark' | required |
| snapshot_index | int |     index of snapshot | required |
| linking_length | float |     FoF linking length [pc physical] | required |
| grp | dictionary |     catalog of groups at a snapshot, if writing | required |
| simulation_directory | string |     base directory of simulation | required |
| group_directory | str |     directory (within a simulation_directory) of group catalog files | required |
| verbose | bool |     whether to print each property read/written | required |

## generate_group_catalog

### Description:
Generate and get dictionary catalog of FoF groups of particles of input species.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| part | dict |     catalog of particles at snapshot | required |
| species_name | str |     name of particle species to use | required |
| property_select | dict |     properties to select particles on: names as keys and limits as values | required |
| part_indices | array |     prior indices[s] of particles to select | required |
| linking_length | float |     maximum distance to link neighbors [pc physical] | required |
| particle_number_min | int |     minimum number of member particles to keep a group | required |
| dimension_number | 3 |     number of spatial dimensions to use (to run in 2-D) | required |
| host_index | int |     index of host galaxy to use to get positions and velocities around | required |

## generate_write_group_catalogs

### Description:
Read particles from snapshot[s], generate FoF group catalog of particle species
write FoF group catalog to HDF5 file.
By default, set up to run from within the base directory of a simulation.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| species_name | str |     name of particle species to generate groups of | required |
| linking_length | float |     FoF linking length [pc physical] | required |
| particle_number_min | int |     minimum number of member particles to keep a group | required |
| property_select | dict |     properties to select particles on: names as keys and limits as values | required |
| snapshot_value_kind | str |     snapshot number kind: 'index', 'redshift', 'scalefactor' | required |
| snapshot_values | int or float or list thereof |     index[s] or redshifts[s] or scale-factor[s] of snapshot file[s] | required |
| simulation_directory | string |     base directory of simulation | required |
| group_directory | str |     directory (within a simulation_directory) of group catalog files | required |
| proc_number | int |     number of parallel processes to run | required |
| verbose | bool |     whether to print each property read/written | required |

## init IOClass

### Description:
.


## read_group_catalogs

### Description:
Read catalog[s] of groups at snapshot[s].
Return as dictionary or list of dictionaries.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| species_name | str |     name of particle species of group catalog: 'gas', 'star', 'dark' | required |
| linking_length | float |     FoF linking length [pc physical] | required |
| snapshot_value_kind | string |     snapshot value kind: 'index', 'redshift', 'scalefactor' | required |
| snapshot_values | int or float or list thereof |     index[s] or redshifts[s] or scale-factor[s] of snapshot file[s]<br />    if 'all' or None, read all snapshots with group catalogs | required |
| simulation_directory | string |     base directory of simulation | required |
| group_directory | string |     directory  of group catalog files | required |
| host_number | int |     number of hosts to assign and compute coordinates relative to<br />    if 0 or None, skip host assignment | required |
| all_snapshot_list | bool |     if reading multiple snapshots, whether to create a list of group catalogs of length<br />    equal to all snapshots in simulation (so group catalog index = snapsht index) | required |
| simulation_name | string |     name of simulation to store for future identification | required |
