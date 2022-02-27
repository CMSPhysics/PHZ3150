import numpy as np
import pandas as pd
import math 

def planet_tour(start_location, destination_location):
    """Function takes the start location and destination location of the trip and returns the travel time, distance, and refuel stops.
    Input: start_location, destination_location
    Outpu: time_years, time_days, time_hours, time_minutes, distance_for_traveller, refuel_stops"""
    
    planets_and_moons = np.array(
        ['Mercury', 'Venus', 'Earth', 'Moon', 'Ceres', 'Mars', 'Jupiter', 'Io', 'Europa', 'Saturn', 'Titan', 'Neptune',
         'Pluto', 'Charon'])
    
    space_distance_data1 = np.loadtxt('../demos/solar_system_date_1.dat')
    space_distances_date2 = np.loadtxt('../demos/solar_system_date_2.dat')
    space_distances_date3 = np.loadtxt('../demos/solar_system_date_3.dat')
    
    df = pd.DataFrame(space_distance_data1, columns=planets_and_moons, index=planets_and_moons)
    distance_for_traveller = df.loc[start_location, destination_location]

    
    time_total = distance_for_traveller / 0.001
    
    time_years = int((time_total / 24)*(1/365))
    d = (((time_total/365)-time_years)*365)/24
    time_days = int(d)
    h = (d-time_days)*24
    time_hours = int(h)
    m = (h-time_hours)*60
    time_minutes = int(m)
    
    refuel_stops = int(math.ceil(distance_for_traveller*(1/0.65)))  
    
    print("The distance from", start_location, "to", destination_location, "is", distance_for_traveller, "AU", "and this trip will take", time_years, "years", time_days, "days,", time_hours, "hours, and", time_minutes, "minutes")
    print()
    print("You will require", refuel_stops, "refuelling stops")
   
    return time_years, time_days, time_hours, time_minutes, distance_for_traveller, refuel_stops