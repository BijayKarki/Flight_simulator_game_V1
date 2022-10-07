###############
## Stage 1
###############

from introductory_text import gameDescription

gameDescription()

user_name = input("Please enter the player's name: ")
start_location = input(str('Please enter your starting location (in ICAO format): ')).upper()
print()
# update this information to the existing database

airports = []
should_game_continue = True

from new_destination import currentLocation

result = (currentLocation(start_location))

# airports.append(location)

airports.append({
    "name": result[0],
    "coord": tuple(result[1:3])

})
print("++++++++++++++++++++++++++++++++++ The game begins, Good luck !! ++++++++++++++++++++++++++++++++++++++++++++++")
print()

###############
## Step 2 (allocating CO2 budget to the player)
###############

# the player will be prompted to play the quiz here which earns him a battery life!

from sustainablity_quiz import playQuiz

battery_life = playQuiz()
should_game_continue = battery_life is not None

if should_game_continue:
    print("Congratulations! You have earned " + str(battery_life) + " kAmph battery life for the flight.")
    print()
    print("Please do the routine engine checkup, fasten your seatbelt and start flying!!")
    print()
    print("----------------------------------- Have a safe flight !!----------------------------------------------")
    while battery_life >= 0:
        print()
        next_location = input(str("Please enter your next destination (in ICAO format): ")).upper()

        result = (currentLocation(next_location))
        airports.append({
            "name": result[0],
            "coord": tuple(result[1:3])

        })

        from geopy import distance

        airport_count = len(airports) - 1
        previous_coord = airports[airport_count - 1]['coord']
        current_coord = airports[airport_count]['coord']

        distance_travelled = round(distance.distance(previous_coord, current_coord).km, 2)

        from co2_calculator import factor

        battery_consumed = round(distance_travelled * factor, 2)  # co2 produced for travelling to the new destination
        battery_life -= battery_consumed

        from Weather_API import getWeatherDataByLatLon

        weather_values = getWeatherDataByLatLon(current_coord[0], current_coord[1])

        if battery_life > 0:
            print()
            print("Your new location is in " + airports[airport_count]['name'] + ".")
            print("Distance travelled   = ", distance_travelled, "km")
            # print(distance_between_airports) # improvise this part using dictionary format
            print("Remaining co2 budget = ", (round(battery_life, 2)))
            print("Local temperature    = ", weather_values[0], "degree centigrade")
            print("Wind speed           = ", weather_values[1], "m/s")
            print("Weather code         = ", weather_values[2],
                  "This is used to detect the coludy or clear sky, still wokring on it!")
            print("---------------------------------------------------------------------------------------------------")

    else:
        print()

        print('You ran out of your battery before reaching the distination!!')
        print()
        print("++++++++++++++++++++++++++++++++++++++ Game Over !! +++++++++++++++++++++++++++++++++++++++++++++++++++")
