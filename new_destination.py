# This file contains a function which performs a query in the database
# the function takes in ICAO code and return name, latitude and longitude of the airport.

from Database_Connection import connection


def currentLocation(code):
    if code == "":
        raise Exception("ICAO code cannot be an empty string!")

    sql = "SELECT name, latitude_deg, longitude_deg, ident FROM airport"
    sql += " WHERE ident ='" + code + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    # print(result)

    if cursor.rowcount == 0:
        raise ValueError(f" Sorry!, no entry found in the database for the given ICAO code, i.e. {code}.")

    return result

# currentLocation('')


# try:
#     currentLocation('')
# except ValueError as e:
#     print("Handling value error exception with wrong code!")
#     # print(e)
# except Exception as e:
#     print(e)
# finally:
#     print("The program continues!")

# print("The program ends here!")

# currentLocation('EFHK')
