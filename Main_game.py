
print()
user_name = input ('Please enter your name: ')
user_location = input ('Please enter your location (in ICAO format): ')


print ("all the information required for the player to proceed further!!") # Write actual information here



from Database_Connection import connection as cnc

def currentLocation(code):
    sql = "SELECT name,latitude_deg, longitude_deg FROM airport"
    sql += " WHERE ident ='" + code + "'"

    cursor = cnc.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            #print(f"{row[0]}, latitude: {row[1]} and longitude: {row[2]}")
            return(row[0], row[1], row[2])


