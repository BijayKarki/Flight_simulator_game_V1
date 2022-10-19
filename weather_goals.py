# This files checks if the local weather complies with the weather targets

from weather_service import getWeatherDataByLatLon

# Helsinki Vantaa Airport (60.3172, 24.963301)

weather_values = getWeatherDataByLatLon(60.3172, 24.963301)

# goal_targets = ['HOT', 'COLD', '0DEG', '10DEG', '20DEG', 'CLEAR', 'CLOUDS', 'WINDY']
goal_targets = {0: 'HOT', 1: 'COLD', 2: '0DEG', 3: '10DEG', 4: '20DEG', 5: 'CLEAR', 6: 'CLOUDS', 7: 'WINDY'}
goal_achieved = set()
print()
print(f"Goal targets set:{goal_targets}.")
print()

# conditions for temperature values
if weather_values[0] > 25:
    goal_achieved.add(goal_targets[0])
elif weather_values[0] < -20:
    goal_achieved.add(goal_targets[1])
elif weather_values[0] == 0:
    goal_achieved.add(goal_targets[2])
elif weather_values[0] == 10:
    goal_achieved.add(goal_targets[3])
elif weather_values[0] == 20:
    goal_achieved.add(goal_targets[4])

# condition for clear or cloudy sky
if weather_values[2] == 0:
    goal_achieved.add(goal_targets[5])
else:
    goal_achieved.add(goal_targets[6])

# conditions for wind speed
if weather_values[1] > 10:
    goal_achieved.add(goal_targets[7])

print(f'Achieved goals are: {goal_achieved}')
print(f'Remaning goals are: {goal_targets}')
