# Table of Contents
- InitialConditionClass Class
    - [init InitialConditionClass](#init-initialconditionclass)
    - [read_halos](#read_halos): Read catalog of halos at the final snapshot.
    - [read_halos_and_particles](#read_halos_and_particles): Read halos at the final snapshot and particles at the final and the initial snapshot.
    - [read_particles](#read_particles): Read particles at the final and the initial snapshot.
    - [write_positions_at_initial_snapshot](#write_positions_at_initial_snapshot): Select dark-matter particles at the final snapshot, write a file of their positions at
the initial snapshot.

If input a halo catalog (hal) and halo index (hal_index) (typically from a
uniform-resolution DM-only simulation), select volume around that halo.

Else, assume that working from an existing zoom-in simulation, re-select spherical volume
around its host center.

If you do not supply particle catalogs (parts), read them at the fiducial snapshots.

Rule of thumb from Onorbe et al:
    given distance_pure, if region_kind in ['particles', 'convex-hull']:
        distance_max = (1.5 * refinement_number + 7) * distance_pure

## init InitialConditionClass

### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| snapshot_redshifts | list |     redshifts of initial and final snapshots | required |
| simulation_directory | str |     base directory of simulation | required |

## read_halos

### Description:
Read catalog of halos at the final snapshot.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| mass_limits | list |     min and max halo mass to assign low-res DM mass | required |
| file_kind | str |     kind of halo file: 'hdf5', 'out', 'ascii', 'hlist' | required |
| assign_nearest_neighbor | bool |     whether to assign nearest neighboring halo | required |

## read_halos_and_particles

### Description:
Read halos at the final snapshot and particles at the final and the initial snapshot.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| mass_limits | list |     min and max halo mass to assign low-res DM mass | required |

## read_particles

### Description:
Read particles at the final and the initial snapshot.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| properties | str or list |     name[s] of particle properties to read | required |
| sort_dark_by_id | bool |     whether to sort dark-matter particles by id | required |

## write_positions_at_initial_snapshot

### Description:
Select dark-matter particles at the final snapshot, write a file of their positions at
the initial snapshot.

If input a halo catalog (hal) and halo index (hal_index) (typically from a
uniform-resolution DM-only simulation), select volume around that halo.

Else, assume that working from an existing zoom-in simulation, re-select spherical volume
around its host center.

If you do not supply particle catalogs (parts), read them at the fiducial snapshots.

Rule of thumb from Onorbe et al:
    given distance_pure, if region_kind in ['particles', 'convex-hull']:
        distance_max = (1.5 * refinement_number + 7) * distance_pure


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| parts | list of dicts |     catalogs of particles at final and initial snapshots | required |
| host_index | int |     index of primary host halo in the particle catalog to use to get position and radius<br />    (if not input halo catalog) | required |
| hal | dict |     catalog of halos at the final snapshot | required |
| hal_index | int |     index of primary host halo | required |
| distance_max | float |     distance from center to select particles at the final snapshot<br />    [kpc physical, or in units of R_halo] | required |
| scale_to_halo_radius | bool |     whether to scale distance to halo radius | required |
| virial_kind | str |     virial overdensity to define halo radius | required |
| region_kind | str |     method to identify zoom-in regon at initial time: 'particles', 'convex-hull', 'cube' | required |
| dark_mass | float |     DM particle mass (if simulation has only DM, at single resolution) | required |
