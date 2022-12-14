#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Britney Pepper (bep28@duke.edu)
# Date:   Fall 2022
#--------------------------------------------------------------

# Ask the user for a date, specifying the format
user_date = input("Enter a date (M/D/YYYY):")

#Create a variable pointing to the data file
file_name = 'data/raw/sara.txt'

#Create a file object from the filename
file_object = open(file = file_name,mode='r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file object
file_object.close()

#Create empty dictionaires 
date_dict = {}
location_dict = {}

#Extract one data line into a variable
for lineString in line_list:
    
    #Check to see if the lineString is a data line
    if lineString[0] == "#" or lineString[0] == "u":
        continue
    #Can Also use
    # if lineString[0] in ('#','u'):
        #continue
    #Or use
    # if not lineString [0] in ('#','u'):
        #and have everything else tabbed under this
    
    # Use the split command to parse the items in lineString into a list object
    lineData = lineString.split()
    
    # Assign variables to specfic items in the list
    record_id = lineData[0]   # ARGOS tracking record ID
    obs_date = lineData[2]   # Observation date
    obs_lc = lineData[4]       # Observation Location Class
    obs_lat = lineData[6]     # Observation Latitude
    obs_lon = lineData[7]     # Observation Longitude
    
    #Add items to dictionaries, if lc criteria is met
    if obs_lc in ('1', '2', '3'): 
        #Add items to dictionaires
        date_dict[record_id] = obs_date
        location_dict[record_id] = (obs_lat, obs_lon)

#Create list to hold keys
matching_keys = []
    
# Loop through all key, value pairs in the date_dictionary
for the_key, the_value in date_dict.items():
    #See if the date (the value) matches the user date
    if the_value == user_date:
        #Add matching keys to list
        matching_keys.append(the_key)
        
# Report whether no keys were found
if len(matching_keys) == 0:
    print(f"Sara was not located on {user_date}")
        
#Reveal locations for each key in matching_keys
for matching_key in matching_keys:
    obs_lat, obs_lon = location_dict[matching_key]
    print(f"Record {matching_key} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {user_date}")
    