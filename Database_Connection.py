# This file establishes the connection to the local database for the project work

import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game_test',  # Please comply your own credentials
    user='root',  # Please comply your own credentials
    password='bijay123',  # Please comply your own credentials
    autocommit=True
)
