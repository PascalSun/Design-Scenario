import random
import numpy as np
import json

# This version can be used in python code

####################################
# Setup the test data              #
####################################


###################################
# Specify the test data file name #
###################################

test_data_name_set = 'test1'


##########################
# Parameter for locations#
##########################

grid_line = 150
v_capacity = 20
v_immature = 0
v_state = [v_capacity,0,0,0]


#######################
# Parameter for hosts #
#######################

host_number = 10000
location_number = grid_line*grid_line
hub_number = 10000
# initialize status for hosts with S E I R
initialize_status = [0.2,0.3,0.4,0.1] # [0.2,0.3,0.4,0.1]
host_no_hub_rate = 0.2

#######################
# Parameter for param #
#######################

param ={
  "duration"                     : 100,
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
	# To generate the param file here   #
	generate_param()


	#-----------------------------------#
	# To generate the location file here
	# Generate the input
	# par = [line of the area, capabilty, immature, v-state]
	parlocation = [grid_line,v_capacity,v_immature,v_state]
	# Generate the location data
	locations = generatelocations(parlocation[0],parlocation[1],parlocation[2],parlocation[3])
	# Generate the file
	generatelocation(locations)

	#--------------------------#
	# To generate host file here
	#Generate the input par
	# par = [num of hosts,num of locations, num of hubs, rate of different situation at initation stage, rate of people stay home with no hub]
	par = [host_number,location_number,hub_number,initialize_status,host_no_hub_rate]
	# Generate data
	hosts = generatehosts(par[0],par[1],par[2],par[3],par[4])
	# Generate file
	generate(hosts)




###################################
# Generate Hosts with 2 functions #
# generatehosts is used to generate the data
# generate is used to generate the file
def generate(hosts):
	# Generate the file
	t = open(test_data_name_set+'.hosts', 'w')
	content ='  "{}" : {{\
	\n    "location" : {},\
	\n    "i-state" : "{}",\
	\n    "home" : {},\
	\n    "hub" : {} \n }},\n'
	t.write("{ \n")
	lens = len(hosts)
	count = 0
	for k in hosts:
		if count > lens - 2:
			break
		else:
			count = count+1
		contentr = content.format(k[0],k[1],k[2],k[3],k[4])
		t.write(contentr)
	content ='  "{}" : {{\
	\n    "location" : {},\
	\n    "i-state" : "{}",\
	\n    "home" : {},\
	\n    "hub" : {} \n }}\n'
	k = hosts[lens-1]
	contentr = content.format(k[0],k[1],k[2],k[3],k[4])
	t.write(contentr)
	t.write("} ")
	t.close()

def generatehosts(hostnum,locationnum,hubnum,rate,hubhome):
	# Generate the hosts []

	# Choose the initation state of the infectious situation with different rate
	hosts = []
	elems = ['S','E','I','R']

	# A list of hub with different rates
	hubs = [-1]
	hubsrate = [hubhome]
	for k in range(hubnum):
		hubs.append(random.randint(0,locationnum))
		hubsrate.append((1-hubhome)/hubnum)

    # Generate a list of home
	home = np.random.choice(locationnum,hostnum)
	for i in range(hostnum):
		hosts.append([i,home[i],np.random.choice(elems, p=rate),home[i],np.random.choice(hubs,p=hubsrate)])
	return hosts
#end generate host
#######################################


######################################
# Generate Location with 3 functions #
# generatelocation is used to generate the file
# generatelocations is used to generate the data
# generateneighbour is used to find the neighbours for each cells
def generatelocation(locations):
	t = open(test_data_name_set+'.locations','w')
	content = ' "{}" :{{\
	\n   "coordinates": {},\
	\n   "neighbours": {},\
	\n   "hosts":{},\
	\n   "v-capacity":{},\
	\n   "v-immature":{},\
	\n   "v-state":{} \n }},\n'
	t.write("{ \n")

	lens = len(locations)
	count = 0
	for k in locations:
		if count > lens - 2:
			break
		else:
			count = count+1
		contentr = content.format(k[0],k[1],k[2],k[3],k[4],k[5],k[6])
		t.write(contentr)
	content = ' "{}" :{{\
	\n   "coordinates": {},\
	\n   "neighbours": {},\
	\n   "hosts":{},\
	\n   "v-capacity":{},\
	\n   "v-immature":{},\
	\n   "v-state":{} \n }}\n'
	k = locations[lens-1]
	contentr = content.format(k[0],k[1],k[2],k[3],k[4],k[5],k[6])
	t.write(contentr)

	t.write("}")
	t.close()


def generatelocations(line,cap,immature,state):
	locations = []
	for k in range(line):
		for j in range(line):
			location=[]
			location.append(k*line+j)
			location.append([float(100*(j+1)),float(100*(k+1))])
			location.append(generateneighbour(k*line+j,line))
			location.append([])
			location.append(cap)
			location.append(immature)
			location.append(state)
			locations.append(location)
	return locations

def generateneighbour(x,line):
	neighbours = []
	if x%line != 0:

		neighbours.append(x-1)
	if x%line != line-1:

		neighbours.append(x+1)
	if x + line < line*line:
		neighbours.append(x+line)
	if x-line > -1:
		neighbours.append(x-line)
	return neighbours

#end generate locations
############################################


#########################################
# Generate param file with one function #
def generate_param():
	param['hosts-file'] = test_data_name_set+'.hosts'
	param['locations-file'] = test_data_name_set+'.locations'
	with open(test_data_name_set+'.params', 'w') as f:
	  json.dump(param, f, ensure_ascii=False)

main()