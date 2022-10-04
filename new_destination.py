
# This file contains a function which performs a query in the database
# the function takes in ICAO code and return name, latitude and longitude of the airport.

from Database_Connection import connection

def currentLocation(code):
    sql = "SELECT name,latitude_deg, longitude_deg FROM airport"
    sql += " WHERE ident ='" + code + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:

            return(row[0], row[1], row[2])


