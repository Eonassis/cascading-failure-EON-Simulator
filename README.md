# cascading-failure-EON-Simulator
cascading-failure-EON-Simulator

# Elastic Optical Network Simulator

This simulator run arrival requests on an Elastic Optical Network Simulator cascading failure.

## Getting Started

These instructions will guide you to run this simulator.

### Files

'EON_SIM.py': It contains EON simulator, It defines the parameters of the simulator, It starts simulation of EON

### Installing

It requires: python 3, networkx , numpy, decorator

######

 sys.version
'3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)]'

 print(networkx.__version__)
2.8.8

print(simpy.__version__)
4.0.2



## Commands Verify requires

import sys

sys.version

import networkx

print(networkx.\_\_version\_\_)

import simpy

print (simpy.\_\_version\_\_)



### Run the simulator

python EON_SIM.py

### Results

Results of the simulations are put in the folder out according to the choose topology

