# Design Project #

* Generate Test Files
    - random
    - random with seed
* Transfer csv to JSON file

## Environment Setup

* python2.7
* numpy

## Directory
- Version0: Python Version Code
    - run with ``python ArbovirusSimulator.py *.params``
    - use to compare with the c++ version outcomes
- Version1: Generate Test Data used in python version
    - ForTest: Randomly generate data
        - mode 1: random
        - mode 2: random with seed
    - Parse: Transfer data from csv to json
- Version3: Generate Test Data for c++ version with new format
    - ForTest_eg: Example of new format
    - ForTest: Randomly generate test data
        - mode 1: random
        - mode 2: random with seed
    - Parse: Transfer data from csv suitable for c++ version
        - note: to be able to use in python version, we can just copy the location and host file for python code to use


## Parameters
* Parameter for python version random test file:
    - location:
        * line*line the grid is a square
        * v-capacity [20]
        * v-immature
        * v-state [20,0,0,0]
    - host
        * number of hosts
        * number of locations
        * number of hubs
        * [S,E,I,R] initialize
        * rate of people without hubs
        * note:
          - number of hub used to generate a list of hubs, then pick up the hub from hub id
          - one hub can contain 2 or more people
          - some people may do not have hub, just stay home
    - param
        * all the parameters should be able to redefined
    - random seed 
        * set the seed to generate the same test file
    - test series name
        * set the test output file name
    - note:
        * all the parameters metioned above can be set within the scenario.py file
  
* Parameter for python version to transform csv 
    - host 
        * initatilize rate for [S,E,I,R]
        * USE random seed or not
    - location
        * capability of the location 
        * default: 1 -> 20, 2->40, other->10
    - test series name
        * set the test output file name
    
## Run

1. In the scenario.py or parse.py file, we can edit the config at the top of the file
2. after edit it with the parameters you want(meanings of parameters seen above), generate it with
    * ``python scenario.py``
    * ``python parse.py``
    

## Need to improve
1. generate location grid not square
