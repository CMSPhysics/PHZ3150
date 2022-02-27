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
    
    #Indexing and reading data from txt files 
    
    space_distance_data1 = np.loadtxt('../demos/solar_system_date_1.dat')
    space_distances_date2 = np.loadtxt('../demos/solar_system_date_2.dat')
    space_distances_date3 = np.loadtxt('../demos/solar_system_date_3.dat')
    
    df1 = pd.DataFrame(space_distance_data1, columns=planets_and_moons, index=planets_and_moons)
    distance_for_traveller1 = df1.loc[start_location, destination_location]
    df2 = pd.DataFrame(space_distances_date2, columns = planets_and_moons, index = planets_and_moons)
    distance_for_traveller2 = df2.loc[start_location, destination_location]
    df3 = pd.DataFrame(space_distances_date3, columns = planets_and_moons, index = planets_and_moons)
    distance_for_traveller3 = df3.loc[start_location, destination_location]
    
    #Finding date that will have the shortest distance of travel 
    
    travel_dates = [distance_for_traveller1, distance_for_traveller2, distance_for_traveller3]
    
    shortest_travel_day = travel_dates[0]
    
    for i in range( 1, len(travel_dates)):
        if travel_dates[i] < shortest_travel_day:
            shortest_travel_day = travel_dates[i]
            
    #Total travel time based on average speed of 0.001AU/m
        
    time_total = shortest_travel_day / 0.001
    
    #Travel time in earth years, days, hours, minutes 
    
    time_years = int((time_total / 24)*(1/365))
    d = (((time_total/365)-time_years)*365)/24
    time_days = int(d)
    h = (d-time_days)*24
    time_hours = int(h)
    m = (h-time_hours)*60
    time_minutes = int(m)
    
    #Number of refueling stops required per trip 
    
    refuel_stops = int(math.ceil(shortest_travel_day*(1/0.65)))  
    
    #Messages sent back to station regarding refueling stop locations in AU
    
    df_t = open('message_to_stations.txt', 'w')
    df_t.write('my trip starts at')
    df_t.write(start_location)
    df_t.write('and ends at')
    df_t.write(destination_location)
    df_t.write('I will need to encounter stations for \n a refueling at \n')
    for x in range(1, refuel_stops):
        y = round(0.65*x, 4)
        df_t.write(str(y))
        df_t.write('AU')
        df_t.write('\n')
    df_t.close()
    
    #Printing trip information
    
    print("The shortest distance from", start_location, "to", destination_location, "is", shortest_travel_day, "AU", "and this trip will take", time_years, "years", time_days, "days,", time_hours, "hours, and", time_minutes, "minutes")
    print()
    print("You will require", refuel_stops, "refuelling stops!")
   
    return time_years, time_days, time_hours, time_minutes, shortest_travel_day, refuel_stops