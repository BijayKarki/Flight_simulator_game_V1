# This is a file containing texts which are printed during the game execution.
spaces = 9
column_count = 113
from time import sleep

sleep_time = 1


def stageOne():
    print()
    print(
        "---------------------------------- Welcome to 'A Flight Simulator game' -----------------------------------------")
    print()
    sleep(sleep_time)
    print(
        "---------------------------------------- Designed by 'Group 4' --------------------------------------------------")
    print()
    sleep(sleep_time)
    print("The game consists of three stages.")
    print()
    sleep(sleep_time)
    print(":" * column_count)
    print()
    print("Stage 1: The game asks 'name' and 'starting location' (in ICAO format) of the player.")
    print()
    print(":" * column_count)
    print()
    sleep(sleep_time)


def stageTwo():
    print()
    sleep(sleep_time)
    print(":" * column_count)
    print()
    print("Stage 2: The player will be flying an electric plane but the battery is empty in the beginning.")
    sleep(sleep_time)
    print(spaces * ' ' + "So, the player must play a quiz game on sustainability topics to earn the battery life.")
    sleep(sleep_time)
    print(spaces * ' ' + "The player chooses a topic of his/her choice out of 5, each containing 5 questions.")
    sleep(sleep_time)
    print(spaces * ' ' + "For each right answer, 2500 Ah battery life is rewarded to the player.")
    print()
    print(":" * column_count)
    sleep(sleep_time)
    print()


def stageThree():
    print()
    sleep(sleep_time)
    print(":" * column_count)
    print()
    print("Stage 3: After earning battery life, the player is ready to fly around the world.")
    sleep(sleep_time)
    print(
        spaces * ' ' + "The goal is to collect weather passports by flying around the world within the battery life.")
    sleep(sleep_time)
    print(
        spaces * ' ' + "The passports will be collected automatically based on the real time weather fetched using API.")
    sleep(sleep_time)
    print(
        spaces * ' ' + "The weather passports to aim for are; HOT, COLD, 0 DEG, 10 DEG, 20 DEG, CLEAR, CLOUDY and WINDY.")
    print()
    print(":" * column_count)
    sleep(sleep_time)
    print()
