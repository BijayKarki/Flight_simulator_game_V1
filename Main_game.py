###############
## Step 1
###############

print()
print("-----------------------------------The game begins, Good luck !!----------------------------------------------")
print()

user_name = input("Please enter the player's name: ")
start_location = input(str('Please enter your starting location (in ICAO format): ')).upper()
print()

# update this information to the existing database

airports = []

loc_name = []  # an empty list to store the names of the airport where the player travels
loc_cord = []  # an empty list to store the coordinates of all the airport where the player travels

from new_destination import currentLocation

result = (currentLocation(start_location))
loc_name.append(result[0])
loc_cord.append(tuple(result[1:3]))

# airports.append(location)

airports.append({
    "name": result[0],
    "coord": tuple(result[1:3])

})

print("A brief text on how to play the game will be displayed here to the player!!")  # Write actual information here
print()

###############
## Step 2 (allocating CO2 budget to the player)
###############

# the player will be prompted to play the quiz here which earns him a battery life!

from sustainablity_quiz import playQuiz

battery_life = playQuiz()

print("You have earned " + str(battery_life) + " battery life from the quiz.")
print("Please do the routine engine checkup, fasten your seatbelt and start flying!!")

c = 1  # This variable is used for indexing through the airport where the user reaches
while battery_life >= 0:

    next_location = input(str("Please enter your next destination (in ICAO format): ")).upper()

    result = (currentLocation(next_location))
    airports.append({
        "name": result[0],
        "coord": tuple(result[1:3])

    })
    loc_name.append(result[0])  # current location
    loc_cord.append(tuple(result[1:3]))

    from geopy import distance

    distance_travelled = distance.distance(loc_cord[c - 1], loc_cord[c]).km
    distance_travelled = round(distance_travelled, 2)

    airport_count = len(airports) - 1
    previous_coord = airports[airport_count - 1]['coord']
    current_coord = airports[airport_count]['coord']

    distance_between_airports = distance.distance(previous_coord, current_coord).km

    from co2_calculator import factor

    co2_emit = round(distance_travelled * factor, 2)  # co2 produced for travelling to the new destination
    battery_life -= co2_emit

    from Weather_API import getWeatherDataByLatLon

    weather_values = getWeatherDataByLatLon(loc_cord[c][0], loc_cord[c][1])

    if battery_life > 0:
        print()
        print("Your new location is in " + loc_name[c] + ".")
        print("Distance travelled   = ", distance_travelled, "km")
        # print(distance_between_airports) # improvise this part using dictionary format
        print("Remaining co2 budget = ", (round(battery_life, 2)))
        print("Local temperature    = ", weather_values[0], "degree centigrade")
        print("Wind speed           = ", weather_values[1], "m/s")
        print("Weather code         = ", weather_values[2],
              "This is used to detect the coludy or clear sky, still wokring on it!")
        print("---------------------------------------------------------------------------------")

    c += 1

else:
    print()

    print('You ran out of your CO2 budget before reaching the distination!!')
    print()
    print("-----------------------------------Game Over !!----------------------------------------------")
