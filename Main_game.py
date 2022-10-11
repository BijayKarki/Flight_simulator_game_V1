###############
## Stage 1
###############


airports = []
goal_targets = {0: 'HOT', 1: 'COLD', 2: '0DEG', 3: '10DEG', 4: '20DEG', 5: 'CLEAR', 6: 'CLOUDY', 7: 'WINDY'}
goals_achieved = set()
should_game_continue = True
total_battery_consumed = 0  # initially battery is not consumed at all

from introductory_text import stageOne, stageTwo, stageThree

stageOne()

user_name = input("Please enter the player's name: ")

from ICAO_checker import inputICAOCode

start_location = inputICAOCode(True)  # True for start location, false = later in the loop
print()
# update this information to the existing database

if start_location is None:
    should_game_continue = False
else:
    airports.append({
        "name": start_location[0],
        "coord": tuple(start_location[1:3])
    })
    print("+" * 113)
    print("+" * 40, " The game begins, Good luck !! ", "+" * 40)
    print("+" * 113)
    print()

###############
## Step 2 (allocating bettery life to the player)
###############

# the player will be prompted to play the quiz here which earns him a battery life!
stageTwo()

if should_game_continue:
    from sustainablity_quiz import playQuiz

    battery_life = playQuiz()
    should_game_continue = battery_life is not None

    from game_service import create_game, update_game_by_id

    game_id = create_game(user_name, battery_life, start_location[3])
    print("Congratulations! You have earned " + str(battery_life) + " Ah battery life for the flight.")
    print()
    stageThree()
    print("Please do the routine engine checkup, fasten your seatbelt and start flying!!")
    print()
    print("-" * 44, " Have a safe flight !! ", "-" * 44)

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
        total_battery_consumed += battery_consumed

        if battery_life > 0 and len(goals_achieved) == 7:

            print()
            print(f"You managed to collect all the {len(goals_achieved)} weather passports!")
            print()
            print("+" * 113)
            print("+" * 37, " Congratulations!! you won the game. ", "+" * 37)
            print("+" * 113)


        elif battery_life > 0:
            update_game_by_id(game_id, total_battery_consumed, next_location[3])

            from Weather_API import getWeatherDataByLatLon

            weather_values = getWeatherDataByLatLon(current_coord[0], current_coord[1])

            # print(f"Goal targets set:{goal_targets}.")

            # conditions for temperature values
            if weather_values[0] > 25:
                temperature_goal_acheived = goal_targets[0]
            elif weather_values[0] < -20:
                temperature_goal_acheived = goal_targets[1]
            elif weather_values[0] == 0:
                temperature_goal_acheived = goal_targets[2]
            elif weather_values[0] == 10:
                temperature_goal_acheived = goal_targets[3]
            elif weather_values[0] == 20:
                temperature_goal_acheived = goal_targets[4]

            goals_achieved.add(temperature_goal_acheived)

            # condition for clear or cloudy sky
            if weather_values[2] == 0:
                weather_goal_achieved = goal_targets[5]
            else:
                weather_goal_achieved = goal_targets[6]

            goals_achieved.add(weather_goal_achieved)

            # condition for wind speed
            if weather_values[1] > 10:
                goals_achieved.add(goal_targets[7])

            print()
            print("Your new location    = ", airports[airport_count]['name'])
            print("Distance travelled   = ", distance_travelled, "km")
            print("Remaining battery    = ", (round(battery_life, 2)), "Ah")
            print()
            print('*' * 10, "Local weather conditions", '*' * 10)
            print("Temperature          = ", weather_values[0], "degree centigrade")
            print("Wind speed           = ", weather_values[1], "m/s")
            print("Sky condition        = ", weather_values[2], "(Weather code)")
            print("-" * 113)
            print(f"Target goals         =  {list(goal_targets.values())}")
            print(f"Goals achieved       =  {list(goals_achieved)}")

            print("-" * 113)
        else:
            print()

            print("You don't have enough battery life to reach the next destination!!")
            print()
            print(f"You managed to collect only {len(goals_achieved)} weather passports out of {len(goal_targets)}!")
            print()
            print("+" * 113)
            print("+" * 49, " Game Over !!", "+" * 49)
            print("+" * 113)
            should_game_continue = False
