# ---------------------------------------------------------------------------
# GEOCODE COUNTRY DATA 
# Author: Grace Johnson
# Description: This program sets the environment and uses a function to
# geocode country data based on country name. Any csv with a field of
# country names can be input and will be output to a feature class of
# country borders. The user defines the input csv file, address locator,
# the field to complete the geocode on and the country borders shapefile
# to join the data to. 
# ---------------------------------------------------------------------------

import arcpy

## Set the environment
arcpy.env.workspace = "\\\\Mac\\Home\\Desktop\\ArcGIS II\\Exercise 5\\Country_Geocoding.gdb"
arcpy.env.overwriteOutput = True

## Input Variables
Country_locator = "\\\\Mac\\Home\\Desktop\\ArcGIS II\\Exercise 5\\Country_Geocoding.gdb\\Country_locator"
Country_Borders = "\\\\Mac\\Home\\Desktop\\ArcGIS II\\Exercise 5\\Country_Geocoding.gdb\\Country_Borders"
input_data = "Coal_Prod_1990.csv"
Geocode_Field = "Country"

def geocodeCountries(inCSV, inLocator, inField, inCountryBorders):
    '''This function geocodes country data, completes a spatial join, and outputs the data'''
    '''to a country shapefile. The input address locator and country borders feature class'''
    '''are packaged in the workspace environment File Geodatabase "Country_Geocoding.gdb"'''
    '''The four input arguments for the function consist of the input variables listed'''
    '''before the function. The user must identify the input csv (input_data) and field'''
    '''the geocode will be based on (Geocode_Field).'''

    # Geocoding input data based on single input (country names)
    Field = "'Single Line Input' %s VISIBLE NONE" %(Geocode_Field)
    Geocoded_Points = "\\\\Mac\\Home\\Desktop\\ArcGIS II\\Exercise 5\\Country_Geocoding.gdb\\Geocoded_Points"
    arcpy.GeocodeAddresses_geocoding(inCSV, inLocator, Field, Geocoded_Points, "STATIC")

    # Spatial Join between country borders and geocoded points
    Join_Output = "\\\\Mac\\Home\\Desktop\\ArcGIS II\\Exercise 5\\Country_Geocoding.gdb\\Join_Output"
    arcpy.SpatialJoin_analysis(inCountryBorders, Geocoded_Points, Join_Output, "JOIN_ONE_TO_ONE", "KEEP_ALL", "NAME \"NAME\" true true false 50 Text 0 0 ,First,#,\\\\Mac\\Home\\Desktop\\ArcGIS II\\Exercise 5\\Country_Geocoding.gdb\\Country_Borders,NAME,-1,-1;Shape_Length \"Shape_Length\" false true true 8 Double 0 0 ,First,#,\\\\Mac\\Home\\Desktop\\ArcGIS II\\Exercise 5\\Country_Geocoding.gdb\\Country_Borders,Shape_Length,-1,-1;Shape_Area \"Shape_Area\" false true true 8 Double 0 0 ,First,#,\\\\Mac\\Home\\Desktop\\ArcGIS II\\Exercise 5\\Country_Geocoding.gdb\\Country_Borders,Shape_Area,-1,-1;Status \"Status\" true true false 1 Text 0 0 ,First,#,\\\\Mac\\Home\\Desktop\\ArcGIS II\\Exercise 5\\Country_Geocoding.gdb\\Geocoded_Points,Status,-1,-1;Score \"Score\" true true false 0 Double 2 21 ,First,#,\\\\Mac\\Home\\Desktop\\ArcGIS II\\Exercise 5\\Country_Geocoding.gdb\\Geocoded_Points,Score,-1,-1;Match_type \"Match_type\" true true false 2 Text 0 0 ,First,#,\\\\Mac\\Home\\Desktop\\ArcGIS II\\Exercise 5\\Country_Geocoding.gdb\\Geocoded_Points,Match_type,-1,-1;Match_addr \"Match_addr\" true true false 120 Text 0 0 ,First,#,\\\\Mac\\Home\\Desktop\\ArcGIS II\\Exercise 5\\Country_Geocoding.gdb\\Geocoded_Points,Match_addr,-1,-1;X \"X\" true true false 0 Double 6 25 ,First,#,\\\\Mac\\Home\\Desktop\\ArcGIS II\\Exercise 5\\Country_Geocoding.gdb\\Geocoded_Points,X,-1,-1;Y \"Y\" true true false 0 Double 6 25 ,First,#,\\\\Mac\\Home\\Desktop\\ArcGIS II\\Exercise 5\\Country_Geocoding.gdb\\Geocoded_Points,Y,-1,-1;Xmin \"Xmin\" true true false 0 Double 6 25 ,First,#,\\\\Mac\\Home\\Desktop\\ArcGIS II\\Exercise 5\\Country_Geocoding.gdb\\Geocoded_Points,Xmin,-1,-1;Xmax \"Xmax\" true true false 0 Double 6 25 ,First,#,\\\\Mac\\Home\\Desktop\\ArcGIS II\\Exercise 5\\Country_Geocoding.gdb\\Geocoded_Points,Xmax,-1,-1;Ymin \"Ymin\" true true false 0 Double 6 25 ,First,#,\\\\Mac\\Home\\Desktop\\ArcGIS II\\Exercise 5\\Country_Geocoding.gdb\\Geocoded_Points,Ymin,-1,-1;Ymax \"Ymax\" true true false 0 Double 6 25 ,First,#,\\\\Mac\\Home\\Desktop\\ArcGIS II\\Exercise 5\\Country_Geocoding.gdb\\Geocoded_Points,Ymax,-1,-1;Addr_type \"Addr_type\" true true false 20 Text 0 0 ,First,#,\\\\Mac\\Home\\Desktop\\ArcGIS II\\Exercise 5\\Country_Geocoding.gdb\\Geocoded_Points,Addr_type,-1,-1;ARC_Single_Line_Input \"Key\" true true false 100 Text 0 0 ,First,#,\\\\Mac\\Home\\Desktop\\ArcGIS II\\Exercise 5\\Country_Geocoding.gdb\\Geocoded_Points,ARC_Single_Line_Input,-1,-1;Country \"Country\" true true false 8000 Text 0 0 ,First,#,\\\\Mac\\Home\\Desktop\\ArcGIS II\\Exercise 5\\Country_Geocoding.gdb\\Geocoded_Points,Country,-1,-1;Value \"Value\" true true false 8 Double 0 0 ,First,#,\\\\Mac\\Home\\Desktop\\ArcGIS II\\Exercise 5\\Country_Geocoding.gdb\\Geocoded_Points,Value,-1,-1", "INTERSECT", "", "")


## Call the function
geocodeCountries(input_data, Country_locator, Geocode_Field, Country_Borders)
print "Your input data has been geocoded and joined with spatial data" 
