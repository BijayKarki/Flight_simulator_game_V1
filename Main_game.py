###############
## Stage 1
###############

airports = []
should_game_continue = True

from introductory_text import gameDescription

gameDescription()

user_name = input("Please enter the player's name: ")

from ICAO_checker import inputICAOCode

start_location = inputICAOCode(True)
print()
# update this information to the existing database

if start_location is None:
    should_game_continue = False
else:
    airports.append({
        "name": start_location[0],
        "coord": tuple(start_location[1:3])
    })
    print(
        "++++++++++++++++++++++++++++++++++ The game begins, Good luck !! ++++++++++++++++++++++++++++++++++++++++++++++")
    print()

###############
## Step 2 (allocating bettery life to the player)
###############

# the player will be prompted to play the quiz here which earns him a battery life!


if should_game_continue:
    from sustainablity_quiz import playQuiz

    battery_life = playQuiz()
    should_game_continue = battery_life is not None

    print("Congratulations! You have earned " + str(battery_life) + " kAmph battery life for the flight.")
    print()
    print("Please do the routine engine checkup, fasten your seatbelt and start flying!!")
    print()
    print("----------------------------------- Have a safe flight !!----------------------------------------------")
    while battery_life >= 0 or should_game_continue:
        print()
        next_location = inputICAOCode()
        if next_location is not None:
            airports.append({
                "name": next_location[0],
                "coord": tuple(next_location[1:3])
            })
        else:
            should_game_continue = False

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
            print("Your new location    = ", airports[airport_count]['name'])
            print("Distance travelled   = ", distance_travelled, "km")
            print("Remaining battery    = ", (round(battery_life, 2)))
            print('*' * 5, "Weather info", '*' * 5)
            print("Local temperature    = ", weather_values[0], "degree centigrade")
            print("Wind speed           = ", weather_values[1], "m/s")
            print("Weather code         = ", weather_values[2],
                  "This is used to detect the cloudy or clear sky, still working on it!")
            print("---------------------------------------------------------------------------------------------------")

        else:
            print()

            print("You don't have enough battery life to reach the next destination!!")
            print()
            print(
                "++++++++++++++++++++++++++++++++++++++ Game Over !! +++++++++++++++++++++++++++++++++++++++++++++++++++")
            should_game_continue = False
