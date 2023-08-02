# stellarutil
Stellarutil is a python utility package for: gizmo_analysis, matplotlib, astropy, and other libraries. It was made specifically for the Cal Poly Pomona Astronomy Research Team, known as CPP FIRE Squad. With the help of the aforementioned libraries, the team conducts FIRE (Feedback In Realistic Environments) simulations to try to discover and comprehend the dwarf galaxies that surround the Milky Way. Stellarutil is built on top of these libraries, namely gizmo_analysis, to provide a more streamlined programming experience for the team’s researchers. 

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

Here is the documentation for each module:
 - [Simulation](./documentation/simulation.md)
 - [Console](./documentation/console.md)
 - [Calculations](./documentation/calculations.md)
 - [Graph](./documentation/graph.md)


[Here](./documentation/gizmo_analysis/) is the documentation for gizmo_analysis:



## Sample Usage
```python 
from stellarutil.simulation import Simulation
simulation = Simulation()
# Print hubble constant
print(simulation.h)
```
