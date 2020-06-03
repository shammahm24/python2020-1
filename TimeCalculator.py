#!/usr/bin/python
##################################################
## Program that calculates the amount of time taken
##to go home with varying walking speeds
##################################################
## Author: Tanyaradzwa Matasva
## Course: CPSC-442-11
## Instructor: Dr Abdelshakour Abuzneid
## School: University of Bridgeport
##################################################

speed1 = 495
speed2 = 432
initialHour = 7
initialMinutes = 30

travellingTime_sec = speed1+(3*speed2)
travellingTime_min = travellingTime_sec/60
totalMinutes = round(initialMinutes+travellingTime_min)

if totalMinutes >= 60:
    initialHour = initialHour+1
    totalMinutes = totalMinutes-60

print("Arrival Time : "+str(initialHour)+" : %02d"%totalMinutes)