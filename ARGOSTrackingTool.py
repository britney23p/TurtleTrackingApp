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

#Create a variable pointing to the data file
file_name = 'data/raw/sara.txt'

#Create a file object from the filename
file_object = open(file = file_name,mode='r')

#Read contents of file into a list
lineString = file_object.readline()


#Extract one data line into a variable
while lineString:
    
    #Check to see if the lineString is a data line
    if lineString[0] == "#" or lineString[0] == 'u':
        lineString = file_object.readline()
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
    ob_lc = lineData[4]       # Observation Location Class
    obs_lat = lineData[6]     # Observation Latitude
    obs_lon = lineData[7]     # Observation Longitude
    
    # Print information to the use
    print (f"Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}")

    #move to the next line in the file
    lineString = file_object.readline()

#Close the file object
file_object.close()
