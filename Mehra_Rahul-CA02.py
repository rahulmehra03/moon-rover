#Mehra_Rahul 201722843   October2023 CA-02.py
#Coded a calculator to determine the distance the rover has moved overall,horizontally and vertically over a given time at a given angle


import math
#input
print ("Welcome to Rahul's Moon Rover distance Calculator.")
angle_in_deg = float(input("Please enter the angle between 0 and 90 inclusive in degrees: "))
time = float(input("Please enter the total time spent travelling in seconds: "))

#Proccess and calculations
angle_in_rad = math.radians(angle_in_deg)
speed = 1.5
battery_usage = 2.7
distance_travelled = (speed*time)
sina = math.sin(angle_in_rad)
cosa = math.cos(angle_in_rad)
horizontal_distance = (sina*distance_travelled)
vertical_distance = (cosa*distance_travelled)
battery_used = (battery_usage*time)
battery_remaining = (100-battery_used)
maximum_time = (100/2.7)
maximum_distance = (maximum_time*speed)
#Here I have implemented 2 variables called maximum distance and maximum time to help with the logic of my if statements
#The maximum time is the time taken for the battery to deplete while at the constant speed of 1.5 m/s
#The maximum distance is the maximum distacne the rover can travel from full battery

#output
print ("Thankyou. Here are your results:")
print ("Angle used:",angle_in_deg,"degrees")
print ("Time of travel:",time,"s")
print (f"Distance travelled: {distance_travelled:.2f}","m")
print (f"Horizontal movement: {horizontal_distance:.2f}","m")
print (f"Vertical movement: {vertical_distance:.2f}","m")
#output is formatted to 2dp for better UI
if (distance_travelled > maximum_distance):
    print("Battery Usage: 100%")
    print("Battery remaining: 0%")
    print(f"Destination not reached,the rover has run out of battery after travelling {maximum_distance:.2f}","m")
elif(battery_used > battery_remaining):
    print ("Battery usage:",battery_used,"%")
    print ("Battery remaining:",battery_remaining,"%")
    print ("Destination reached however, battery levels are insufficient to return to base.")
else:
    print ("Battery usage:",battery_used,"%")
    print ("Battery remaining:",battery_remaining,"%")
    print ("Destination reached.Battery levels are sufficient to return to base.")
#For the if statement if the distance travlled calculated exceeds the maximum distance the battery mustve run out so user is informed
#for the elif statement if the battery used is greater than the battery remaining this must meen the rover has arrived but does not have enough battery to return hence the user is informed
#If none of the above two scenarios apply we are left with the else statment that informs the user rover has arrived and has enough battery to return

#Testing    angle     time        expected result            actual result              comments          
#1           50        25       elif statement activated    elif statement activated      ok
#2           45.5      62       if statement activated      if statement activated        ok
#3           82        17      else statement activated     else statment activated       ok
#4           97        86            error                       error               vertical distance negative as angle was outside of parameter 
#5           x         y             error                        error               x and y cannot be converted to floats


    



       
