
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game_new',
    user='root',
    password='bijay123',
    autocommit=True
)
