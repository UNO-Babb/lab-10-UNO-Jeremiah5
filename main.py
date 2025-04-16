#MapPlot.py
#Name:Jeremiah Sanchez 
#Date: 16 April 2025
#Assignment: Los Angeles Lakers in 5

import astronauts
mission = astronauts.get_mission()

all_mission = len(mission)

vehicle_list = []
year_list = []

for spot in range(all_mission):
    vehicle = mission[spot]["Mission"]["Vechicles"]["Orbit"]
    year = mission[spot]["Mission"]["Year"]
    if year > 2010: #vehicle == "STS-124":
        print(year)
        print(vehicle)
        vehicle_list.append(vehicle)
        year_list.append(year)

print(vehicle_list, year_list)

import matplotlib.pyplot as plt
plt.plot(vehicle_list, year_list)
plt.xlabel('Mission')
plt.ylabel('Year')
plt.savefig("output")







"""


if total_score > 10:
    scores.append(total_score)
    years.append(year)



    plt.plot(years, scores, 'ro')

"""