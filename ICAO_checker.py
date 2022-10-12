# This file contains a function which performs a query in the database

from new_destination import currentLocation


def inputICAOCode(isStartingAirport=False):
    max_attempt = 5  # No. of chances provided to the player for a valid input
    prompt_message = 'Please enter the ICAO of your '
    prompt_message += 'starting airport: ' if isStartingAirport else 'next destination airport: '
    for attempt_no in range(0, max_attempt):
        print()
        try:
            code = str(input(prompt_message))
            location = currentLocation(code)
            return location
        except Exception as e:
            print("❗Invalid Input❗")
            print(e)

            if max_attempt - (attempt_no + 1) == 0:
                return None
            else:
                print(f"You have {max_attempt - (attempt_no + 1)} more attempts to give a valid input!")
                continue
