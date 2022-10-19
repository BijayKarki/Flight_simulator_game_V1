# This file contains a function which performs a query in the database
# The function takes in ICAO code and return name, latitude, longitude and ICAO of the airport.

from database_connection import connection


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
