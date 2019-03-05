# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 09:23:55 2019

@author: Peter Pranata
"""

maxTemp = -infinity
minTemp = +infinity
for i in myData:
    if (myData[i]['temp'] > maxTemp):
        maxTemp = myData[i]['temp']
    if (myData[i]['temp'] < minTemp):
        minTemp = myData[i]['temp']
        
coldestSize = 8
hottestSize = 18
for i in myData:
    myData[i]['circleSize'] = a value between coldestSize and hottestSize

for i in myData:
    myData[i]['circleColor'] = a color along the red <--> blue spectrum
    
