#!/usr/bin/python
##################################################
## Program that calculates the wholesale price of 40
## Books
##################################################
## Author: Tanyaradzwa Matasva
## Course: CPSC-442-11
## Instructor: Dr Abdelshakour Abuzneid
## School: University of Bridgeport
##################################################

pricePerBook=2500
discountAmount=pricePerBook*.1
first5_ShippingCost=200
shippingCost=2.75

subTotal=(pricePerBook*40)-(discountAmount*40)
totalCents=(subTotal+(5*first5_ShippingCost)+(shippingCost*(40-5)))
total=totalCents/100.0

print("The wholesale price for 40 Books is : $ %.2f"%total)
