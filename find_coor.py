# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 13:12:27 2019

@author: Peter Pranata
"""
"""
Goal:
    To create a map with city locations and their respective temperatures
    - Each city should be represented by a circle, color coded to reflet cold (blue) or warm (red)
    - Please convert any .xls or any data table to .csv format if it's not done so
    - Install proper libraries as listed below
"""
# Please install the proper modules 
# pip install opencage 
# pip install geocoder
# Please SAVE AS the temperature file to a .CSV file before proceeding

from opencage.geocoder import OpenCageGeocode
from pprint import pprint

import geocoder
import csv
import pandas as pd

# Open initial csv file that consists of the city you want to find the coordinates of
# We will create the 2 columns first for their latitude and longtitude
# Reference: Python documentation = https://docs.python.org/3/library/csv.html

with open('city_temperatures.csv', 'r') as csvinput:
    with open('city_temp_raw.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)
        
        all = []
        row = next(reader)
        row.append('lat')
        row.append('lon')
        all.append(row)
        
        for row in reader:
            row.append(row[0])
            all.append(row)
            
        writer.writerows(all)
# Now, we have the 2 new columns to store the latitude and longtitude of each city
# We will use opencage geocoder to retrieve the coordinates
# To get results from geocoder, please be sure to register and get an API key first
# Get API from:
    # Google Maps API
    # Opencage
# They are free but need it to access Google Maps data

df = pd.read_csv('city_temp_raw.csv')
c = 0 # Sets the initial row to get the coordinates of

# We will now loop through the number of cities/location as based on the file
# Use the length of the city as the parameter for range()
# Reference: https://opencagedata.com/tutorials/geocode-in-python

for c in range(0, len(df['City'])):
    result = geocoder.opencage(df['City'][c], key='f9eb598460d74976b143b0b4c99bbe13')
    y = result.latlng[0]
    x = result.latlng[1]
    df.set_value(c, 'lat', y)
    df.set_value(c, 'lon', x)
    del x
    del y
    c += 1
    
# We will now save the result of the dataframe to update the coordinates 
# You can save the file name to anything to want, but make sure to open this file
    # ...for the actual plotting as it contains the coordinates
df.to_csv('city_temp.csv', index=False)


