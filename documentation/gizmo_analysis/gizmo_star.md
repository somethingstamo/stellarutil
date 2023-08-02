# Table of Contents
 - [get_ages_transition](#get_ages_transition): Get array of ages [Myr] that mark transitions in stellar evolution for a given model.
Use to supply to numerical integrators.
 - [get_sun_massfraction](#get_sun_massfraction): Get dictionary of Solar abundances (mass fractions) for the elements that Gizmo tracks.
(These may differ by up to a percent from the values in utilities.constant, given choices of
mean atomic mass.)
 - [plot_mass_loss_v_age](#plot_mass_loss_v_age): Plot fractional mass loss (relative to mass of stars at that age) from all stellar evolution
channels (stellar winds, core-collapse and white-dwarf supernovae) versus stellar age [Myr].
 - [plot_nucleosynthetic_yields](#plot_nucleosynthetic_yields): Plot nucleosynthetic yield mass [M_sun] v element name, for input event_kind[s].
 - [plot_supernova_number_v_age](#plot_supernova_number_v_age): Plot specific rates or cumulative numbers [per M_sun of stars at that age] of
core-collapse and white-dwarf (Ia) supernova events versus stellar age [Myr].
- MassLossClass Class
    - [_make_mass_loss_spline](#_make_mass_loss_spline): Create 2-D bivariate spline (in age and metallicity) for fractional mass loss
relative to mass of stars at that age via all stellar evolution channels.
    - [_parse_model](#_parse_model): Parse input model.
    - [get_mass_loss](#get_mass_loss): Get fractional mass loss[es] (relative to mass of stars at that age)
via all stellar evolution channels within age interval[s] in the FIRE-2 or FIRE-3 model.
    - [get_mass_loss_from_spline](#get_mass_loss_from_spline): Get fractional mass loss[es] (relative to mass of stars at that age) via all stellar
evolution channels at ages and metallicities (or metal mass fractions)
via 2-D (bivariate) spline.
    - [get_mass_loss_rate](#get_mass_loss_rate): Get rate[s] of fractional mass loss (relative to mass of stars at that age) [Myr ^ -1]
from all stellar evolution channels in FIRE-2 or FIRE-3.
    - [init MassLossClass](#init-masslossclass)
- NucleosyntheticYieldClass Class
    - [_parse_model](#_parse_model): Parse input model.
    - [assign_element_yields](#assign_element_yields): Store nucleosynthetic yields from all stellar channels, for a fixed progenitor metallicity,
as dictionaries with element name as kwargs and yield [mass fraction wrt total
ejecta/wind mass] as values.
Useful to avoid having to re-call get_element_yields() many times.
    - [get_element_yields](#get_element_yields): Get dictionary of stellar nucleosynthetic yields for a single event_kind event
in the FIRE-2 or FIRE-3 model.
Return each yield as a mass fraction [mass of element / total ejecta mass] if return_mass
is False (default), else return mass of element [Msun] if return_mass is True.
Stellar wind yield is always/intrinsically mass fraction [wrt wind mass].

For stellar winds, FIRE-2 and FIRE-3 add the existing surface abundances from the progenitor
to the injected yield for elements not included in its yield.
For supernovae (core-collapse and white-dwarf), FIRE-2 and FIRE-3 do not add any existing
surface abundances from the progenitor to the yield.
    - [init NucleosyntheticYieldClass](#init-nucleosyntheticyieldclass): Store Solar elemental abundances, as linear mass fractions.

FIRE-2 uses Solar values from Anders & Grevesse 1989.
FIRE-3 uses proto-Solar values from Asplund et al 2009.
- StellarWindClass Class
    - [_parse_model](#_parse_model): Parse input model.
    - [get_mass_loss](#get_mass_loss): Get cumulative fractional mass loss[es] (wrt mass of IMF-averaged stars at that age) from
stellar winds within input age interval[s].
    - [get_mass_loss_rate](#get_mass_loss_rate): Get rate[s] of fractional mass loss (wrt IMF-averaged mass of stars at that age) [Myr ^ -1]
from stellar winds in FIRE-2 or FIRE-3.
Input either metallicity (linear, wrt Solar) or (raw) metal_mass_fraction.

Includes all non-supernova mass-loss channels, dominated by O, B, and AGB stars.
    - [init StellarWindClass](#init-stellarwindclass)
- SupernovaCCClass Class
    - [_get_rate_fire3](#_get_rate_fire3)
    - [_parse_model](#_parse_model): Parse input model.
    - [get_mass_loss](#get_mass_loss): Get fractional mass loss[es] from core-collapse supernovae across input age interval[s]
(ejecta mass relative to IMF-averaged mass of stars at that age).
    - [get_mass_loss_rate](#get_mass_loss_rate): Get fractional mass-loss rate[s] from core-collapse supernovae at input age[s]
(ejecta mass relative to IMF-averaged mass of stars at that age) [Myr ^ -1].
    - [get_number](#get_number): Get specific number[s] of core-collapse supernova events in input age interval[s]
[per M_sun of stars at that age].
    - [get_rate](#get_rate): Get specific rate[s] of core-collapse supernova events at input age[s]
[Myr ^ -1 per M_sun of stars at that age].

FIRE-2
    Rates are from Starburst99 energetics: get rate from overall energetics assuming each
    core-collapse supernova is 10^51 erg.
    Core-collapse supernovae occur from 3.4 to 37.53 Myr after formation:
        3.4 to 10.37 Myr:    rate / M_sun = 5.408e-10 yr ^ -1
        10.37 to 37.53 Myr:  rate / M_sun = 2.516e-10 yr ^ -1
    - [init SupernovaCCClass](#init-supernovaccclass)
- SupernovaWDClass Class
    - [_get_rate](#_get_rate)
    - [_parse_model](#_parse_model): Parse input model.
    - [get_mass_loss](#get_mass_loss): Get fractional mass loss[es] from WD supernovae in input age interval[s]
(ejecta mass relative to IMF-averaged mass of stars at that age).
    - [get_mass_loss_rate](#get_mass_loss_rate): Get fractional mass loss rate[s] from WD supernovae in input age interval[s]
(ejecta mass relative to IMF-averaged mass of stars at that age) [Myr ^ -1].
    - [get_number](#get_number): Get specific number[s] of WD supernova events in input age interval[s]
[per M_sun of stars at that age].
    - [get_rate](#get_rate): Get specific rate[s] of WD supernova events [Myr ^ -1 per M_sun of stars at that age].

FIRE-2
    rates are from Mannucci, Della Valle, & Panagia 2006, for a delayed population
    (constant rate) + prompt population (Gaussian), starting 37.53 Myr after formation:
    rate / M_sun = 5.3e-14 + 1.6e-11 * exp(-0.5 * ((star_age - 5e-5) / 1e-5) ** 2) yr ^ -1

FIRE-3
    power-law model from Maoz & Graur 2017, starting 44 Myr after formation
    normalized to 1.6 events per 1000 Msun per Hubble time:
    rate / M_sun = 2.67e-13 * (star_age / 1e6) ** (-1.1) yr ^ -1
    - [init SupernovaWDClass](#init-supernovawdclass)

## get_ages_transition

### Description:
Get array of ages [Myr] that mark transitions in stellar evolution for a given model.
Use to supply to numerical integrators.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| model | str |     stellar evolution model: 'fire2', 'fire3' | required |

## get_sun_massfraction

### Description:
Get dictionary of Solar abundances (mass fractions) for the elements that Gizmo tracks.
(These may differ by up to a percent from the values in utilities.constant, given choices of
mean atomic mass.)


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| model | str |     stellar evolution model: 'fire2', 'fire3' | required |

## plot_mass_loss_v_age

### Description:
Plot fractional mass loss (relative to mass of stars at that age) from all stellar evolution
channels (stellar winds, core-collapse and white-dwarf supernovae) versus stellar age [Myr].


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| mass_loss_kind | str |     'rate' or 'mass' | required |
| mass_loss_limits | list |     min and max limits to impose on y-axis | required |
| mass_loss_log_scale | bool |     whether to use logarithmic scaling for age bins | required |
| element_name | str |     name of element to get yield of (if None, compute total mass loss) | required |
| metallicity | float |     (linear) total abundance of metals wrt Solar | required |
| metal_mass_fraction | float |     mass fration of all metals (everything not H, He) | required |
| model | str |     model for rates: 'fire2', 'fire3' | required |
| age_limits | list |     min and max limits of age of stellar population [Myr] | required |
| age_bin_width | float |     width of stellar age bin [Myr] | required |
| age_log_scale | bool |     whether to use logarithmic scaling for age bins | required |
| file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |
| directory | str |     directory in which to write figure file | required |
| figure_index | int |     index for matplotlib window | required |

## plot_nucleosynthetic_yields

### Description:
Plot nucleosynthetic yield mass [M_sun] v element name, for input event_kind[s].


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| event_kinds | str or list |     stellar event: 'wind', 'supernova.cc', 'supernova.wd' or 'supernova.ia', 'all' | required |
| metallicity | float |     metallicity of progenitor [linear mass fraction wrt to Solar] | required |
| model | str |     stellar evolution model for yields: 'fire2', 'fire3' | required |
| axis_y_limits | list |     min and max limits of y axis | required |
| axis_y_log_scale | bool |     whether to use logarithmic scaling for y axis | required |
| file_name | str |     whether to write figure to file and its name. True = use default naming convention | required |
| directory | str |     directory to write figure file | required |
| figure_index | int |     index of figure for matplotlib | required |

## plot_supernova_number_v_age

### Description:
Plot specific rates or cumulative numbers [per M_sun of stars at that age] of
core-collapse and white-dwarf (Ia) supernova events versus stellar age [Myr].


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| axis_y_kind | str |     'rate' or 'number' | required |
| axis_y_limits | list |     min and max limits to impose on y axis | required |
| axis_y_log_scale | bool |     whether to duse logarithmic scaling for y axis | required |
| age_limits | list |     min and max limits of age of stellar population [Myr] | required |
| age_bin_width | float |     width of stellar age bin [Myr] | required |
| age_log_scale | bool |     whether to use logarithmic scaling for age bins | required |
| file_name | str |     whether to write figure to file, and set its name: True = use default naming convention | required |
| directory | str |     where to write figure file | required |
| figure_index | int |     index for matplotlib window | required |

## _make_mass_loss_spline

### Description:
Create 2-D bivariate spline (in age and metallicity) for fractional mass loss
relative to mass of stars at that age via all stellar evolution channels.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| age_limits | list |     min and max limits of age of stellar population [Myr] | required |
| age_bin_number | int |     number of age bins within age_limits | required |
| metallicity_limits | list |     min and max limits of (linear) metallicity | required |
| metallicity_bin_number | float |     number of metallicity bins | required |

## _parse_model

### Description:
Parse input model.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| model | str |     stellar evolution model to use: 'fire2', 'fire3' | required |

## get_mass_loss

### Description:
Get fractional mass loss[es] (relative to mass of stars at that age)
via all stellar evolution channels within age interval[s] in the FIRE-2 or FIRE-3 model.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| age_min | float |     min (starting) age of stellar population [Myr] | required |
| age_maxs | float or array |     max (ending) age[s] of stellar population [Myr] | required |
| metallicity | float |     metallicity [(linear) wrt Sun] of progenitor, for scaling the wind rates<br />    input either this or metal_mass_fraction (below)<br />    For FIRE-2, this should be *total* metallicity [scaled to Solar := 0.02]<br />    For FIRE-3, this should be Iron abundance [scaled to Solar := 1.38e-3] | required |
| metal_mass_fraction | float |     optional: mass fraction of given metal in progenitor stars<br />    input either this or metallicity (above)<br />    For FIRE-2, this should be *total* metals (everything not H, He).<br />    For FIRE-3, this should be iron. | required |
| optional | mass fraction of given metal in progenitor stars | None | required |
| element_name | str [optional] |     name of element to get fractional mass loss of<br />    if None or '', get mass loss from all elements | required |

## get_mass_loss_from_spline

### Description:
Get fractional mass loss[es] (relative to mass of stars at that age) via all stellar
evolution channels at ages and metallicities (or metal mass fractions)
via 2-D (bivariate) spline.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ages | float or array |     age[s] of stellar population [Myr] | required |
| metallicities | float or array |     metallicity [linear wrt Solar] of progenitor, for scaling the wind rates<br />    input either this or metal_mass_fraction (below)<br />    For FIRE-2, this should be *total* metallicity [scaled to Solar := 0.02].<br />    For FIRE-3, this should be iron abundance [scaled to Solar := 1.38e-3]. | required |
| metal_mass_fractions | float or array |     optional: mass fraction of given metal in progenitor stars<br />    input either this or metallicity (above)<br />    For FIRE-2, this should be *total* metals (everything not H, He).<br />    For FIRE-3, this should be iron. | required |
| optional | mass fraction of given metal in progenitor stars | None | required |

## get_mass_loss_rate

### Description:
Get rate[s] of fractional mass loss (relative to mass of stars at that age) [Myr ^ -1]
from all stellar evolution channels in FIRE-2 or FIRE-3.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| age | float or array |     age[s] of stellar population [Myr] | required |
| metallicity | float |     metallicity [(linear) wrt Sun] of progenitor, for scaling the wind rates<br />    input either this or metal_mass_fraction (below)<br />    For FIRE-2, this should be *total* metallicity [scaled to Solar := 0.02]<br />    For FIRE-3, this should be Iron abundance [scaled to Solar := 1.38e-3] | required |
| metal_mass_fraction | float |     optional: mass fraction of given metal in progenitor stars<br />    input either this or metallicity (above)<br />    For FIRE-2, this should be *total* metals (everything not H, He)<br />    For FIRE-3, this should be iron | required |
| optional | mass fraction of given metal in progenitor stars | None | required |
| element_name | str [optional] |     name of element to get fractional mass loss of<br />    if None or '', get mass loss from all elements | required |

## init MassLossClass

### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| model | str |     stellar evolution model to use: 'fire2', 'fire2.1', 'fire2.2', 'fire3' | required |

## _parse_model

### Description:
Parse input model.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| model | str |     stellar evolution model for yields: 'fire2', 'fire3' | required |

## assign_element_yields

### Description:
Store nucleosynthetic yields from all stellar channels, for a fixed progenitor metallicity,
as dictionaries with element name as kwargs and yield [mass fraction wrt total
ejecta/wind mass] as values.
Useful to avoid having to re-call get_element_yields() many times.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| progenitor_metallicity | float |     total metallicity of progenitor [linear mass fraction wrt sun_mass_fraction['metals']] | required |
| progenitor_massfraction_dict | dict or bool [optional] |     optional: dictionary that contains the mass fraction of each element in the progenitor<br />    if blank, then assume Solar abundance ratios and use progenitor_metallicity to normalize<br />    For FIRE-2, use to add corrections from surface abundances for supernovae.<br />    For FIRE-3, use to compute stellar winds yields. | required |
| optional | dictionary that contains the mass fraction of each element in the progenitor | None | required |
| age | float |     stellar age [Myr] | required |

## get_element_yields

### Description:
Get dictionary of stellar nucleosynthetic yields for a single event_kind event
in the FIRE-2 or FIRE-3 model.
Return each yield as a mass fraction [mass of element / total ejecta mass] if return_mass
is False (default), else return mass of element [Msun] if return_mass is True.
Stellar wind yield is always/intrinsically mass fraction [wrt wind mass].

For stellar winds, FIRE-2 and FIRE-3 add the existing surface abundances from the progenitor
to the injected yield for elements not included in its yield.
For supernovae (core-collapse and white-dwarf), FIRE-2 and FIRE-3 do not add any existing
surface abundances from the progenitor to the yield.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| event_kind | str |     stellar event: 'wind', 'supernova.cc', 'supernova.wd' or 'supernova.ia' | required |
| progenitor_metallicity | float |     total metallicity of progenitor [linear mass fraction wrt sun_mass_fraction['metals']] | required |
| progenitor_massfraction_dict | dict or bool [optional] |     optional: dictionary that contains the mass fraction of each element in the progenitor<br />    if blank, then assume Solar abundance ratios and use progenitor_metallicity to normalize<br />    For FIRE-2, use to add corrections from surface abundances for supernovae.<br />    For FIRE-3, use to compute stellar winds yields. | required |
| optional | dictionary that contains the mass fraction of each element in the progenitor | None | required |
| age | float |     stellar age [Myr] | required |
| model | str |     stellar evolution model for yields: 'fire2', 'fire2.1', 'fire2.2', 'fire3' | required |
| return_mass | bool |     whether to return total mass of each element [Msun],<br />    instead of mass fraction wrt total ejecta/wind mass. | required |

## init NucleosyntheticYieldClass

### Description:
Store Solar elemental abundances, as linear mass fractions.

FIRE-2 uses Solar values from Anders & Grevesse 1989.
FIRE-3 uses proto-Solar values from Asplund et al 2009.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| model | str |     stellar evolution model for yields: 'fire2', 'fire3' | required |

## _parse_model

### Description:
Parse input model.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| model | str |     model for stellar wind rate: 'fire2', 'fire3' | required |

## get_mass_loss

### Description:
Get cumulative fractional mass loss[es] (wrt mass of IMF-averaged stars at that age) from
stellar winds within input age interval[s].


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| age_min | float |     min age of stellar population [Myr] | required |
| age_maxs | float or array |     max age[s] of stellar population [Myr] | required |
| metallicity | float |     metallicity [linear mass fraction wrt Solar] of progenitor, for scaling the wind rates<br />    input either this or metal_mass_fraction (below)<br />    For FIRE-2, this should be *total* metallicity [scaled to Solar := 0.02]<br />    For FIRE-3, this should be Iron abundance [scaled to Solar := 1.38e-3] | required |
| metal_mass_fraction | float |     optional: mass fraction of given metal in progenitor stars<br />    input either this or metallicity (above)<br />    For FIRE-2, this should be *total* metals (everything not H, He)<br />    For FIRE-3, this should be iron | required |
| optional | mass fraction of given metal in progenitor stars | None | required |
| model | str |     model for wind rate: 'fire2', 'fire2.1', 'fire2.2', 'fire3' | required |
| element_name | str |     name of element to get fractional mass loss of<br />    if None or '', get total fractional mass loss (wrt mass of stars at that age) | required |

## get_mass_loss_rate

### Description:
Get rate[s] of fractional mass loss (wrt IMF-averaged mass of stars at that age) [Myr ^ -1]
from stellar winds in FIRE-2 or FIRE-3.
Input either metallicity (linear, wrt Solar) or (raw) metal_mass_fraction.

Includes all non-supernova mass-loss channels, dominated by O, B, and AGB stars.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| age | float or array |     age[s] of stellar population [Myr] | required |
| metallicity | float |     metallicity [linear mass fraction wrt Solar] of progenitor, for scaling the wind rates<br />    input either this or metal_mass_fraction (below)<br />    For FIRE-2, this should be *total* metallicity [scaled to Solar := 0.02]<br />    For FIRE-3, this should be Iron abundance [scaled to Solar := 1.38e-3] | required |
| metal_mass_fraction | float |     optional: mass fraction of given metal in progenitor stars<br />    input either this or metallicity (above)<br />    For FIRE-2, this should be *total* metals (everything not H, He)<br />    For FIRE-3, this should be iron | required |
| optional | mass fraction of given metal in progenitor stars | None | required |
| model | str |     model for wind rate: 'fire2', 'fire2.1', 'fire2.2', 'fire3' | required |
| element_name | str |     name of element to get fractional mass loss of<br />    if None or '', get total fractional mass loss (wrt mass at stars at that age) | required |

## init StellarWindClass

### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| model | str |      model for wind rate: 'fire2', 'fire2.1', 'fire2.2', 'fire3' | required |

## _get_rate_fire3

## _parse_model

### Description:
Parse input model.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| model | str |     model for core-collapse supernova rates (delay time distribution): 'fire2', 'fire3' | required |
| sncc_age_min | float |     minimum age for core-collapse supernova to occur [Myr] | required |
| sncc_age_break | float |     age at which rate of core-collapse supernova changes/breaks [Myr] | required |
| sncc_age_min | float |     minimum age for core-collapse supernova to occur [Myr] | required |

## get_mass_loss

### Description:
Get fractional mass loss[es] from core-collapse supernovae across input age interval[s]
(ejecta mass relative to IMF-averaged mass of stars at that age).


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| age_min | float |     min age of stellar population [Myr] | required |
| age_maxs | float or array |     max age[s] of stellar population [Myr] | required |
| model | str |     model for core-collapse supernova rates (delay time distribution): 'fire2', 'fire3' | required |
| sncc_age_min | float |     minimum age for core-collapse supernova to occur [Myr] | required |
| sncc_age_break | float |     age at which rate of core-collapse supernova changes/breaks [Myr] | required |
| sncc_age_min | float |     minimum age for core-collapse supernova to occur [Myr] | required |
| element_name | str [optional] |     name of element to get fractional mass loss of<br />    if  None or '', get mass loss fraction from total ejecta | required |
| metallicity | float |     metallicity (wrt Solar) of progenitor stars (for Nitrogen yield in FIRE-2) | required |

## get_mass_loss_rate

### Description:
Get fractional mass-loss rate[s] from core-collapse supernovae at input age[s]
(ejecta mass relative to IMF-averaged mass of stars at that age) [Myr ^ -1].


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ages | float or array |     stellar ages [Myr] | required |
| model | str |     model for core-collapse supernova rates (delay time distribution): 'fire2', 'fire3' | required |
| sncc_age_min | float |     minimum age for core-collapse supernova to occur [Myr] | required |
| sncc_age_break | float |     age at which rate of core-collapse supernova changes/breaks [Myr] | required |
| sncc_age_min | float |     minimum age for core-collapse supernova to occur [Myr] | required |
| element_name | str [optional] |     name of element to get fraction mass loss rate of<br />    if None or '', get fractional mass loss rate of total ejecta | required |
| metallicity | float |     metallicity (wrt Solar) of progenitor (for Nitrogen yield in FIRE-2) | required |

## get_number

### Description:
Get specific number[s] of core-collapse supernova events in input age interval[s]
[per M_sun of stars at that age].


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| age_min | float |     min age of stellar population [Myr] | required |
| age_maxs | float or array |     max age[s] of stellar population [Myr] | required |
| model | str |     model for core-collapse supernova rates (delay time distribution): 'fire2', 'fire3' | required |
| sncc_age_min | float |     minimum age for core-collapse supernova to occur [Myr] | required |
| sncc_age_break | float |     age at which rate of core-collapse supernova changes/breaks [Myr] | required |
| sncc_age_min | float |     minimum age for core-collapse supernova to occur [Myr] | required |

## get_rate

### Description:
Get specific rate[s] of core-collapse supernova events at input age[s]
[Myr ^ -1 per M_sun of stars at that age].

FIRE-2
    Rates are from Starburst99 energetics: get rate from overall energetics assuming each
    core-collapse supernova is 10^51 erg.
    Core-collapse supernovae occur from 3.4 to 37.53 Myr after formation:
        3.4 to 10.37 Myr:    rate / M_sun = 5.408e-10 yr ^ -1
        10.37 to 37.53 Myr:  rate / M_sun = 2.516e-10 yr ^ -1


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ages | float or array |     age[s] of stellar population [Myr] | required |
| model | str |     model for core-collapse supernova rates (delay time distribution): 'fire2', 'fire3' | required |
| sncc_age_min | float |     minimum age for core-collapse supernova to occur [Myr] | required |
| sncc_age_break | float |     age at which rate of core-collapse supernova changes/breaks [Myr] | required |
| sncc_age_min | float |     minimum age for core-collapse supernova to occur [Myr] | required |

## init SupernovaCCClass

### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| model | str |     model for core-collapse supernova rates (delay time distribution): 'fire2', 'fire3' | required |
| sncc_age_min | float |     minimum age for core-collapse supernova to occur [Myr] | required |
| sncc_age_break | float |     age at which rate of core-collapse supernova changes/breaks [Myr] | required |
| sncc_age_min | float |     minimum age for core-collapse supernova to occur [Myr] | required |

## _get_rate

## _parse_model

### Description:
Parse input model.


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| model | str |     model for rate (delay time distribution):<br />        'fire2' or 'mannucci' (FIRE-2 default), 'fire3' (FIRE-3 default), 'maoz' (power law) | required |
| age_min | float |     minimum age for WD supernova to occur [Myr] | required |

## get_mass_loss

### Description:
Get fractional mass loss[es] from WD supernovae in input age interval[s]
(ejecta mass relative to IMF-averaged mass of stars at that age).


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| age_min | float |     min age of stellar population [Myr] | required |
| age_maxs | float or array |     max age[s] of stellar population [Myr] | required |
| model | str |     model for rate (delay time distribution):<br />        'fire2' or 'mannucci' (FIRE-2 default), 'fire3' (FIRE-3 default), 'maoz' (power law) | required |
| snwd_age_min | float |     minimum age for WD supernova to occur [Myr] | required |
| element_name | str [optional] |     name of element to get fractional mass loss of<br />    if None or '', get mass loss of total ejecta | required |

## get_mass_loss_rate

### Description:
Get fractional mass loss rate[s] from WD supernovae in input age interval[s]
(ejecta mass relative to IMF-averaged mass of stars at that age) [Myr ^ -1].


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ages | float or array |     stellar age[s] [Myr] | required |
| model | str |     model for rate (delay time distribution):<br />        'fire2' or 'mannucci' (FIRE-2 default), 'fire3' (FIRE-3 default), 'maoz' (power law) | required |
| snwd_age_min | float |     minimum age for WD supernova to occur [Myr] | required |
| element_name | str [optional] |     name of element to get fractional mass loss of<br />    if None or '', get mass loss of total ejecta | required |

## get_number

### Description:
Get specific number[s] of WD supernova events in input age interval[s]
[per M_sun of stars at that age].


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| age_min | float |     min age of stellar population [Myr] | required |
| age_maxs | float or array |     max age[s] of stellar population [Myr] | required |
| model | str |     model for rate (delay time distribution):<br />        'fire2' or 'mannucci' (FIRE-2 default), 'fire3' (FIRE-3 default), 'maoz' (power law) | required |
| snwd_age_min | float |     minimum age for WD supernova to occur [Myr] | required |

## get_rate

### Description:
Get specific rate[s] of WD supernova events [Myr ^ -1 per M_sun of stars at that age].

FIRE-2
    rates are from Mannucci, Della Valle, & Panagia 2006, for a delayed population
    (constant rate) + prompt population (Gaussian), starting 37.53 Myr after formation:
    rate / M_sun = 5.3e-14 + 1.6e-11 * exp(-0.5 * ((star_age - 5e-5) / 1e-5) ** 2) yr ^ -1

FIRE-3
    power-law model from Maoz & Graur 2017, starting 44 Myr after formation
    normalized to 1.6 events per 1000 Msun per Hubble time:
    rate / M_sun = 2.67e-13 * (star_age / 1e6) ** (-1.1) yr ^ -1


### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ages | float |     age of stellar population [Myr] | required |
| model | str |     model for WD supernova rate (delay time distribution):<br />        'fire2' or 'mannucci' (FIRE-2 default), 'fire3' (FIRE-3 default), 'maoz' (power law) | required |
| snwd_age_min | float |     minimum age for WD supernova to occur [Myr]<br />    decreasing to 10 Myr increases total number by ~50%,<br />    increasing to 100 Myr decreases total number by ~50% | required |

## init SupernovaWDClass

### Parameters:


| Name | Type | Description | Default |
| --- | --- | --- | --- |
| model | str |     model for rate (delay time distribution):<br />        'fire2' or 'mannucci' (FIRE-2 default), 'fire3' (FIRE-3 default), 'maoz' (power law) | required |
| age_min | float |     minimum age for WD supernova to occur [Myr] | required |
