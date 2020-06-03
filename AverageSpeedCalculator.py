#!/usr/bin/python
##################################################
## Program that calculates the average speed for
## running a race
##################################################
## Author: Tanyaradzwa Matasva
## Course: CPSC-442-11
## Instructor: Dr Abdelshakour Abuzneid
## School: University of Bridgeport
##################################################

distance_miles = (10/1.609)
maxTime = ((1*3600)+(5*60)+42)

time_per_mile = maxTime/distance_miles

minutes = int(time_per_mile/60)
seconds = time_per_mile % 60

print("Average pace : %02d minutes " % minutes+"%02d seconds per mile" % seconds)

speed_per_second=distance_miles/maxTime
averageSpeed=speed_per_second*3600

print("Average speed : %.2f miles/hour"%averageSpeed)
