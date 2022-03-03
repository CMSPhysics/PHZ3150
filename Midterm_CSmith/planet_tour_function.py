import numpy as np
import pandas as pd
import math
import sys


def planet_tour(start_location, destination_location):
    """Function asks the user if they want to take a grand tour Y/N.  If Y, then it returns the information regarding possible stops on the way to their destination (possible stops and dates, extra mileage, and refuelling information). If the user inputs N, it takes the start location and destination location of the trip and returns the travel time in earth years/days/heures/minutes, the shortest distance from the start location to the destination location, what date this trip is the shortest, refuel information and refuel stops. It will also send a message to the station regarding the number and location of refuelling stops needed. 
    Input: start_location, destination_location
    Output: time_years, time_days, time_hours, time_minutes, shortest_travel_distance, shortest_travel_day, refuel_stops, detour"""

    planets_and_moons = np.array(
        ['Mercury', 'Venus', 'Earth', 'Moon', 'Ceres', 'Mars', 'Jupiter', 'Io', 'Europa', 'Saturn', 'Titan', 'Neptune',
         'Pluto', 'Charon'])

    # Grand Tour IF/ELSE loop (If N, code breaks and returns the shortest distance of travel between start location and destination location. If Y, else code run Grand Tour.)

    gt = input('Do you wanna take a grand tour, input Y for yes or N for no.')

    for x in gt:
        if x == 'N':
            break
        elif x == 'Y':
            print('You have chosen to take a GRAND TOUR!')


            # Indexing and reading data from txt files for GRAND TOUR stops

            space_distance_data1 = np.loadtxt('../demos/solar_system_date_1.dat')
            space_distances_date2 = np.loadtxt('../demos/solar_system_date_2.dat')
            space_distances_date3 = np.loadtxt('../demos/solar_system_date_3.dat')

            start_body_i = start_location
            destination_body_i = destination_location

            #stop_location = input("Where would you like to stop on your GRAND TOUR?")

            df1 = pd.DataFrame(space_distance_data1, columns=planets_and_moons, index=planets_and_moons)
            distance_for_traveller1 = df1.loc[start_body_i, destination_body_i]
            df2 = pd.DataFrame(space_distances_date2, columns=planets_and_moons, index=planets_and_moons)
            distance_for_traveller2 = df2.loc[start_body_i, destination_body_i]
            df3 = pd.DataFrame(space_distances_date3, columns=planets_and_moons, index=planets_and_moons)
            distance_for_traveller3 = df3.loc[start_body_i, destination_body_i]

            # Finding the shortest distance of travel

            travel_dates = [distance_for_traveller1, distance_for_traveller2, distance_for_traveller3]
            

            shortest_travel_distance = min(travel_dates)

            shortest_travel_date = travel_dates.index(shortest_travel_distance)

            result = df1.loc[start_location, destination_location]

            #print('You will travel', shortest_travel_distance, 'AU', 'from', start_body_i, 'to', destination_body_i,"and occurs on day", shortest_travel_date + 1)
            
            #Finding the extra stop with the shortest distance(s) according to date(1,2,3)

            shortest_travel_column = [df1, df2, df3]

            result = pd.concat(shortest_travel_column, keys=['0', '1', '2'])
            df_index_shortest = str(shortest_travel_date)

            df_shortest = result.loc[df_index_shortest]

            col_df_shortest = pd.DataFrame(df_shortest[start_body_i])

            col_df_shortest_range_1 = pd.DataFrame(col_df_shortest[: start_body_i])
            col_df_shortest_range_2 = pd.DataFrame(col_df_shortest[start_body_i:])

            if destination_body_i in col_df_shortest_range_1.index:
                col_df_shortest_range_act = col_df_shortest_range_1
            else:
                col_df_shortest_range_act = col_df_shortest_range_2

            col_df_shortest_range_act_c = col_df_shortest_range_act.drop(destination_body_i)

            col_df_shortest_range_act_c_sort = col_df_shortest_range_act_c.sort_values(start_body_i)

            zz_top = col_df_shortest_range_act_c_sort[start_body_i].loc[col_df_shortest_range_act_c_sort[start_body_i] != 0]
           
            shortest_stop_name = zz_top.idxmin()
            shortest_stop_dist = zz_top.min()

            #print('Your shortest detour stop is', shortest_stop_name, 'with a distance of', shortest_stop_dist, 'AU')

            stop_to_dest = df_shortest.loc[shortest_stop_name, destination_body_i]
                
            #print('The distance from the extra stop to the final destination is', stop_to_dest, 'AU')

            tot_dist = stop_to_dest + shortest_stop_dist
            #print('You will have a total distance of ', tot_dist, 'AU')
            
            shortest_travel_column = [df1, df2, df3]

            result = pd.concat(shortest_travel_column, keys=['0', '1', '2'])
            df_index_shortest = str(shortest_travel_date)

            stops_for_date = {'date_1' : '0', 'date_2' : '1', 'date_3' : '2'}

            df_shortest = result.loc[df_index_shortest]


            df_td_1 = result.loc['0']
            df_td_2 = result.loc['1']
            df_td_3 = result.loc['2']

            col_df_shortest = pd.DataFrame(df_shortest[start_body_i])


            col_df_td_1 = pd.DataFrame(df_td_1[start_body_i])
            col_df_td_2 = pd.DataFrame(df_td_2[start_body_i])
            col_df_td_3 = pd.DataFrame(df_td_3[start_body_i])

            col_df_shortest_range_1 = pd.DataFrame(col_df_shortest[: start_body_i])
            col_df_shortest_range_2 = pd.DataFrame(col_df_shortest[start_body_i :])


            col_df_td_1_range_1 = pd.DataFrame(col_df_td_1[: start_body_i])
            col_df_td_1_range_2 = pd.DataFrame(col_df_td_1[start_body_i :])

            col_df_td_2_range_1 = pd.DataFrame(col_df_td_2[: start_body_i])
            col_df_td_2_range_2 = pd.DataFrame(col_df_td_2[start_body_i :])

            col_df_td_3_range_1 = pd.DataFrame(col_df_td_3[: start_body_i])
            col_df_td_3_range_2 = pd.DataFrame(col_df_td_3[start_body_i :])

            if destination_body_i in col_df_shortest_range_1.index:
                col_df_shortest_range_act = col_df_shortest_range_1
            else:
                col_df_shortest_range_act = col_df_shortest_range_2

            if destination_body_i in col_df_td_1_range_1.index:
                col_df_td_1_range_act = col_df_td_1_range_1
            else:
                col_df_td_1_range_act = col_df_td_1_range_2

            if destination_body_i in col_df_td_2_range_1.index:
                col_df_td_2_range_act = col_df_td_2_range_1
            else:
                col_df_td_2_range_act = col_df_td_2_range_2

            if destination_body_i in col_df_td_3_range_1.index:
                col_df_td_3_range_act = col_df_td_3_range_1
            else:
                col_df_td_3_range_act = col_df_td_3_range_2

            col_df_shortest_range_act_c =  col_df_shortest_range_act.drop(destination_body_i)


            col_df_td_1_range_act_c = col_df_td_1_range_act.drop(destination_body_i)

            col_df_td_2_range_act_c = col_df_td_2_range_act.drop(destination_body_i)

            col_df_td_3_range_act_c = col_df_td_3_range_act.drop(destination_body_i)


            col_df_shortest_range_act_c_sort = col_df_shortest_range_act_c.sort_values(start_body_i)


            col_df_td_1_range_act_c_sort = col_df_td_1_range_act_c.sort_values(start_body_i)

            col_df_td_2_range_act_c_sort = col_df_td_2_range_act_c.sort_values(start_body_i)

            col_df_td_3_range_act_c_sort = col_df_td_3_range_act_c.sort_values(start_body_i)


            zz_top = col_df_shortest_range_act_c_sort[start_body_i].loc[ col_df_shortest_range_act_c_sort[start_body_i] !=0]

            zz_top_1 = col_df_td_1_range_act_c_sort[start_body_i].loc[ col_df_td_1_range_act_c_sort[start_body_i] !=0]

            zz_top_2 = col_df_td_2_range_act_c_sort[start_body_i].loc[ col_df_td_2_range_act_c_sort[start_body_i] !=0]

            zz_top_3 = col_df_td_3_range_act_c_sort[start_body_i].loc[ col_df_td_3_range_act_c_sort[start_body_i] !=0]


            shortest_stop_name = zz_top.idxmin()
            shortest_stop_dist = zz_top.min()

            stop_to_dest = df_shortest.loc[shortest_stop_name, destination_body_i]
            tot_dist = stop_to_dest + shortest_stop_dist

            stop_to_dest_1 = df_td_1.loc[shortest_stop_name, destination_body_i]
            tot_dist = stop_to_dest + shortest_stop_dist

            shortest_stop_name_1 = zz_top_1.idxmin()
            shortest_stop_dist_1 = zz_top_1.min()

            shortest_stop_name_2 = zz_top_2.idxmin()
            shortest_stop_dist_2 = zz_top_2.min()

            shortest_stop_name_3 = zz_top_3.idxmin()
            shortest_stop_dist_3 = zz_top_3.min()

            stop_to_dest_1 = df_td_1.loc[shortest_stop_name_1, destination_body_i]
            tot_dist_1 = stop_to_dest_1 + shortest_stop_dist_1

            stop_to_dest_2 = df_td_2.loc[shortest_stop_name_2, destination_body_i]
            tot_dist_2 = stop_to_dest_2 + shortest_stop_dist_2

            stop_to_dest_3 = df_td_3.loc[shortest_stop_name_3, destination_body_i]
            tot_dist_3 = stop_to_dest_3 + shortest_stop_dist_3


            if shortest_stop_name_1 in [shortest_stop_name_2]:

                src = shortest_stop_name_1, shortest_stop_name_2
                shortest_stop_name_1 = shortest_stop_name_1 + str('_1')
                shortest_stop_name_2 = shortest_stop_name_2 + str('_2')
            elif shortest_stop_name_1 in [shortest_stop_name_3]:
                src2 = shortest_stop_name_1, shortest_stop_name_3
                shortest_stop_name_1 = shortest_stop_name_1 + str('_1')
                shortest_stop_name_3 = shortest_stop_name_3 + str('_3')
            elif shortest_stop_name_2 in [shortest_stop_name_3]:
                src3 = shortest_stop_name_2, shortest_stop_name_3
                shortest_stop_name_2 = shortest_stop_name_2 + str('_2')
                shortest_stop_name_3 = shortest_stop_name_3 + str('_3')
            else:
                shortest_stop_name_1 = shortest_stop_name_1
                shortest_stop_name_2 = shortest_stop_name_2
                shortest_stop_name_3 = shortest_stop_name_3

            print('The possible stops are', shortest_stop_name_1, 'for date_1,', shortest_stop_name_2, 'for date_2, and,', shortest_stop_name_3, 'for date_3')
            
            #Dictionary for possible stops 
            my_dict = {shortest_stop_name_1 : tot_dist_1,  shortest_stop_name_2 :  tot_dist_2,  shortest_stop_name_3 :  tot_dist_3}
            
            #Stop Mercury1 refuel 
            refuel_stops = int(math.ceil(shortest_travel_distance * (1 / 0.65)))
            refuel_extra_stop = int(math.ceil(shortest_stop_dist_1 * (1 / 0.65)))
            refuel_stop_dest = int(math.ceil(stop_to_dest * (1 / 0.65)))
            
            refuel_grand_tour1 = refuel_stop_dest + refuel_extra_stop
            
            #Stop Mercury2 refuel 
            refuel_stops = int(math.ceil(shortest_travel_distance * (1 / 0.65)))
            refuel_extra_stop = int(math.ceil(shortest_stop_dist_2 * (1 / 0.65)))
            refuel_stop_dest = int(math.ceil(stop_to_dest * (1 / 0.65)))
            
            refuel_grand_tour2 = refuel_stop_dest + refuel_extra_stop
            
            #Stop Venus3 refuel 
            refuel_stops = int(math.ceil(shortest_travel_distance * (1 / 0.65)))
            refuel_extra_stop = int(math.ceil(shortest_stop_dist_3 * (1 / 0.65)))
            refuel_stop_dest = int(math.ceil(stop_to_dest * (1 / 0.65)))
            
            refuel_grand_tour3 = refuel_stop_dest + refuel_extra_stop
            
            #print("You will require", refuel_grand_tour, "refuelling stops for a GRAND TOUR!")
            
            print("The stop", shortest_stop_name_1, "will add", shortest_stop_dist_1, "AU to your trip, and require", refuel_grand_tour1, "refuelling stops.")
            print("The stop", shortest_stop_name_2, "will add", shortest_stop_dist_2, " AU to your trip, and require", refuel_grand_tour2, "refuelling stops.")
            print("The stop", shortest_stop_name_3, "will add", shortest_stop_dist_3, "AU to your trip, and require", refuel_grand_tour3, "refuelling stops.")
          
            #Choosing your stop             
            stop_choice = input("What stop would you like to choose for your trip?")
            
            if stop_choice == shortest_stop_name_1:
                print("You've chosen", shortest_stop_name_1, "as your stop. The best day is date 1 to travel to this stop. You will require", refuel_grand_tour1, "refuelling stops.")
            elif stop_choice == shortest_stop_name_2:
                print("You've chosen", shortest_stop_name_2, "as your stop. The best day is date 2 to travel to this stop. You will require", refuel_grand_tour2, "refuelling stops.")
            elif stop_choice == shortest_stop_name_3:
                print("You've chosen", shortest_stop_name_3, "as your stop. The best day is date 3 to travel to this stop. You will require", refuel_grand_tour3, "refuelling stops.")
        
            #Dictionary for possible stops 
            my_dict = {shortest_stop_name_1 : tot_dist_1,  shortest_stop_name_2 :  tot_dist_2,  shortest_stop_name_3 :  tot_dist_3}
            i = stop_choice 
            for i in my_dict:
                value = my_dict[i]
                
            x = str(value)
                
            #Fuel stops for chosen stop
            
            refuel_stops = int(math.ceil(shortest_travel_distance * (1 / 0.65)))
            refuel_extra_stop = int(math.ceil(value * (1 / 0.65)))
            refuel_stop_dest = int(math.ceil(stop_to_dest * (1 / 0.65)))
            
            refuel_grand_tour = refuel_stop_dest + refuel_extra_stop
            
            #refuel_date = refuel_dates.get(key)
            my_dict = {shortest_stop_name_1 : '1' ,  shortest_stop_name_2 : '2' ,  shortest_stop_name_3 : '3' }
            i = stop_choice 
            for i in my_dict:
                date = my_dict[i]
            
            d = str(date)
            
            #Refuel days 

            #z = np.round(((0.65 / 0.001) / 24 ) , 3)
            z = [27.083]
            for i in range( 0, 11):
                z.append( z[i] + 27.083)
                
            # Sending information back to station in message_to_stations_stops.txt
                
            df_t = open('message_to_stations_stops.txt', 'w')
            df_t.write(' Beginning at the location ')
            df_t.write(start_body_i)
            df_t.write(' and ending at ')
            df_t.write(destination_body_i)
            df_t.write(', and this is the refuelling information for my trip which starts on day ')
            df_t.write(d)
            df_t.write('. I will need to encounter stations for refueling at \n')
            for x in range(1, refuel_grand_tour):
                y = round(0.65 * x, 4)
                z = np.round(z, 3)
                df_t.write('We will refuel on date ')
                df_t.write(str(d))
                df_t.write(' + ')
                df_t.write(str(z))
                df_t.write(' days at the location ')
                df_t.write(str(y))
                df_t.write(' AU ')
                df_t.write('\n')
            df_t.close()
            sys.exit()

    # Indexing and reading data from txt files

    space_distance_data1 = np.loadtxt('../demos/solar_system_date_1.dat')
    space_distances_date2 = np.loadtxt('../demos/solar_system_date_2.dat')
    space_distances_date3 = np.loadtxt('../demos/solar_system_date_3.dat')

    start_body_i = start_location
    destination_body_i = destination_location

    df1 = pd.DataFrame(space_distance_data1, columns=planets_and_moons, index=planets_and_moons)
    distance_for_traveller1 = df1.loc[start_body_i, destination_body_i]
    df2 = pd.DataFrame(space_distances_date2, columns=planets_and_moons, index=planets_and_moons)
    distance_for_traveller2 = df2.loc[start_body_i, destination_body_i]
    df3 = pd.DataFrame(space_distances_date3, columns=planets_and_moons, index=planets_and_moons)
    distance_for_traveller3 = df3.loc[start_body_i, destination_body_i]

    # Finding the shortest distance of travel

    travel_dates = [distance_for_traveller1, distance_for_traveller2, distance_for_traveller3]

    shortest_travel_distance = min(travel_dates)

    shortest_travel_date = travel_dates.index(shortest_travel_distance)

    # The day that the shortest travel distance is possible

    # Total travel time based on average speed of 0.001AU/hr

    time_total = shortest_travel_distance / 0.001

    # Travel time in earth years, days, hours, minutes

    time_years = int((time_total / 24) * (1 / 365))
    d = ((time_total / 24) * (1 / 365) - time_years) * 365
    time_days = int(d)
    h = (d - time_days) * 24
    time_hours = int(h)
    m = (h - time_hours) * 60
    time_minutes = int(m)

    # Number of refueling stops required per trip

    refuel_stops = int(math.ceil(shortest_travel_distance * (1 / 0.65)))

    # Sending information back to station in message_to_stations3.txt

    df_t = open('message_to_stations3.txt', 'w')
    df_t.write('my trip starts at ')
    df_t.write(start_body_i)
    df_t.write(' and ends at ')
    df_t.write(destination_body_i)
    df_t.write(', I will need to encounter stations for \na refueling at \n')
    for x in range(1, refuel_stops):
        y = round(0.65 * x, 4)
        df_t.write(str(y))
        df_t.write('AU')
        df_t.write('\n')
    df_t.close()

    # Printing trip information
   
    print("The shortest distance from", start_body_i, "to", destination_body_i, "is", shortest_travel_distance, "AU",
          "and occurs on day", shortest_travel_date + 1,'.')
    print()
    print("This trip will take", time_years, "Earth years,", time_days, "Earth days,", time_hours, "Earth hours, and", time_minutes, "Earth minutes!")
    print()
    print("You will require", refuel_stops, "refuelling stops!")

    return time_years, time_days, time_hours, time_minutes, shortest_travel_distance, refuel_stops