# Design Project #

* Generate Test Files
    - random
    - random with seed
* Transfer csv to JSON file

## Environment Setup

* python3/python2
* numpy

## Parameter
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
  

## ToDo
- [x] Generate for python code
    * Generate param json file
    * Generate configure json file
    * Should be able to take input set
- [x] Generate for new format
    * a new config file is added
- [ ] Transfer the csv to json, real data

## Generate Test Json
* Choose mode:
    * mode 1: random
    * mode 2: with seed

## Need to improve
1. generate location grid not square
