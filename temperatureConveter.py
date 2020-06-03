#!/usr/bin/python
##################################################
## Program that takes temperature values in Celsius
# and converts them to Fahrenheit
##################################################
## Author: Tanyaradzwa Matasva
## Course: CPSC-442-11
## Instructor: Dr Abdelshakour Abuzneid
## School: University of Bridgeport
##################################################
import os

print("Celsius to Fahrenheit")
#prompt user to enter temperature in celcius
tempC = int(input("Enter temperature in Celsius : "))
#convert temperature to fahrenheit
tempF = tempC*1.8+32

#display result
print(str(tempF)+" Fahrenheit")