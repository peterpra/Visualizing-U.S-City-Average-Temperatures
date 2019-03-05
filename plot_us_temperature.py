# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 02:14:54 2019

@author: Peter Pranata
"""
"""
***This code will create a plotly map for the .csv file that was created by the find_coor.py script

Please ensure that you have an account with plot.ly before proceeding

** Code modified and taken from:
https://plot.ly/python/bubble-maps/ for the sample code

"""

# Please login to plot.ly before running the code
# You need to have access first using their free registration

import plotly.plotly as py
import pandas as pd

df = pd.read_csv('city_temp.csv')
df.head()

# Used template sample given from Plotly website

df['text'] = df['City'] + '<br>Temperature ' + df['Temp'].astype(str)+' \xb0F'
limits = [(0,10),(11,20),(21,30),(31,40),(41,50)]
colors = ["rgb(255,51,0)","rgb(255,153,51)","rgb(255,204,102)","rgb(204,255,255)","rgb(102,204,255)", "rgb(0,102,255)"]
cities = [] # Creates an empty list for later use
scale = 0.1

for i in range(len(limits)): # Loops through all the rows and assigns the value for each city
    lim = limits[i]
    df_sub = df[lim[0]:lim[1]]
    city = dict(
        type = 'scattergeo',
        locationmode = 'USA-states',
        lon = df_sub['lon'],
        lat = df_sub['lat'],
        text = df_sub['text'],
        marker = dict(
            size = df_sub['Temp']/scale,
            # sizeref = 2. * max(df_sub['pop']/scale) / (25 ** 2),
            color = colors[i],
            line = dict(width=0.5, color='rgb(40,40,40)'),
            sizemode = 'area'
        ),
        name = '{0} - {1}'.format(lim[0],lim[1]) )
    cities.append(city) # Assigns the value (temp, lat, long) of city i and loops through it


# We will now create the base layout of the map for visualization
layout = dict( 
        title = 'US City Temperatures<br>(Click legend to toggle traces)',
        showlegend = True,
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showland = True,
            landcolor = 'rgb(217, 217, 217)', # Base color for the US map
            subunitwidth=1, # These defines the gap between each state
            countrywidth=1,
            subunitcolor="rgb(255, 255, 255)", # Line color for the gaps between states
            countrycolor="rgb(255, 255, 255)"
        ),
    )
            
fig = dict(data=cities, layout=layout)
# This will open up a new tab in the browser
py.plot(fig, validate=False, filename='d3-bubble-map-temperature')
