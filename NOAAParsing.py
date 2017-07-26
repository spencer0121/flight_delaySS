# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 23:21:47 2017

@author: spencershores
"""


#####################
##General Set up
#####################

#Import Libraries
import os


#User Variables
#user="mike"
user="spencer"

#Set Directory
if user=="mike":
    os.chdir(r"C:\Users\Mike Shores\Desktop")
else:
    os.chdir("/Users/spencershores/Documents/GitHub/flight_delaySS")
    

#####################
##Define Functions
#####################

#Function to parse precipitation variables (pg. 12 of dictionary) 
def precip_vars(start_location,line):
    percip_periodh= line[start_location+3:start_location+5]
    percip_depth= line[start_location+5:start_location+9]
    percip_condition_code= line[start_location+9:start_location+10]
    percip_quality_code= line[start_location+10:start_location+11]
    return(percip_periodh,percip_depth,percip_condition_code,percip_quality_code)



#####################
##Parse File
#####################

#Open Files I will use

usingfile=open("725030-14732-2016","r")
results= open("results.csv", "w")

#Get 1 line

myline=usingfile.readline()   

for line in usingfile.readlines():
    if line[15:23]=='20160316' and line[23:27]> '1300':
        myline=line
        break

#Parse mandatory data

additional_characters= myline[0:4]
master_station = myline[4:10]
wban_identifer = myline[10:15]
observation_date = myline[15:23]
observation_time = myline[23:27]
data_source = myline[27:28]
latitude = myline[28:34]
longitude = myline[34:41]
report_type = myline[41:46]
elevation_demension = myline[46:51]
call_letter = myline[51:56]
meteorlogicial_point = myline[56:60]
wind_angle = myline[60:63]
wind_direction_quality = myline[63:64]
wind_observation_type = myline[64:65]
wind_speed = myline[65:69]
speed_quality = myline[69:70]
ceiling_height = myline[70:75]
ceiling_quality = myline[75:76]
ceiling_determination = myline[76:77]
cavok = myline[77:78]
visability_distance = myline[78:84]
visability_quality = myline[84:85]
visibility_variability = myline[85:86]
quality_variability = myline[86:87]
air_temp = myline[87:92]
air_temp_quality = myline[92:93]
dew_point_temp = myline[93:98]
dew_point_quality = myline[98:99]
sea_level_pressure= myline[99:104]
sea_level_quality= myline[104:105]

#Split line to be only additional data
add_info= myline[105:]

#Define entire list of possible additional data variables
percip_periodh=''
percip_depth=''
percip_condition_code=''
percip_quality_code=''

#Function to parse additional data
def additional_info(add_info):
    #Iterate through precipitation variables (pg. 12 of dictionary)
    for current_prefix in ['AA1','AA2','AA3','AA4']:
        aa_loc= add_info.find(current_prefix)
        if aa_loc ==-1:
            pass
        else:
            global percip_periodh,percip_depth,percip_condition_code,percip_quality_code
            percip_periodh,percip_depth,percip_condition_code,percip_quality_code=precip_vars(start_location=aa_loc,line=add_info)
    
    #Information about precipitation observations (pg. 14 of dictionary)
    AC1_loc= add_info.find('AC1')
    if AC1_loc == -1:
        pass
    else:
        observed_duration= add_info[AC1_loc+3:AC1_loc+4]
        character_observed= add_info[AC1_loc+4:AC1_loc+5]
    AG1_loc= add_info.find('AG1')
    if AG1_loc == -1:
        pass
    else:
        report_v_weather= add_info[AG1_loc+3:AG1_loc+4]
        three_hour_rain_total= add_info[AG1_loc+4:AG1_loc+7]
    AJ1_loc= add_info.find('AJ1')
    if AJ1_loc == -1:
        pass
    else:
        snow_on_ground= add_info[AJ1_loc+3:AJ1_loc+7]
        snow_condition= add_info[AJ1_loc+7:AJ1_loc+8]
        snow_quality= add_info[AJ1_loc+8:AJ1_loc+9]
    AL1_loc= add_info.find('AL1')
    if AL1_loc ==-1:
        pass
    else:
        snow_periodh= add_info[AL1_loc+3:AL1_loc+5]
    AL2_loc= add_info.find('AL2')
    if AL2_loc ==-1:
        pass
    else:
        percip_periodh= add_info[AL2_loc+3:AL2_loc+5]
        snow_depth= add_info[AL2_loc+5:AL2_loc+8]
    AL3_loc= add_info.find('AL3')
    if AL3_loc ==-1:
        pass
    else:
        snow_periodh= add_info[AL3_loc+3:AL3_loc+5]
        snow_depth= add_info[AL3_loc+5:AL3_loc+8]
        snow_condition_code= add_info[AL3_loc+8:AL3_loc+9]
    AL4_loc= add_info.find('AL4')
    if AL4_loc ==-1:
        pass
    else:
        snow_periodh= add_info[AL4_loc+3:AL4_loc+5]
        snow_depth= add_info[AL4_loc+5:AL4_loc+8]
        snow_condition_code= add_info[AL4_loc+8:AL4_loc+9]
        snow_quality_code= add_info[AL4_loc+9:AL4_loc+10]
    return percip_periodh


#Call function to split additional info if it exists
if len(add_info)>0:
    additional_info(add_info=add_info)

#Join all variables together into 1 line
output_line=",".join(list(<list of your variables>))

#Write Line to output
results.write(output_line)

#Close files
usingfile.close()
results.close()