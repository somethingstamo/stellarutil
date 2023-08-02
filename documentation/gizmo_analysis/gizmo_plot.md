# Table of Contents
 - [compare_resolution](#compare_resolution): .
 - [compare_star_formation_models](#compare_star_formation_models): .
 - [disk_height_double](#disk_height_double)
 - [disk_height_single](#disk_height_single)
 - [explore_galaxy](#explore_galaxy): Print and plot several properties of galaxies in list.
 - [get_galaxy_mass_profiles_v_redshift](#get_galaxy_mass_profiles_v_redshift): Read snapshots and store dictionary of galaxy/halo position, velocity, size, mass at input
scale-factors, for Shea.
 - [plot_density_distribution](#plot_density_distribution): Plot distribution of gas density.
 - [plot_element_v_distance](#plot_element_v_distance): Plot elemental mass or mass fraction for gas or stars v distance (in bin or cumulative).
 - [plot_galaxy_property_v_time](#plot_galaxy_property_v_time): Plot host galaxy property v time_name, using tabulated dictionary of properties of progenitor
across snapshots.
 - [plot_gas_neutral_fraction_v_redshift](#plot_gas_neutral_fraction_v_redshift): .
 - [plot_neighbors_v_distance](#plot_neighbors_v_distance): Plot number of neighbors (spatial correlation) v separation/distance.
 - [plot_property_distribution](#plot_property_distribution): Plot distribution of property.
 - [plot_property_v_distance](#plot_property_v_distance): parts : dict or list
    catalog[s] of particles (can be different simulations or snapshots)
species_name : str
    name of particle species to compute mass from: 'dark', 'star', 'gas', 'baryon', 'total'
property_name : str
    property to get profile of
property_statistic : str
    statistic/type to plot: sum, sum.cum, density, density.cum, vel.circ, sum.fraction,
    sum.cum.fraction, median, average
property_log_scale : bool
    whether to use logarithmic scaling for property bins
weight_property : str
    property to weight each particle by
property_limits : list
    limits to impose on y-axis
distance_limits : list
    min and max distance for binning
distance_bin_width : float
    width of distance bin
distance_log_scale : bool
    whether to use logarithmic scaling for distance bins
dimension_number : int
    number of spatial dimensions for profile. if 1, get profile along minor axis.
    if 2, get profile along 2 major axes
rotation : bool or array
    whether to rotate particles - two options:
    (a) if input array of eigen-vectors, will define rotation axes
    (b) if True, will rotate to align with principal axes stored in species dictionary
other_axis_distance_limits : float
    min and max distances along other axis[s] to keep particles [kpc physical]
center_positions : array or list of arrays
    position of center for each particle catalog
center_velocities : array or list of arrays
    velocity of center for each particle catalog
host_index : int
    index of host halo to get position and/or velocity of (if not input them)
property_select : dict
    (other) properties to select on: names as keys and limits as values
part_indicess : array or list of arrays
    indices of particles from which to select
distance_reference : float
    reference distance at which to draw vertical line
plot_nfw : bool
    whether to overplot NFW profile: density ~ 1 / r
plot_fit : bool
    whether to overplot linear fit
fit_distance_limits : list
    min and max distance for fit
print_values : bool
    whether to print values plotted
get_values : bool
    whether to return values plotted
plot_file_name : str
    whether to write figure to file and its name. True = use default naming convention
plot_directory : str
    directory to write figure file
figure_index : int
    index of figure for matplotlib
 - [plot_property_v_property](#plot_property_v_property): Plot property v property.
 - [plot_velocity_distribution](#plot_velocity_distribution): Plot distribution of velocities.
 - [plot_velocity_v_age](#plot_velocity_v_age): .
 - [print_densities](#print_densities): parts : dict or list
    catalog[s] of particles (can be different simulations or snapshots)
species_names : str or list thereof
    name of particle species to compute densities of: 'dark', 'star', 'gas'
distance_limitss : list of lists
    min and max distances/positions
coordinate_system : str
    which coordinates to get positions in: 'cartesian' (default), 'cylindrical', 'spherical'
center_positions : array or list of arrays
    position of center for each particle catalog
center_velocities : array or list of arrays
    velocity of center for each particle catalog
rotation : bool or array
    whether to rotate particles - two options:
        (a) if input array of eigen-vectors, will define rotation axes
        (b) if True, will rotate to align with principal axes stored in species dictionary
host_index : int
    index of host galaxy/halo to get position, velocity, and/or rotation tensor (if not input)
property_select : dict
    (other) properties to select on: names as keys and limits as values
 - [print_galaxy_mass_v_redshift](#print_galaxy_mass_v_redshift): Print galaxy/halo position, velocity, size, mass over time for Shea.
 - [print_properties_statistics](#print_properties_statistics): For each property of each species in particle catalog, print its range and median.
 - [test_element_to_element_ratio](#test_element_to_element_ratio): Test element-to-element variations in abundance ratios (normalizing out the median ratio)
for metals that FIRE tracks directly.
 - [test_potential_v_distance](#test_potential_v_distance): .
 - [write_galaxy_properties_v_time](#write_galaxy_properties_v_time): Read snapshots and store dictionary of host galaxy properties (such as mass and radius)
at snapshots.
- CompareSimulationsClass Class
    - [_parse_inputs](#_parse_inputs): parts : list
    dictionaries of particles at snapshot
species : str or list
    name[s] of particle species to read and analyze
redshifts : float or list
    - [init CompareSimulationsClass](#init-comparesimulationsclass): Set directories and names of simulations to read.
    - [plot](#plot): Analyze and plot all quantities for all simulations at each redshift.
    - [plot_histories](#plot_histories): Plot histories of star formation and mass.
    - [plot_images](#plot_images): Plot images of each simulation.
    - [plot_properties_v_distance](#plot_properties_v_distance): Plot profiles of various properties, comparing all simulations at each redshift.
    - [plot_properties_v_properties](#plot_properties_v_properties): Plot property v property for each simulation.
    - [print_masses_sizes](#print_masses_sizes): Print masses and sizes of simulations / galaxies.
- DiskClass Class
    - [plot_axis_ratio_v_time](#plot_axis_ratio_v_time): Plot minor / major axis ratio of the disk versus time_name.
Requires that you have read pre-compiled host rotation tensors in host_coordinates.hdf5.
    - [plot_orientation_v_property](#plot_orientation_v_property): Plot orientation angle of the disk versus property_name.
    - [plot_orientation_v_time](#plot_orientation_v_time): Plot orientation angle[s] of the principal axes of the disk (wrt their orientations at
refrence_snapshot_index) versus time_name.
Requires that you have read pre-compiled host rotation tensors in host_coordinates.hdf5.
- ElementAgeTracerClass Class
    - [plot_element_distribution](#plot_element_distribution): Plot distribution of elemental abundance, comparing direct simulation to age-tracer model.
    - [plot_element_v_distance](#plot_element_v_distance): part : dict
    catalog[s] of particles
species_name : str
    name of particle species to compute mass from: 'star', 'gas'
property_name : str
    property to get profile of
property_statistic : str
    statistic/type to plot: 'median', 'average'
property_limits : list
    limits to impose on y-axis
weight_property : str
    property to weight each particle by
distance_limits : list
    min and max distance for binning
distance_bin_width : float
    width of distance bin
distance_log_scale : bool
    whether to use logarithmic scaling for distance bins
dimension_number : int
    number of spatial dimensions for profile. if 1, get profile along minor axis.
    if 2, get profile along 2 major axes
rotation : bool or array
    whether to rotate particles - two options:
    (a) if input array of eigen-vectors, will define rotation axes
    (b) if True, will rotate to align with principal axes stored in species dictionary
other_axis_distance_limits : float
    min and max distances along other axis[s] to keep particles [kpc physical]
part_indices : array
    indices of particles to select
plot_file_name : str
    whether to write figure to file and its name. True = use default naming convention
plot_directory : str
    directory to write figure file
figure_index : int
    index of figure for matplotlib
    - [plot_element_v_element](#plot_element_v_element): Plot elemental abundance v elemental abundance.
    - [plot_element_v_time](#plot_element_v_time): Plot elemental abundance v time.
    - [test_agetracers](#test_agetracers): Test element-to-element variations in abundance ratios (normalizing out the median ratio)
for metals that FIRE tracks directly.
    - [test_agetracers_with_progenitor_metallicity](#test_agetracers_with_progenitor_metallicity): .
    - [test_progenitor_metallicity_dependence](#test_progenitor_metallicity_dependence): .
- HalosClass Class
    - [assign_vel_circ_at_radius](#assign_vel_circ_at_radius): .
    - [plot_density_profile](#plot_density_profile): Plot density profile for single halo/center.
    - [plot_density_profiles](#plot_density_profiles): plot_file_name : str
    whether to write figure to file and its name. True = use default naming convention
plot_directory : str : directory to write figure file
figure_index : int : index of figure for matplotlib
    - [plot_property_v_distance](#plot_property_v_distance): parts : dict or list
    catalog[s] of particles at snapshot
hals : dict or list
    catalog[s] of halos at snapshot
part_indicesss : array (halo catalog number x halo number x particle number)
hal_indicess : array (halo catalog number x halo number)
    indices of halos to plot
gal : dict
    catalog of observed galaxies
gal_indices : array
    indices of galaxies to plot
species_name : str
    name of particle species to compute mass from: 'dark', 'star', 'gas', 'baryon', 'total'
property_name : str
    property to get profile of
property_statistic : str
    statistic/type to plot: sum, sum.cum, density, density.cum, vel.circ, sum.fraction,
    sum.cum.fraction, median, ave
property_log_scale : bool
    whether to use logarithmic scaling for property bins
weight_property : str
    property to weight each particle by
property_limits : list
    limits to impose on y-axis
distance_limits : list
    min and max distance for binning
distance_bin_width : float
    width of distance bin
distance_log_scale : bool
    whether to use logarithmic scaling for distance bins
dimension_number : int
    number of spatial dimensions for profile
distance_reference : float
    reference distance at which to draw vertical line
plot_file_name : str
    whether to write figure to file and its name. True = use default naming convention
plot_directory : str
    directory to write figure file
figure_index : int
    index of figure for matplotlib
    - [plot_vel_circ_v_distance](#plot_vel_circ_v_distance): .
- ISMClass Class
    - [get_positions_sampled](#get_positions_sampled): .
    - [get_velocity_dispersion_v_distance](#get_velocity_dispersion_v_distance): .
    - [plot_velocity_dispersion_v_distance](#plot_velocity_dispersion_v_distance): .
- ImageClass Class
    - [get_histogram](#get_histogram): Get 2-D histogram, either by summing all partiles along 3rd dimension or computing the
highest density along 3rd dimension.
    - [init ImageClass](#init-imageclass): .
    - [plot_image](#plot_image): Plot image of the positions of given partcle species, using either a single panel for
2 dimensions or 3 panels for all axis permutations.
    - [plot_image_simple](#plot_image_simple): Plot image of the positions of given partcle species, using either a single panel for
2 dimensions or 3 panels for all 2-dimensional combinations.
    - [print_values](#print_values): Write 2-D histogram values of image to file.
- MassRadiusClass Class
    - [init MassRadiusClass](#init-massradiusclass): .
    - [plot_age_v_distance](#plot_age_v_distance): Plot average age v radial distance (today and at formation).
    - [plot_massfraction_v_distance](#plot_massfraction_v_distance): Plot average age v radial distance (today and at formation).
    - [plot_radius_v_age](#plot_radius_v_age): Plot average age v radial distance (today and at formation).
- StarFormHistoryClass Class
    - [_get_star_form_history](#_get_star_form_history): Get array of times and star-formation rate at each time.
    - [plot_star_form_history](#plot_star_form_history): Plot star-formation history v time_name.
    - [plot_star_form_history_galaxies](#plot_star_form_history_galaxies): Plot star-formation history v time_name for multiple galaxies in a halo catalog.

## compare_resolution

### Description:
.


## compare_star_formation_models

### Description:
.


## disk_height_double

## disk_height_single

## explore_galaxy

### Description:
Print and plot several properties of galaxies in list.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| hal | dict |     catalog of halos at snapshot | required |
| hal_index | int |     index within halo catalog | required |
| part | dict |     atalog of particles at snapshot | required |
| species_plot | str or dict |     which particle species to plot | required |
| distance_max | float |     max distance (radius) for galaxy image | required |
| distance_bin_width | float |     length of pixel for galaxy image | required |
| distance_bin_number | int |     number of pixels for galaxy image | required |
| plot_only_members | bool |     whether to plat only particles that are members of halo | required |
| plot_file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |
| plot_directory | str |     directory to write figure file | required |

## get_galaxy_mass_profiles_v_redshift

### Description:
Read snapshots and store dictionary of galaxy/halo position, velocity, size, mass at input
scale-factors, for Shea.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| directory | str : directory of snapshot files | None | required |
| redshifts | array-like : redshifts at which to get properties | None | required |
| parts | list : list of particle dictionaries | None | required |

## plot_density_distribution

### Description:
Plot distribution of gas density.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| part | dict |     catalog of particles at snapshot | required |
| species_name | str |     name of particle species | required |
| property_name | str |     property name | required |
| property_limits | list |     min and max limits of property | required |
| property_bin_width | float |     width of property bin (use this or property_bin_number) | required |
| property_log_scale | bool |     whether to use logarithmic scaling for property bins | required |
| property_statistic | str |     statistic to plot: 'probability', 'probability.cum', 'probability.norm', 'histogram',<br />    'histogram.cum' | required |
| weight_property | str or list |     property[s] to weight each particle by | required |
| property_select | dict |     (other) properties to select on: names as keys and limits as values | required |
| part_indicess | array or list of arrays |     indices of particles from which to select | required |
| axis_y_limits | list |     min and max limits for y axis | required |
| axis_y_log_scale | bool |     whether to use logarithmic scaling for y axis | required |
| plot_file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |
| plot_directory | str |     directory to write plot file | required |
| figure_index | int |     index of figure for matplotlib | required |

## plot_element_v_distance

### Description:
Plot elemental mass or mass fraction for gas or stars v distance (in bin or cumulative).


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| part | dict or list |     catalog[s] of particles at snapshot | required |
| species_name | str |     name of particle species | required |
| property_name | str |     'massfraction.<element_name>' or 'mass.<element_name>' | required |
| property_statistic | str |     'sum', 'sum.cum' | required |
| axis_y_log_scale | bool |     whether to use logarithmic scaling for y axis | required |
| distance_limits | list |     min and max limits for distance from galaxy | required |
| distance_bin_width | float |     width of each distance bin (in units of distance_scaling) | required |
| distance_log_scale | bool |     whether to use logarithmic scaling for distance bins | required |
| halo_radius | float |     radius of halo [kpc physical] | required |
| scale_to_halo_radius | bool |     whether to scale distance to halo_radius | required |
| center_positions | array |     position[s] of galaxy center[s] [kpc comoving] | required |
| host_index | int |     index of host halo to get position of (if not input center_positions) | required |
| plot_file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |
| plot_directory | str |     directory to write figure file | required |
| figure_index | int |     index of figure for matplotlib | required |

## plot_galaxy_property_v_time

### Description:
Plot host galaxy property v time_name, using tabulated dictionary of properties of progenitor
across snapshots.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| gals | dict |     tabulated dictionary of host galaxy properties | required |
| sfhs | dict |     tabulated dictinnary of star-formation histories (computed at single snapshot) | required |
| property_name | str |     name of star formation history property to plot:<br />        'rate', 'rate.specific', 'mass', 'mass.normalized' | required |
| time_name | str |     time kind to use: 'time', 'time.lookback', 'redshift' | required |
| time_limits | list |     min and max limits of time_name to get | required |
| time_log_scale | bool |     whether to use logarithmic scaling for time bins | required |
| snapshot_subsample_factor | int |     factor by which to sub-sample snapshots from gals | required |
| axis_y_limits | list |     min and max limits for y axis | required |
| axis_y_log_scale | bool |     whether to use logarithmic scaling for y axis | required |
| plot_file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |
| plot_directory | str |     directory to write figure file | required |
| figure_index | int |     index of figure for matplotlib | required |

## plot_gas_neutral_fraction_v_redshift

### Description:
.


## plot_neighbors_v_distance

### Description:
Plot number of neighbors (spatial correlation) v separation/distance.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| parts | dict or list |     catalog of particles at snapshot | required |
| species_name | str |     name of particle species | required |
| distance_limits | list |     min and max limits for particle neighbor separation distances to measure | required |
| distance_bin_width | float |     width of separation distance bin | required |
| distance_log_scale | bool |     whether to use logarithmic scaling for separation distance bins | required |
| neig_number_max | int |     maximum number of neighbors to find per particle | required |
| dimension_number | int |     number of spatial dimensions to use | required |
| host_index | int |     index of host galaxy/halo to get position and/or velocity of (if not input them) | required |
| property_select | dict |     (other) properties to select on: names as keys and limits as values | required |
| property_statistic | str |     statistic to plot: 'probability', 'probability.cum', 'histogram', 'histogram.cum',<br />    'density.norm' | required |
| axis_y_limits | list |     min and max limits for y axis | required |
| axis_y_log_scale | bool |     whether to use logarithmic scaling for y axis | required |
| plot_file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |
| plot_directory | str |     directory to write figure file | required |
| figure_index | int |     index of figure for matplotlib | required |

## plot_property_distribution

### Description:
Plot distribution of property.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| part | dict |     catalog of particles at snapshot | required |
| species_name | str |     name of particle species | required |
| property_name | str |     property name | required |
| property_limits | list |     min and max limits of property | required |
| property_bin_width | float |     width of property bin (use this or property_bin_number) | required |
| property_bin_number | int |     number of bins within limits (use this or property_bin_width) | required |
| property_log_scale | bool |     whether to use logarithmic scaling for property bins | required |
| property_statistic | str |     statistic to plot: 'probability', 'probability.cum', 'probability.norm', 'histogram',<br />    'histogram.cum' | required |
| weight_property | str |     property to weight each particle by | required |
| distance_limits | list |     min and max limits for distance from galaxy | required |
| center_positions | array or list of arrays |     position[s] of galaxy center[s] | required |
| center_velocities | array or list of arrays |     velocity[s] of galaxy center[s] | required |
| host_index | int |     index of host halo to get position and velocity of (if not input) | required |
| property_select | dict |     (other) properties to select on: names as keys and limits as values | required |
| part_indicess | array or list of arrays |     indices of particles from which to select | required |
| axis_y_limits | list |     min and max limits for y axis | required |
| axis_y_log_scale | bool |     whether to use logarithmic scaling for y axis | required |
| plot_file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |
| plot_directory | str |     directory to write plot file | required |
| figure_index | int |     index of figure for matplotlib | required |

## plot_property_v_distance

### Description:
parts : dict or list
    catalog[s] of particles (can be different simulations or snapshots)
species_name : str
    name of particle species to compute mass from: 'dark', 'star', 'gas', 'baryon', 'total'
property_name : str
    property to get profile of
property_statistic : str
    statistic/type to plot: sum, sum.cum, density, density.cum, vel.circ, sum.fraction,
    sum.cum.fraction, median, average
property_log_scale : bool
    whether to use logarithmic scaling for property bins
weight_property : str
    property to weight each particle by
property_limits : list
    limits to impose on y-axis
distance_limits : list
    min and max distance for binning
distance_bin_width : float
    width of distance bin
distance_log_scale : bool
    whether to use logarithmic scaling for distance bins
dimension_number : int
    number of spatial dimensions for profile. if 1, get profile along minor axis.
    if 2, get profile along 2 major axes
rotation : bool or array
    whether to rotate particles - two options:
    (a) if input array of eigen-vectors, will define rotation axes
    (b) if True, will rotate to align with principal axes stored in species dictionary
other_axis_distance_limits : float
    min and max distances along other axis[s] to keep particles [kpc physical]
center_positions : array or list of arrays
    position of center for each particle catalog
center_velocities : array or list of arrays
    velocity of center for each particle catalog
host_index : int
    index of host halo to get position and/or velocity of (if not input them)
property_select : dict
    (other) properties to select on: names as keys and limits as values
part_indicess : array or list of arrays
    indices of particles from which to select
distance_reference : float
    reference distance at which to draw vertical line
plot_nfw : bool
    whether to overplot NFW profile: density ~ 1 / r
plot_fit : bool
    whether to overplot linear fit
fit_distance_limits : list
    min and max distance for fit
print_values : bool
    whether to print values plotted
get_values : bool
    whether to return values plotted
plot_file_name : str
    whether to write figure to file and its name. True = use default naming convention
plot_directory : str
    directory to write figure file
figure_index : int
    index of figure for matplotlib


## plot_property_v_property

### Description:
Plot property v property.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| part | dict |     catalog of particles at snapshot | required |
| species_name | str |     name of particle species | required |
| x_property_name | str |     property name for x-axis | required |
| x_property_limits | list |     min and max limits to impose on x_property_name | required |
| x_property_log_scale | bool |     whether to use logarithmic scaling for x axis | required |
| y_property_name | str |     property name for y-axis | required |
| y_property_limits | list |     min and max limits to impose on y_property_name | required |
| y_property_log_scale | bool |     whether to use logarithmic scaling for y axis | required |
| property_bin_number | int |     number of bins for histogram along each axis | required |
| weight_property | str |     property to weight each particle by | required |
| host_distance_limits | list |     min and max limits for distance from galaxy | required |
| center_position | array |     position of galaxy center | required |
| host_index | int |     index of host galaxy/halo to get position of (if not input) | required |
| property_select | dict |     (other) properties to select on: names as keys and limits as values | required |
| part_indices | array |     indices of particles from which to select | required |
| draw_statistics | bool |     whether to draw statistics (such as median) on figure | required |
| plot_file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |
| plot_directory | str |     directory to write figure file | required |
| add_simulation_name | bool |     whether to add name of simulation to figure name | required |
| figure_index | int |     index of figure for matplotlib | required |

## plot_velocity_distribution

### Description:
Plot distribution of velocities.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| part | dict |     catalog of particles at snapshot | required |
| species_name | str |     name of particle species | required |
| property_name | str |     property name | required |
| property_limits | list |     min and max limits of property | required |
| property_bin_width | float |     width of property bin (use this or property_bin_number) | required |
| property_bin_number | int |     number of bins within limits (use this or property_bin_width) | required |
| property_log_scale | bool |     whether to use logarithmic scaling for property bins | required |
| property_statistic | str : |     statistic to plot: 'probability', 'probability.cum', 'histogram', 'histogram.cum' | required |
| distance_limits | list |     min and max limits for distance from galaxy | required |
| center_positions | array or list of arrays |     position[s] of galaxy center[s] | required |
| center_velocities | array or list of arrays |     velocity[s] of galaxy center[s] | required |
| host_index | int |     index of host galaxy/halo to get position and/or velocity of (if not input them) | required |
| property_select | dict |     (other) properties to select on: names as keys and limits as values | required |
| part_indicess | array or list of arrays |     indices of particles from which to select | required |
| axis_y_limits | list |     min and max limits for y axis | required |
| axis_y_log_scale | bool |     whether to use logarithmic scaling for y axis | required |
| plot_file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |
| plot_directory | str |     directory to write figure file | required |
| figure_index | int |     index of figure for matplotlib | required |

## plot_velocity_v_age

### Description:
.


## print_densities

### Description:
parts : dict or list
    catalog[s] of particles (can be different simulations or snapshots)
species_names : str or list thereof
    name of particle species to compute densities of: 'dark', 'star', 'gas'
distance_limitss : list of lists
    min and max distances/positions
coordinate_system : str
    which coordinates to get positions in: 'cartesian' (default), 'cylindrical', 'spherical'
center_positions : array or list of arrays
    position of center for each particle catalog
center_velocities : array or list of arrays
    velocity of center for each particle catalog
rotation : bool or array
    whether to rotate particles - two options:
        (a) if input array of eigen-vectors, will define rotation axes
        (b) if True, will rotate to align with principal axes stored in species dictionary
host_index : int
    index of host galaxy/halo to get position, velocity, and/or rotation tensor (if not input)
property_select : dict
    (other) properties to select on: names as keys and limits as values


## print_galaxy_mass_v_redshift

### Description:
Print galaxy/halo position, velocity, size, mass over time for Shea.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| gal | dict |     dictionary of galaxy properties across snapshots | required |

## print_properties_statistics

### Description:
For each property of each species in particle catalog, print its range and median.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| part | dict |     catalog of particles (use this instead of reading in) | required |
| species | str or list |     name[s] of particle species to print | required |

## test_element_to_element_ratio

### Description:
Test element-to-element variations in abundance ratios (normalizing out the median ratio)
for metals that FIRE tracks directly.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| parts | dict or list |     catalog[s] of particles at snapshot | required |
| species_name | str or list |     name[s] of particle species | required |
| element_reference | str |     name of element to use as reference, to get scatter of other elements relative to it | required |
| log_ratio | bool |     whether to compute the log ratio of elemental abundances | required |

## test_potential_v_distance

### Description:
.


## write_galaxy_properties_v_time

### Description:
Read snapshots and store dictionary of host galaxy properties (such as mass and radius)
at snapshots.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| simulation_directory | str |     root directory of simulation | required |
| redshifts | array-like |     redshifts at which to get properties<br />        'all' = read and store all snapshots | required |
| species | str or list |     name[s] of species to read and get properties of | required |

## _parse_inputs

### Description:
parts : list
    dictionaries of particles at snapshot
species : str or list
    name[s] of particle species to read and analyze
redshifts : float or list


## init CompareSimulationsClass

### Description:
Set directories and names of simulations to read.


## plot

### Description:
Analyze and plot all quantities for all simulations at each redshift.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| parts | list |     dictionaries of particles at snapshot | required |
| species | str or list |     name[s] of particle species to read and analyze | required |
| simulation_directories | list |     simulation directories and names/labels for figure | required |
| redshifts | float or list | None | required |

## plot_histories

### Description:
Plot histories of star formation and mass.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| parts | list |     dictionaries of particles at snapshot | required |

## plot_images

### Description:
Plot images of each simulation.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| parts | list |     dictionaries of particles at snapshot | required |
| distance_max | float |     maximum distance from center to plot | required |
| distance_bin_width | float |     distance bin width (pixel size) | required |
| align_principal_axes | bool |     whether to align plot axes with principal axes | required |

## plot_properties_v_distance

### Description:
Plot profiles of various properties, comparing all simulations at each redshift.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| parts | list |     dictionaries of particles at snapshot | required |
| distance_bin_width | float |     width of distance bin | required |
| plot_abundances | bool |     whether to plot elemental abundances | required |

## plot_properties_v_properties

### Description:
Plot property v property for each simulation.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| parts | list |     dictionaries of particles at snapshot | required |
| property_bin_number | int |     number of bins along each dimension for histogram | required |

## print_masses_sizes

### Description:
Print masses and sizes of simulations / galaxies.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| parts | list of dicts |     catalogs of particles at snapshot | required |
| species | str or list |     name[s] of particle species to read and analyze | required |
| distance_max | float |     maximum distance from center to plot | required |
| mass_fraction | float |     mass fraction (within distance_max) to determine edge of galaxy | required |

## plot_axis_ratio_v_time

### Description:
Plot minor / major axis ratio of the disk versus time_name.
Requires that you have read pre-compiled host rotation tensors in host_coordinates.hdf5.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| parts | dict or list |     catalog[s] of particles (can be different simulations or snapshots) | required |
| time_name | str |     time kind to plot: 'time', 'time.lookback', 'age', 'redshift', 'scalefactor' | required |
| time_limits | list |     min and max limits of time_name to impose | required |
| time_width | float |     width of time_name bin | required |
| time_log_scale | bool |     whether to use logarithmic scaling for time bins | required |
| axis_index_numerator | int |     which principal axix to use in numerator of ratio<br />    0 = minor, 1 = intermediate, 2 = major | required |
| axis_index_denominator | int |     which principal axix to use in denominator of ratio | required |
| host_index | int |     index of host galaxy/halo to get stored position of (if not input it) | required |
| plot_file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |
| plot_directory | str |     directory to write figure file | required |
| figure_index | int |     index of figure for matplotlib | required |

## plot_orientation_v_property

### Description:
Plot orientation angle of the disk versus property_name.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| parts | dict or list |     catalog[s] of particles (can be different simulations or snapshots) | required |
| species_names | str or list |     name[s] of particle species to compute: 'star', 'gas', 'dark' | required |
| property_name | str |     which property to vary (along x-axis): 'distance', 'age' | required |
| property_limits | list |     min and max property for binning | required |
| property_bin_width | float |     width of property bin | required |
| property_log_scale | bool |     whether to use logarithmic scaling for property | required |
| reference_distance_max | float |     reference distance to compute principal axes | required |
| center_positions | array or list of arrays |     position of center for each particle catalog | required |
| center_velocities | array or list of arrays |     velocity of center for each particle catalog | required |
| host_index | int |     index of host galaxy/halo to get stored position of (if not input it) | required |
| plot_file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |
| plot_directory | str |     directory to write figure file | required |
| figure_index | int |     index of figure for matplotlib | required |

## plot_orientation_v_time

### Description:
Plot orientation angle[s] of the principal axes of the disk (wrt their orientations at
refrence_snapshot_index) versus time_name.
Requires that you have read pre-compiled host rotation tensors in host_coordinates.hdf5.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| parts | dict or list |     catalog[s] of particles (can be different simulations or snapshots) | required |
| time_name | str |     time kind to plot: 'time', 'time.lookback', 'age', 'redshift', 'scalefactor' | required |
| time_limits | list |     min and max limits of time_name to impose | required |
| time_width | float |     width of time_name bin | required |
| time_log_scale | bool |     whether to use logarithmic scaling for time bins | required |
| refrence_snapshot_index | int |     index of reference snapshot, that defines angle zero point | required |
| axis_indices | list |     which principal axes to plot the orientation angles of<br />    0 = minor, 1 = intermediate, 2 = major | required |
| host_index | int |     index of host galaxy/halo to get stored position of (if not input it) | required |
| plot_file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |
| plot_directory | str |     directory to write figure file | required |
| figure_index | int |     index of figure for matplotlib | required |

## plot_element_distribution

### Description:
Plot distribution of elemental abundance, comparing direct simulation to age-tracer model.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| part | dict |     catalog of particles at snapshot | required |
| species_name | str |     name of particle species | required |
| property_name | str |      name of element | required |
| property_limits | list |     min and max limits of element | required |
| property_bin_width | float |     width of element bin | required |
| property_statistic | str |     statistic to plot: 'probability', 'probability.cum', 'probability.norm', 'histogram',<br />    'histogram.cum' | required |
| axis_y_limits | list |     min and max limits for y axis | required |
| axis_y_log_scale | bool |     whether to use logarithmic scaling for y axis | required |
| weight_property | str |     property to weight each particle by | required |
| part_indices | array |     indices of particles from which to select | required |
| verbose | bool |     verbosity flag | required |
| plot_file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |
| plot_directory | str |     directory to write plot file | required |
| figure_index | int |     index of figure for matplotlib | required |

## plot_element_v_distance

### Description:
part : dict
    catalog[s] of particles
species_name : str
    name of particle species to compute mass from: 'star', 'gas'
property_name : str
    property to get profile of
property_statistic : str
    statistic/type to plot: 'median', 'average'
property_limits : list
    limits to impose on y-axis
weight_property : str
    property to weight each particle by
distance_limits : list
    min and max distance for binning
distance_bin_width : float
    width of distance bin
distance_log_scale : bool
    whether to use logarithmic scaling for distance bins
dimension_number : int
    number of spatial dimensions for profile. if 1, get profile along minor axis.
    if 2, get profile along 2 major axes
rotation : bool or array
    whether to rotate particles - two options:
    (a) if input array of eigen-vectors, will define rotation axes
    (b) if True, will rotate to align with principal axes stored in species dictionary
other_axis_distance_limits : float
    min and max distances along other axis[s] to keep particles [kpc physical]
part_indices : array
    indices of particles to select
plot_file_name : str
    whether to write figure to file and its name. True = use default naming convention
plot_directory : str
    directory to write figure file
figure_index : int
    index of figure for matplotlib


## plot_element_v_element

### Description:
Plot elemental abundance v elemental abundance.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| part | dict |     catalog of particles at snapshot | required |
| species_name | str |     name of particle species | required |
| x_property_name | str |     name of element on x-axis | required |
| x_property_limits | list |     min and max limits to impose | required |
| x_property_width | float |     width of x-axis bin | required |
| y_property_name | str |     name of element[s] on y-axis | required |
| y_property_limits | list |     min and max limits to impose | required |
| weight_property | str |     property by which to weight each particle | required |
| part_indices | array |     indices of particles from which to select | required |
| plot_file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |
| plot_directory | str |     directory to write figure file | required |
| figure_index | int |     index of figure for matplotlib | required |

## plot_element_v_time

### Description:
Plot elemental abundance v time.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| part | dict |     catalog of particles at snapshot | required |
| time_name | str |     name of time property: 'age', 'time', 'redshift' | required |
| time_limits | list |     min and max limits on time property | required |
| time_width | float |     width of time bin | required |
| property_name | str |     name of element[s] on y-axis | required |
| property_limits | list |     min and max limits on property_name | required |
| weight_property | str |     property by which to weight each particle | required |
| part_indices | array |     indices of particles from which to select | required |
| plot_file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |
| plot_directory | str |     directory to write figure file | required |
| figure_index | int |     index of figure for matplotlib | required |

## test_agetracers

### Description:
Test element-to-element variations in abundance ratios (normalizing out the median ratio)
for metals that FIRE tracks directly.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| part | dict |     catalog of particles at snapshot | required |
| species_name | str or list |     name of particle species | required |
| weight_property | str |     property to weight each abundance by. If None, do not weight. | required |
| pindices | array |     prior indices of particles to select | required |

## test_agetracers_with_progenitor_metallicity

### Description:
.


## test_progenitor_metallicity_dependence

### Description:
.


## assign_vel_circ_at_radius

### Description:
.


## plot_density_profile

### Description:
Plot density profile for single halo/center.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| part | dict |     catalog of particles at snapshot | required |
| species_name | str |     name of particle species to plot | required |
| hal | dict |     catalog of halos at snapshot | required |
| hal_index | int |     index of halo in catalog | required |
| center_position | array |     position to center profile (to use instead of halo position) | required |
| distance_max | float |     max distance (radius) for galaxy image | required |
| distance_bin_width | float |     length of pixel for galaxy image | required |
| plot_file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |
| plot_directory | str |     directory to write figure file | required |
| figure_index | int |     index of figure for matplotlib | required |

## plot_density_profiles

### Description:
plot_file_name : str
    whether to write figure to file and its name. True = use default naming convention
plot_directory : str : directory to write figure file
figure_index : int : index of figure for matplotlib


## plot_property_v_distance

### Description:
parts : dict or list
    catalog[s] of particles at snapshot
hals : dict or list
    catalog[s] of halos at snapshot
part_indicesss : array (halo catalog number x halo number x particle number)
hal_indicess : array (halo catalog number x halo number)
    indices of halos to plot
gal : dict
    catalog of observed galaxies
gal_indices : array
    indices of galaxies to plot
species_name : str
    name of particle species to compute mass from: 'dark', 'star', 'gas', 'baryon', 'total'
property_name : str
    property to get profile of
property_statistic : str
    statistic/type to plot: sum, sum.cum, density, density.cum, vel.circ, sum.fraction,
    sum.cum.fraction, median, ave
property_log_scale : bool
    whether to use logarithmic scaling for property bins
weight_property : str
    property to weight each particle by
property_limits : list
    limits to impose on y-axis
distance_limits : list
    min and max distance for binning
distance_bin_width : float
    width of distance bin
distance_log_scale : bool
    whether to use logarithmic scaling for distance bins
dimension_number : int
    number of spatial dimensions for profile
distance_reference : float
    reference distance at which to draw vertical line
plot_file_name : str
    whether to write figure to file and its name. True = use default naming convention
plot_directory : str
    directory to write figure file
figure_index : int
    index of figure for matplotlib


## plot_vel_circ_v_distance

### Description:
.


## get_positions_sampled

### Description:
.


## get_velocity_dispersion_v_distance

### Description:
.


## plot_velocity_dispersion_v_distance

### Description:
.


## get_histogram

### Description:
Get 2-D histogram, either by summing all partiles along 3rd dimension or computing the
highest density along 3rd dimension.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| image_kind | str |     'histogram', 'histogram.3d' | required |
| dimension_list | list |     indices of dimensions to plot<br />    if length 2, plot one v other, if length 3, plot all via 3 panels | required |
| position_bin_number | int |     number of pixels/bins across image | required |
| position_limits | list or list of lists |     min and max values of position to compute | required |
| positions | array |     3-D positions | required |
| weights | array |     weight for each position | required |
| use_column_units | bool |     whether to convert to [number / cm^2] | required |

## init ImageClass

### Description:
.


## plot_image

### Description:
Plot image of the positions of given partcle species, using either a single panel for
2 dimensions or 3 panels for all axis permutations.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| part | dict |     catalog of particles at snapshot | required |
| species_name | str |     name of particle species to plot | required |
| weight_name | str |     property to weight positions by | required |
| image_kind | str |     'histogram', 'histogram.3d', 'points' | required |
| dimensions_plot | list |     dimensions to plot - if length 2, plot one v one; if length 3, plot all via 3 panels | required |
| dimensions_select | list |     dimensions to use to select particles<br />    use this to set selection 'depth' of an image | required |
| distances_max | float or array |     distance[s] from center to plot and/or cut [kpc] | required |
| distance_bin_width | float |     size of pixel [kpc] | required |
| distance_bin_number | int |     number of pixels from distance = 0 to max (2x this across image) | required |
| center_position | array-like |     position of center | required |
| rotation | bool or array |     whether to rotate particles - two options:<br />    (a) if input array of eigen-vectors, will define rotation axes<br />    (b) if True, will rotate to align with principal axes defined by input species | required |
| host_index | int |     index of host halo to get position and rotation of (if not input them) | required |
| property_select | dict |     (other) properties to select on: names as keys and limits as values | required |
| part_indices | array |     input selection indices for particles | required |
| subsample_factor | int |     factor by which periodically to sub-sample particles | required |
| use_column_units | bool |     whether to convert to particle number / cm^2 | required |
| image_limits | list |     min and max limits to impose on image dynamic range (exposure) | required |
| background_color | str |     name of color for background: 'white', 'black' | required |
| hal | dict |     catalog of halos at snapshot | required |
| hal_indices | array |     indices of halos to plot | required |
| hal_position_kind | str |     name of position to use for center of halo | required |
| hal_radius_kind | str |     name of radius to use for size of halo | required |
| plot_file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |
| plot_directory | str |     path + directory where to write file<br />    if ends in '.pdf', override default file naming convention and use input name | required |
| figure_index | int |     index of figure for matplotlib | required |

## plot_image_simple

### Description:
Plot image of the positions of given partcle species, using either a single panel for
2 dimensions or 3 panels for all 2-dimensional combinations.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| part | dict |     catalog of particles at snapshot | required |
| species_name | str |     name of particle species to plot | required |
| weight_name | str |     property to weight positions by | required |
| dimensions_plot | list |     dimensions to plot - if length 2, plot one v one; if length 3, plot all via 3 panels | required |
| distance_max | float or array |     distance from center to plot [kpc] | required |
| distance_bin_width | float |     size of pixel [kpc] | required |
| rotation | bool or array |     whether to rotate particles<br />    if True, will rotate to align with principal axes defined by input species | required |
| host_index | int |     index of host halo to get position and rotation of (if not input them) | required |
| part_indices | array |     input selection indices for particles | required |
| image_limits | list |     min and max limits to impose on image dynamic range (exposure) | required |
| plot_file | bool |     whether to write figure to file and its name | required |

## print_values

### Description:
Write 2-D histogram values of image to file.


## init MassRadiusClass

### Description:
.


## plot_age_v_distance

### Description:
Plot average age v radial distance (today and at formation).


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| parts | dict or list |     catalog[s] of particles | required |
| species_names | str or list |     name[s] of particle species to compute: 'star', 'gas', 'dark' | required |
| property_name | str |     which property to vary (along x-axis): 'distance', 'age' | required |
| property_limits | list |     min and max property for binning | required |
| property_bin_width | float |     width of property bin | required |
| property_log_scale | bool |     whether to use logarithmic scaling for property | required |
| host_index | int |     index of host galaxy/halo to get stored position of (if not input it) | required |
| plot_file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |
| plot_directory | str |     directory to write figure file | required |
| figure_index | int |     index of figure for matplotlib | required |

## plot_massfraction_v_distance

### Description:
Plot average age v radial distance (today and at formation).


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| parts | dict or list |     catalog[s] of particles | required |
| property_name | str |     which property to vary (along x-axis): 'distance', 'age' | required |
| property_limits | list |     min and max property for binning | required |
| property_bin_width | float |     width of property bin | required |
| property_log_scale | bool |     whether to use logarithmic scaling for property | required |
| host_index | int |     index of host galaxy/halo to get stored position of (if not input it) | required |
| plot_file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |
| plot_directory | str |     directory to write figure file | required |
| figure_index | int |     index of figure for matplotlib | required |

## plot_radius_v_age

### Description:
Plot average age v radial distance (today and at formation).


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| parts | dict or list |     catalog[s] of particles | required |
| property_name | str |     which property to vary (along x-axis): 'distance', 'age' | required |
| property_limits | list |     min and max property for binning | required |
| property_bin_width | float |     width of property bin | required |
| property_log_scale | bool |     whether to use logarithmic scaling for property | required |
| host_index | int |     index of host galaxy/halo to get stored position of (if not input it) | required |
| plot_file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |
| plot_directory | str |     directory to write figure file | required |
| figure_index | int |     index of figure for matplotlib | required |

## _get_star_form_history

### Description:
Get array of times and star-formation rate at each time.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| part | dict |     catalog of particles | required |
| time_name | str |     time metric to use: 'time', 'time.lookback', 'age', 'redshift', 'scalefactor' | required |
| time_limits | list |     min and max limits of time_name to impose | required |
| time_width | float |     width of time_name bin (in units set by time_scaling) | required |
| time_log_scale | bool |     whether to use logarithmic scaling for time bins | required |
| distance_limits | list |     min and max limits of galaxy distance to select star particles | required |
| center_position | list |     position of galaxy centers [kpc comoving] | required |
| host_index | int |     index of host galaxy/halo to get position of (if not input it) | required |
| property_select | dict |     dictionary with property names as keys and limits as values | required |
| part_indices | array |     indices of star particles to select | required |

## plot_star_form_history

### Description:
Plot star-formation history v time_name.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| parts | dict or list |     catalog[s] of particles | required |
| sfh_name | str |     star form kind to plot: 'form.rate', 'form.rate.specific', 'mass', 'mass.normalized' | required |
| time_name | str |     time kind to use: 'time', 'time.lookback', 'age', 'redshift', 'scalefactor' | required |
| time_limits | list |     min and max limits of time_name to impose | required |
| time_width | float |     width of time_name bin | required |
| time_log_scale | bool |     whether to use logarithmic scaling for time bins | required |
| distance_limits | list |     min and max limits of distance to select star particles | required |
| center_positions | list or list of lists |     position[s] of galaxy centers [kpc comoving] | required |
| host_index | int |     index of host galaxy/halo to get position of (if not input center_position) | required |
| property_select | dict |     properties to select on: names as keys and limits as values | required |
| part_indicess | array |     indices of particles from which to select | required |
| sfh_limits | list |     min and max limits for y-axis | required |
| sfh_log_scale | bool |     whether to use logarithmic scaling for SFH bins | required |
| plot_file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |
| plot_directory | str |     directory to write figure file | required |
| figure_index | int |     index of figure for matplotlib | required |

## plot_star_form_history_galaxies

### Description:
Plot star-formation history v time_name for multiple galaxies in a halo catalog.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| part | dict |     catalog of particles | required |
| hal | dict |     catalog of halos at snapshot | required |
| gal | dict |     catalog of galaxies in the Local Group with SFHs | required |
| mass_name | str |     mass kind by which to select halos | required |
| mass_limits | list |     min and max limits to impose on mass_name | required |
| property_select | dict |     properties to select on: names as keys and limits as values | required |
| hal_indices | index or array |     index[s] of halo[s] whose particles to plot | required |
| sfh_name | str |     star form kind to plot: 'rate', 'rate.specific', 'mass', 'mass.normalized' | required |
| sfh_limits | list |     min and max limits for y axis | required |
| sfh_log_scale | bool |     whether to use logarithmic scaling for y axis | required |
| time_name | str |     time kind to plot: 'time', 'time.lookback', 'age', 'redshift' | required |
| time_limits | list |     min and max limits of time_name to plot | required |
| time_width | float |     width of time_name bin | required |
| time_log_scale | bool |     whether to use logarithmic scaling for time bins | required |
| plot_file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |
| plot_directory | str |     directory to write figure file | required |
| figure_index | int |     index of figure for matplotlib | required |
