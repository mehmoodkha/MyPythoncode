#!/usr/bin/python

print('''
            ___________
         /   |    |    |
  ______/____|____|    |
 /      |    -|        |
/_______|_____|_______/= zzzzz
   \__/         \__/


''')
print("To calculate milage we need distance covered and fuel used")

start_point=input("Enter starting point :")
end_point=input("Enter end Point :")
fuel=input("Fuel Consumption in Liters :")

milage=(end_point-start_point)/fuel

print("\nMilage is :"),milage


print("############################################"),

print("$$$ Lets calculate stops for fueling while traveling from bangalore to goa $$$")
tank_size=input("\nWhat is the capacity of car's fuel tank :")
full_tank_run_in_km=tank_size*milage

distance=input("What is the distance from bangalore to goa: ")

no_of_stops=distance/full_tank_run_in_km

print(" Number of stops for fueling is" ), no_of_stops

