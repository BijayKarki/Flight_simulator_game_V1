# Future development
# CSS, Java script, html,
# sql injection (Important part, future enhancement)
# cyber security (sanitize user input) for all the user inputs e.g length specification, length, or data type(INT/string)
# restricted input for the parameters
# *, quotations, be careful for eg. about dropping the db.
# input validation for the future for e.g. empty code, wrong code, etc

airports = []

first_location = {
    "name": 'helsinki',
    "lat": 60.31,
    "lon": 24.91

}

airports.append(first_location)
airports.append({"name": 'riga',
                 "lat": 70.31,
                 "lon": 27.91}
                )

print(airports)
print(airports[1]['name'])
