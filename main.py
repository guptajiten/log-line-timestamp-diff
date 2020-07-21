#!/usr/bin/env python
import os
import re
from datetime import datetime

regStart = "Start request"
regEnd = "Finish request"
regCompile = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{3}'
filePath = "mylogs.log" 
lastTime = ""
counter = 0

with open(filePath, 'r') as f:
    for line in f:   
        start_index = line.find(regStart)
        end_index = line.find(regEnd)
        
        if start_index > 0:
          #print("Request Start : " + line)
          print ("##########################START#############################")
          objTime = re.findall(regCompile,line)
          lastTime = objTime[0]
          
          
        if len(lastTime) != 0 and end_index > 0:
          #print("Request Finish : " + line)  
          counter = counter + 1
          
          objTime = re.findall(regCompile,line)
          currentTime = objTime[0]
          
          datetime_object_lastTime = datetime.strptime(lastTime, '%Y-%m-%d %H:%M:%S,%f')
          datetime_object_currentTime = datetime.strptime(currentTime, '%Y-%m-%d %H:%M:%S,%f')
          t_delta = datetime_object_currentTime - datetime_object_lastTime
          print ("Request served : "+ str(counter) +" and duration : " + str(t_delta))
          print ("##########################END##############################")
          lastTime = ""
f.closed