###############
## Stage 1
###############

from goal_service import get_all_goals, create_goal_reached
from weather_service import getWeatherDataByLatLon
from game_service import create_game, update_game_by_id
from geopy import distance
from co2_calculator import factor
from ICAO_checker import inputICAOCode
from introductory_text import stageOne, stageTwo, stageThree

all_goals = get_all_goals()
# https://www.geeksforgeeks.org/python-convert-a-list-to-dictionary/
goal_targets = {all_goals[i][0]: all_goals[i][1] for i in range(0, len(all_goals))}

airports = []
goals_achieved = set()
should_game_continue = True
total_battery_consumed = 0  # initially battery is not consumed at all

stageOne()

user_name = input("Please enter the player's name: ")

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
    # battery_life = 12500
    should_game_continue = battery_life is not None

    # print('game service loaded')
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

        airport_count = len(airports) - 1
        previous_coord = airports[airport_count - 1]['coord']
        current_coord = airports[airport_count]['coord']

        distance_travelled = round(distance.distance(previous_coord, current_coord).km, 2)

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

            weather_values = getWeatherDataByLatLon(current_coord[0], current_coord[1])

            temperature_goal_id = None
            weather_goal_id = None
            wind_speed_goal_id = None
            # goal_targets = {1: 'HOT', 2: 'COLD', 3: '0DEG', 4: '10DEG', 5: '20DEG', 6: 'CLEAR', 7: 'CLOUDY', 8: 'WINDY'}

            # conditions for temperature values
            if weather_values[0] > 25:
                temperature_goal_id = 1  # HOT
            elif weather_values[0] < -20:
                temperature_goal_id = 2  # COLD
            elif weather_values[0] == 0:
                temperature_goal_id = 3  # 0DEG
            elif weather_values[0] == 10:
                temperature_goal_id = 4  # 10DEG
            elif weather_values[0] == 20:
                temperature_goal_id = 5  # 20DEG

            if temperature_goal_id is not None:
                goal_reached = goal_targets[temperature_goal_id]
                goals_achieved.add(goal_reached)

                # create_goal_reached(game_id, temperature_goal_id)
                # update goal_reached table with game_id and temperature_goal_id

            # condition for clear or cloudy sky
            if weather_values[2] == 0:
                weather_goal_id = 6  # CLEAR
            else:
                weather_goal_id = 7  # CLOUDS

            if weather_goal_id is not None:
                goals_achieved.add(goal_targets[weather_goal_id])
                # create_goal_reached(game_id, weather_goal_id)
                # update goal_reached table with game_id and temperature_goal_id

            # condition for wind speed
            if weather_values[1] > 10:
                wind_speed_goal_id = 8
                goals_achieved.add(goal_targets[wind_speed_goal_id])  # WINDY

                # create_goal_reached(game_id, wind_speed_goal_id)
                # update goal_reached table with game_id and temperature_goal_id

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
