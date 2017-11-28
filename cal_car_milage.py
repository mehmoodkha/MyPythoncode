#!/usr/bin/python

print("To calculate milage we need distance covered and fuel used")

start_point=input("Enter starting point :")
end_point=input("Enter end Point :")
fuel=input("Fuel Consumption in Liters :")

milage=(end_point-start_point)/fuel

print("Milage is :"),milage
