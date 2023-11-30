# stellarutil
Stellarutil is a python utility package for gizmo_analysis. It was made specifically for the Coral Wheeler’s Cal Poly Pomona Astronomy Research Team, known as CPP FIRE Squad. The team conducts FIRE (Feedback In Realistic Environments) simulations to try to discover and comprehend the dwarf galaxies that surround the Milky Way. Stellarutil is built on top of gizmo_analysis to provide a more streamlined programming experience for the team’s researchers. 

To set up your development environment, click [here](https://docs.google.com/document/d/1k4cySN2KbI2uWVRci_68NunSoVHhqr92PvQBMSoT3m4/edit?usp=sharing)!

## Installation

First install dependencies:
```shell
pip3 install astropy matplotlib numpy h5py pandas scipy --user
```
Then, run the following command:
```shell
pip3 install git+https://github.com/CPP-FIRE-Squad/stellarutil.git --user
```

## Documentation
 - [Here](./documentation/stellarutil.md) is the documentation for stellarutil.
 - [Here](./documentation/gizmo_analysis/) is the documentation for gizmo_analysis.



## Sample Usage
```python 
from stellarutil import Simulation

# These are the two ways to access a simulation
# 1) via name - must adhere to folder structure
m10v_res250 = Simulation('m10v_res250md', species=['star']) 
# 2) or you can specify the path of each item manually if you do not want to use the proper structure
m10v_res250 = Simulation(
    simulation_directory = '../data/m10v_res250md',
    snapshot_directory='output',
    ahf_path='../data/m10v_res250md/snapshot_600.z0.000.AHF_halos',
)

# Getting help
m10v_res250.help()

# Print hubble constant
print(m10v_res250.h)
# Print particle fields
print(m10v_res250.particles.keys())
print(m10v_res250.particles['star'].keys())
# Print field
print(m10v_res250.get_field('nstar'))
# Get a halo and print its mass
halo = m10v_res250.get_halo()
print(halo.mass)
# Get a list of ages and x pos of each star in the halo
ages = [star.a for star in halo.stars]
# Center the halo on the halo at index 1
halo.center_on(2)
# Filter all stars in the halo at 15%
halo.restrict_percentage(15)
```
