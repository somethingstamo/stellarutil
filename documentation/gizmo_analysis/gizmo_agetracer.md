# Table of Contents
 - [initialize_agetracers](#initialize_agetracers): Master function to set up age-tracer information in particle catalog[s].
 - [parse_element_names](#parse_element_names): Utility function to parse the input element names.
- ElementAgeTracerClass Class
    - [assign_age_bins](#assign_age_bins): Assign to self the age bins used by the age-tracer module in a Gizmo simulation.
You can do this 3 ways:
    (1) input a dictionary of the header information from a Gizmo simulation snapshot,
        as tabulated in gizmo_io.py, which contains the age-tracer age bin information
    (2) input an array of (custom) age bins
    (3) input the number of age bins and the min and max age,
        to use to generate age bins, assuming equal spacing in log age
    - [assign_element_initial_massfraction](#assign_element_initial_massfraction): Set the initial conditions for the elemental abundances (mass fractions),
to add to the age-tracer nucleosynthetic yields.
You need to run assign_element_yield_massfractions() before calling this.
If you do not call this, will assume that all particles started with initial mass fraction
for all elements (beyond H) of 0.
    - [assign_element_yield_massfractions](#assign_element_yield_massfractions): Assign to self a dictionary of stellar nucleosynthetic yield mass fractions within
stellar age bins.
Use to map (multiply) the age-tracer mass weights in each age bin into elemental abundances
(mass fractions).
    - [get_element_massfractions](#get_element_massfractions): Get the actual elemental abundances (mass fractions) for input element_name[s],
using the the input 2-D array of age-tracer mass weights.

Before you call this method, you must
    (1) set up the age bins via
        assign_age_bins()
    (2) assign the nucleosynthetic yield mass fraction within each age bin for each element
        assign_element_yield_massfractions()
    (3) (optional) assign the initial abundance (mass fraction) for each element via
        assign_element_initial_massfraction()
    - [init ElementAgeTracerClass](#init-elementagetracerclass): Initialize self's dictionary to store all age-tracer information.
- ElementAgeTracerZClass Class
    - [assign_element_yield_massfractions](#assign_element_yield_massfractions): Assign to self a dictionary of stellar nucleosynthetic yields within stellar age bins.
    - [get_element_massfractions](#get_element_massfractions): Get the elemental abundances (mass fractions) for input element_name[s],
using the the input 2-D array of age-tracer weights.

Before you call this method, you must:
    (1) set up the age bins via:
        assign_age_bins()
    (2) assign the nucleosynthetic yield mass fraction within each age bin for each element:
        assign_element_yield_massfractions()
    (3) (optional) assign the initial abundance (mass fraction) for each element via:
        assign_element_initial_massfraction()
- FIREYieldClass Class
    - [_get_element_yield_rate](#_get_element_yield_rate): Return the specific rate of nucleosynthetic yield (yield mass relative to IMF-averaged mass
of stars at that time) [Myr ^ -1] at input stellar age [Myr] for input element_name,
from all stellar processes.
get_element_yields() uses this to integrate across age within each age bin.
    - [get_element_yields](#get_element_yields): Construct and return a dictionary of stellar nucleosynthetic yields.
* Each key is an element name
* Each key value is a 1-D array of yields within each input age bin,
  constructed by integrating the total yield for each element across each age bin.

Supply the returned element_yield_dict to
    ElementAgeTracerClass.assign_element_yield_massfractions()
to assign elemental abundances to star particles or gas cells via the age-tracer mass
weights ina Gizmo simulation.
    - [init FIREYieldClass](#init-fireyieldclass)
- NuGridYieldClass Class
    - [compute_yields](#compute_yields): Runs through the Sygma model given model parameters.
This function is not strictly necessary in a YieldsObject, but exists here to pre-compute
information needed for the `yields` function so it is not re-computed each time called.
    - [get_element_yields](#get_element_yields)
    - [init NuGridYieldClass](#init-nugridyieldclass): .

## initialize_agetracers

### Description:
Master function to set up age-tracer information in particle catalog[s].


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| parts | dict or list |     catalogs[s] of particles at a snapshot | required |
| species_names | str or list |     name[s] of particle species to assign age-tracers to: 'star', 'gas' | required |
| progenitor_metallicity | float |     metallicity to assume for all progenitor stars in calculating nucleosynthetic yields | required |
| metallicity_initial | float |     initial metallicity to assign to 'unenriched' gas cells at the start of the simulation<br />    [linear mass fraction relative to Solar] | required |
| yield_model | str |     model to use for yields: 'fire2', 'fire2.1', 'fire2.2' | required |
| YieldClass | class |     class to calculate nucleosynthetic yields in age bins | required |

## parse_element_names

### Description:
Utility function to parse the input element names.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| element_names_possible | list of str |     possible names of elements in a given model | required |
| element_names | str or list |     possible names of elements in a given model | required |
| scalarize | bool |     whether to return single string (instead of list) if input single string | required |

## assign_age_bins

### Description:
Assign to self the age bins used by the age-tracer module in a Gizmo simulation.
You can do this 3 ways:
    (1) input a dictionary of the header information from a Gizmo simulation snapshot,
        as tabulated in gizmo_io.py, which contains the age-tracer age bin information
    (2) input an array of (custom) age bins
    (3) input the number of age bins and the min and max age,
        to use to generate age bins, assuming equal spacing in log age


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| header_dict | dict |     dictionary that contains header information from a Gizmo snapshot file<br />    use this to assign age-tracer stellar age bin information | required |
| age_bins | array |     age bins [Myr], with N_age-bins + 1 values: left edges plus right edge of final bin | required |
| age_bin_number | int |     number of age bins | required |
| age_min | float |     minimum age (left edge of first bin) [Myr] (over-ride this to be self._age_min_impose) | required |
| age_max | float |     maximum age (right edge of final bin) [Myr] (over-ride this to be self._age_max_impose) | required |

## assign_element_initial_massfraction

### Description:
Set the initial conditions for the elemental abundances (mass fractions),
to add to the age-tracer nucleosynthetic yields.
You need to run assign_element_yield_massfractions() before calling this.
If you do not call this, will assume that all particles started with initial mass fraction
for all elements (beyond H) of 0.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| massfraction_initial_dict | dict |     Keys are element names and values are the linear mass fraction for each element,<br />    to use as initial conditions (at early cosmic times) for each particle.<br />    Default to 0 for any element that is not in input massfraction_initial_dict. | required |
| metallicity | float |     Linear total metallity relative to Solar.<br />    If defined, assume that input massfraction_initial_dict are Solar mass fractions,<br />    and multiply them by this value. | required |
| helium_massfraction | float |     If defined, use this for the initial mass fraction of helium, over-writing any value in<br />    input massfraction_initial_dict. | required |

## assign_element_yield_massfractions

### Description:
Assign to self a dictionary of stellar nucleosynthetic yield mass fractions within
stellar age bins.
Use to map (multiply) the age-tracer mass weights in each age bin into elemental abundances
(mass fractions).


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| element_yield_dict | dict of 1-D arrays |     nucleosynthetic yield fractional mass (relative to IMF-averaged mass of stars at that<br />    time) of each element produced within each age bin | required |
| _progenitor_metal_massfractions | array |     placeholder for future development | required |

## get_element_massfractions

### Description:
Get the actual elemental abundances (mass fractions) for input element_name[s],
using the the input 2-D array of age-tracer mass weights.

Before you call this method, you must
    (1) set up the age bins via
        assign_age_bins()
    (2) assign the nucleosynthetic yield mass fraction within each age bin for each element
        assign_element_yield_massfractions()
    (3) (optional) assign the initial abundance (mass fraction) for each element via
        assign_element_initial_massfraction()


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| element_name | str |     name of element to get mass fraction of for each particle | required |
| agetracer_mass_weights | 2-D array (N_particle x N_age-bins) |     age-tracer mass weights for particles - should be values from<br />        part[species_name]['massfraction'][:, self['element.index.start']:],<br />        where species_name = 'star' or 'gas' | required |
| _metal_massfractions | 1-D array |     placeholder for future development | required |

## init ElementAgeTracerClass

### Description:
Initialize self's dictionary to store all age-tracer information.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| header_dict | dict |     dictionary that contains header information from a Gizmo snapshot file, as tabulated in<br />    gizmo_io.py, to assign all age-tracer age bin information.<br />    If you do not input header_dict, you need to assign age bins via assign_age_bins(). | required |
| element_index_start | int |     index of first age-tracer field in Gizmo's particle element mass fraction array.<br />    If you input header_dict, it will over-ride any value here. | required |

## assign_element_yield_massfractions

### Description:
Assign to self a dictionary of stellar nucleosynthetic yields within stellar age bins.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| element_yield_dict | list of dicts of 1-D arrays |     nucleosynthetic yield fractional mass [M_sun per M_sun of stars formed] of each element<br />    produced within/across each age bin, to map the age-tracer mass weights in each age bin<br />    into actual element yields | required |
| progenitor_metal_massfractions | array | None | required |

## get_element_massfractions

### Description:
Get the elemental abundances (mass fractions) for input element_name[s],
using the the input 2-D array of age-tracer weights.

Before you call this method, you must:
    (1) set up the age bins via:
        assign_age_bins()
    (2) assign the nucleosynthetic yield mass fraction within each age bin for each element:
        assign_element_yield_massfractions()
    (3) (optional) assign the initial abundance (mass fraction) for each element via:
        assign_element_initial_massfraction()


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| element_name | str |     name of element to get mass fraction of for each particle | required |
| agetracer_mass_weights | 2-D array (N_particle x N_age-bins) |     age-tracer mass weights for particles - should be values from<br />        part[species_name]['massfraction'][:, self['element.index.start']:],<br />        where species_name = 'star' or 'gas' | required |
| metallicities | array | None | required |

## _get_element_yield_rate

### Description:
Return the specific rate of nucleosynthetic yield (yield mass relative to IMF-averaged mass
of stars at that time) [Myr ^ -1] at input stellar age [Myr] for input element_name,
from all stellar processes.
get_element_yields() uses this to integrate across age within each age bin.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| age | float |     stellar age [Myr] at which to compute the nucleosynthetic yield rate | required |
| element_name | str |     name of element, must be in self.element_names | required |
| progenitor_metallicity | float |     metallicity [linear mass fraction relative to Solar]<br />    In FIRE-2 and FIRE-3, this determines the mass-loss rate of stellar winds. | required |

## get_element_yields

### Description:
Construct and return a dictionary of stellar nucleosynthetic yields.
* Each key is an element name
* Each key value is a 1-D array of yields within each input age bin,
  constructed by integrating the total yield for each element across each age bin.

Supply the returned element_yield_dict to
    ElementAgeTracerClass.assign_element_yield_massfractions()
to assign elemental abundances to star particles or gas cells via the age-tracer mass
weights ina Gizmo simulation.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| age_bins | array |     stellar age bins used in Gizmo for the age-tracer model [Myr]<br />    Should have N_age-bins + 1 values: left edges plus right edge of final bin. | required |
| element_names | list |     names of elements to generate, if only generating a subset<br />    If input None, assign all elements in this model. | required |

## init FIREYieldClass

### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| model | str |     name for this rate + yield model: 'fire2', 'fire3'<br />    'fire2.1' is 'fire2' but removes prgenitor metallicity dependence to all yields<br />    'fire2.2' is 'fire2.1' but also removes progenitor metallicity dependence to<br />    stellar wind mass-loss rates | required |
| progenitor_metallicity | float |     metallicity [linear mass fraction relative to Solar]<br />    for nucleosynthetic rates and yields that depend on progenitor metallicity | required |

## compute_yields

### Description:
Runs through the Sygma model given model parameters.
This function is not strictly necessary in a YieldsObject, but exists here to pre-compute
information needed for the `yields` function so it is not re-computed each time called.


## get_element_yields

### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| t | float or array |     time [Gyr] to compute instantaneous yield rate | required |
| element | str |     element name, must be in self dictionary | required |

## init NuGridYieldClass

### Description:
.

