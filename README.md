# Design Project #

* Generate Test Files
    - random
    - random with seed
* Transfer csv to JSON file

## Environment Setup
    * python3/python2
    * numpy

## Parameter
* Parameter for file:
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
    - param
        * all the parameters should be able to redefined

## ToDo
* Generate param json file
* Generate configure json file
* Should be able to take input set

## Generate Test Json

* Choose mode:
    * mode 1: random
    * mode 2: with seed

## Proposal
1. generate location grid not square
