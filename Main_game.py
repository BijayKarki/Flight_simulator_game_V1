
###############
## Step 1
###############

print()
user_name = input("Please enter the player's name: ")
start_location = input(str('Please enter your starting location (in ICAO format): ')).upper()
print()

# update this information to the existing database

loc_name = [] # starting an empty list to store the names of the airport where the player travels
loc_cord = [] # an empty list to store the coordinates of all the airport where the player travels

from new_destination import currentLocation
result = (currentLocation(start_location))
loc_name.append(result[0])
loc_cord.append(tuple(result[1:3]))

print ("A brief text on how to play the game will be displayed here to the player!!") # Write actual information here
print()

###############
## Step 2 (allocating CO2 budget to the player)
###############

# the mathematical questions or ways to allocate the budget will be here!

co2_bgd = 1000 # for test purpose only
print("Your allocated CO2 budget is " + str(co2_bgd) + ".")
print("Please do the routine engine checkup, fasten your seatbealt and start flying!!")

c = 1 # This variable is used to for indexing through the airport
while co2_bgd >= 0:
    print()
    next_location = input(str("Please enter your next destination (in ICAO format): ")).upper()

    result = (currentLocation(next_location))
    loc_name.append(result[0])  # current location
    loc_cord.append(tuple(result[1:3]))

    from geopy import distance
    dt = distance.distance(loc_cord[c-1], loc_cord[c]).km
    dt = round(dt,2) # distance travelled

    from co2_calculator import factor
    co2_emit = round(dt * factor, 2)  # co2 used for travelling to the new distination
    co2_bgd -= co2_emit

    if co2_bgd >0:
        print()
        print("Your new location is in " + loc_name[c] + ".")
        print("Distance travelled is " + str(dt) + "km.")
        print("Remaining co2 budget is "+ str(round(co2_bgd,2)) +".")

    c += 1

else:
    print()
    print('You ran out of your CO2 budget before reaching the distination!!')
print()






