# Table of Contents
 - [test_particle_pointers](#test_particle_pointers): .
- ParticleCoordinateClass Class
    - [_generate_write_hosts_coordinates_at_snapshot](#_generate_write_hosts_coordinates_at_snapshot): Compute the coordinates and principal axes of each host at snapshot_index.
Also compute the 3-D distance and 3-D velocity wrt each primary host galaxy (rotated into
its principle axes) for each particle at snapshot_index and write to file.
    - [generate_write_hosts_coordinates](#generate_write_hosts_coordinates): Select member particles in each host galaxy at the reference snapshot (usually z = 0).
Tracking back only these particles, compute the coordinates and principal axes of each host
at each previous snapshot.
Also compute the 3-D distance and 3-D velocity wrt each primary host galaxy (rotated into
its principle axes) for each particle and write to file.
Work backwards in time and over-write existing values, so for each particle keep only its
coordinates at the first snapshot after it formed.
    - [init ParticleCoordinateClass](#init-particlecoordinateclass)
    - [io_hosts_coordinates](#io_hosts_coordinates): For each host, read or write its position, velocity, and principal axes at each snapshot,
computed by tracking back only member particles at the reference snapshot (z = 0).
If formation_coordinates is True, for each particle, read or write its 3-D distance and
3-D velocity wrt each host galaxy at the first snapshot after it formed,
aligned with (rotated into) the principal axes of each host at that time.
If reading, assign to input dictionary of particles (or halos).
- ParticlePointerClass Class
    - [_generate_write_pointers_to_snapshot](#_generate_write_pointers_to_snapshot): Assign to each particle a pointer from its index at the reference (later, z0) snapshot
to its index (and species name) at a (earlier, z) snapshot.
Write the particle pointers to file.
    - [generate_write_pointers](#generate_write_pointers): Assign to each particle a pointer from its index at the reference (later) snapshot
to its index (and species name) at all other (earlier) snapshots.
Write particle pointers to file, one file for each snapshot besides the reference snapshot.
    - [init ParticlePointerClass](#init-particlepointerclass)
    - [io_pointers](#io_pointers): Read or write, for each star particle at the reference (later, z0) snapshot
its pointer index (and species name) to the other (earlier, z) snapshot.
If input particle catalog (part), append pointers as dictionary class to part,
else return pointers as a dictionary class.
    - [read_pointers_between_snapshots](#read_pointers_between_snapshots): Get particle pointer indices for single species between any two snapshots.
Given input snapshot indices, get array of pointer indices from snapshot_index_from to
snapshot_index_to.
- ParticlePointerDictionaryClass Class
    - [add_intermediate_pointers](#add_intermediate_pointers): Add pointers between an intermediate snapshot (zi) and the earlier snapshot (z),
to allow tracking between these 2 snapshots at z > 0.
The intermediate snapshot (zi) must be between the reference (z0) snapshot and the earlier
(z) snapshot.
    - [assign_forward_pointers](#assign_forward_pointers): Assign pointer indices going forward in time, from the earlier (z) snapshot to the
reference (later) snapshot.
Currently, if gas cell split, assigns only one split gas cell as a descendant.
TODO: deal with gas cells splitting
    - [get_pointers](#get_pointers): Get pointer indices (and species) from species_name_from particles at the
reference (later) snapshot to species_names_to particles the earlier snapshot.
If enable forward, get pointers going forward in time (from z to z_ref) instead.
    - [init ParticlePointerDictionaryClass](#init-particlepointerdictionaryclass): Given input particle catalogs, store summary info about snapshots and particle counts.

## test_particle_pointers

### Description:
.


## _generate_write_hosts_coordinates_at_snapshot

### Description:
Compute the coordinates and principal axes of each host at snapshot_index.
Also compute the 3-D distance and 3-D velocity wrt each primary host galaxy (rotated into
its principle axes) for each particle at snapshot_index and write to file.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| part_z0 | dict |     catalog of particles at the reference (latest) snapshot | required |
| hosts_part_z0_indices | list of arrays |     indices of particles near each primary host at the reference (latest) snapshot | required |
| host_number | int |     number of host galaxies to assign and compute coordinates relative to | required |
| snapshot_index | int |     snapshot index at which to assign particle pointers to | required |
| count_tot | dict |     diagnostic counters | required |

## generate_write_hosts_coordinates

### Description:
Select member particles in each host galaxy at the reference snapshot (usually z = 0).
Tracking back only these particles, compute the coordinates and principal axes of each host
at each previous snapshot.
Also compute the 3-D distance and 3-D velocity wrt each primary host galaxy (rotated into
its principle axes) for each particle and write to file.
Work backwards in time and over-write existing values, so for each particle keep only its
coordinates at the first snapshot after it formed.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| part | dict |     catalog of particles at the reference snapshot | required |
| host_number | int |     number of host galaxies to assign and compute coordinates relative to | required |
| reference_snapshot_index | int or str |     index of reference (final) snapshot (generally z = 0)<br />    if 'final', use final snapshot in snapshot_times.txt | required |
| proc_number | int |     number of parallel processes to run | required |
| simulation_directory | str |     base directory of simulation | required |

## init ParticleCoordinateClass

### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| species | str |     name of particle species to track | required |
| simulation_directory | str |     directory of simulation | required |
| track_directory | str |     directory of files for particle pointers and formation coordinates | required |
| snapshot_directory | str |     directory of snapshot files (within simulation directory) | required |
| host_distance_limits | list |     min and max distance [kpc physical] to select particles near each primary host at the<br />    reference snapshot (usually z = 0).<br />    Use only these particles to compute host coordinates at earlier snapshots. | required |
| host_edge_percent | float |     percent of species mass (within initial aperture) to define host galaxy radius + height | required |

## io_hosts_coordinates

### Description:
For each host, read or write its position, velocity, and principal axes at each snapshot,
computed by tracking back only member particles at the reference snapshot (z = 0).
If formation_coordinates is True, for each particle, read or write its 3-D distance and
3-D velocity wrt each host galaxy at the first snapshot after it formed,
aligned with (rotated into) the principal axes of each host at that time.
If reading, assign to input dictionary of particles (or halos).


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| part | dict |     catalog of particles at a snapshot<br />    (or catalog of halos at a snapshot or catalog of halo merger trees across snapshots) | required |
| simulation_directory | str |     directory of simulation | required |
| track_directory | str |     directory of files for particle pointers and formation coordinates | required |
| assign_formation_coordinates | bool |     whether to read and assign the formation coordinates for each particle | required |
| write | bool |     whether to write to file (instead of read) | required |
| verbose | bool |     whether to print diagnostic information | required |

## _generate_write_pointers_to_snapshot

### Description:
Assign to each particle a pointer from its index at the reference (later, z0) snapshot
to its index (and species name) at a (earlier, z) snapshot.
Write the particle pointers to file.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| part_z0 | dict |     catalog of particles at the reference (later, z0) snapshot | required |
| snapshot_index | int |     snapshot index to assign pointers to at the (earlier, z) snapshot | required |
| count | dict |     total diagnostic counters across all snapshots | required |

## generate_write_pointers

### Description:
Assign to each particle a pointer from its index at the reference (later) snapshot
to its index (and species name) at all other (earlier) snapshots.
Write particle pointers to file, one file for each snapshot besides the reference snapshot.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| snapshot_indices | array-like |     snapshot indices at which to assign pointers | required |
| reference_snapshot_index | int or str |     index of reference (final) snapshot to compute particle pointers relative to | required |
| proc_number | int |     number of parallel processes to run | required |

## init ParticlePointerClass

### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| species_names | str or list |     name[s] of particle species to track | required |
| simulation_directory | str |     directory of simulation | required |
| track_directory | str |     directory of files for particle pointers and formation coordinates | required |
| snapshot_directory | str |     directory of snapshot files (within simulation directory) | required |

## io_pointers

### Description:
Read or write, for each star particle at the reference (later, z0) snapshot
its pointer index (and species name) to the other (earlier, z) snapshot.
If input particle catalog (part), append pointers as dictionary class to part,
else return pointers as a dictionary class.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| part | dict |     catalog of particles at a the (earlier, z) snapshot | required |
| snapshot_index | int |     index of the (earlier, z) snapshot to read | required |
| Pointer | dict class |     particle pointers (if writing) | required |
| simulation_directory | str |     directory of simulation | required |
| track_directory | str |     directory of files for particle pointers and formation coordinates | required |
| verbose | bool |     whether to print diagnostic information | required |

## read_pointers_between_snapshots

### Description:
Get particle pointer indices for single species between any two snapshots.
Given input snapshot indices, get array of pointer indices from snapshot_index_from to
snapshot_index_to.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| snapshot_index_from | int |     snapshot index to get pointers from | required |
| snapshot_index_to | int |     snapshot index to get pointers to | required |
| species_name | str |     name of particle species to track | required |
| simulation_directory | str |     directory of simulation | required |

## add_intermediate_pointers

### Description:
Add pointers between an intermediate snapshot (zi) and the earlier snapshot (z),
to allow tracking between these 2 snapshots at z > 0.
The intermediate snapshot (zi) must be between the reference (z0) snapshot and the earlier
(z) snapshot.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| Pointer | dict class |     pointers to an intemediate snapshot (between z0 and z) | required |

## assign_forward_pointers

### Description:
Assign pointer indices going forward in time, from the earlier (z) snapshot to the
reference (later) snapshot.
Currently, if gas cell split, assigns only one split gas cell as a descendant.
TODO: deal with gas cells splitting


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| intermediate_snapshot | bool |     whether to get pointers between z and an intermediate snapshot (at z > 0) | required |

## get_pointers

### Description:
Get pointer indices (and species) from species_name_from particles at the
reference (later) snapshot to species_names_to particles the earlier snapshot.
If enable forward, get pointers going forward in time (from z to z_ref) instead.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| species_name_from | str |     name of species at the reference (later, z0) snapshot | required |
| species_names_to | str or list |     name[s] of species to get pointers to at the (earlier, z) snapshot | required |
| part_indices | arr |     indices of particles at the reference (later, z0) snapshot | required |
| forward | bool |     whether to get pointers from the (earlier, z) snapshot to the reference (later, z0)<br />    snapshot, that is, tracking forward in time default (forward=False) is tracking<br />    backwards in time | required |
| intermediate_snapshot | bool |     whether to get pointers between z and an intermediate snapshot (at z > 0)<br />    default (intermediate_snapshot=False) is to get pointers to/from z0 | required |
| return_single_array | bool |     if tracking single species at both snapshots, whether to return single array of<br />    pointer indices (instead of dictionary of pointers that includes species names) | required |

## init ParticlePointerDictionaryClass

### Description:
Given input particle catalogs, store summary info about snapshots and particle counts.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| part_z0 | dict |     catalog of particles at the reference (later) snapshot | required |
| part_z | dict |     catalog of particles at the reference (later) snapshot | required |
| species_names | str or list |     name[s] of particle species to track | required |
| id_name | str |     dictionary key of particle id | required |
