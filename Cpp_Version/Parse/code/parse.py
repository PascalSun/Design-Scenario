from host import generate_host
from location import generate_location
import random
import numpy as np
import json

# This is the code to generate test files with new format for c++ version

####################################
# Setup the test data              #
####################################


###################################
# Specify the test data file name #
###################################

test_data_name_set = 'thisistest'


########################
# Parameter for config #
########################

test_data_config = {
  "current-cycle": 0,
  "total-cycles": 1000,
    "checkpoint": {
	"type": "cycles",
	"interval":100
  },
  
  "seed": {
	"type": "uint",
	"value": 3333333333
  }  
}

#######################
# Paramter for host   #
#######################
host_config = {
	"rate":[0.9,0.1,0,0],
	"use_seed":False,
	'the_seed':1121
}

##########################
# Parameter for location #
##########################
location_config = {
	"1":20,
	"2":40,
	"other":10
}


#######################
# Parameter for param #
#######################

param ={
  "vector-diffusion-probability" : 0.1,
  "biting-rate"                  : 1.0,
  "vector-infection-probability" : 0.1,
  "host-infection-probability"   : 0.9,
  "vector-e-to-i-rate"           : 0.5,
  "host-e-to-i-rate"             : 0.5,
  "host-i-to-r-rate"             : 0.1,
  "vector-birth-rate"            : 0.5,
  "vector-maturation-rate"       : 0.1,
  "vector-death-rate"            : 0.1
}



###################################
#          main function          #
###################################
def main():


	#-----------------------------------#
	# To generate the config file here  #
	generate_config()


	#-----------------------------------#
	# To generate the param file here   #
	generate_param()

	#===================================#
	# To transform host from host file  #
	print('Generating host file, it may take some time...')
	generate_host(test_data_name_set,host_config)


	#===================================#
	# To transform location from file   #
	print('Generating location file, it may take some time...')
	generate_location(test_data_name_set,location_config)

#########################################
# Generate param file with one function #
def generate_param():
	with open(test_data_name_set+'.params.json', 'w') as f:
	  json.dump(param, f, ensure_ascii=False)


############################################
# Generate config file within one function #
def generate_config():
	test_data_config['params-file'] = test_data_name_set+ ".params.json"
	test_data_config['hosts-file'] = test_data_name_set+ ".hosts.json"
	test_data_config['locations-file'] = test_data_name_set+ ".locations.json"
	test_data_config['datalog-file'] = test_data_name_set+ ".datalog.json"
	with open(test_data_name_set+'.config.json', 'w') as f:
	  json.dump(test_data_config, f, ensure_ascii=False)



###################
# run main function
main()
