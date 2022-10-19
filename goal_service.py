# This is the file that updates the user information to the database i.e. goal table
# This file is not yet functional!!!

from database_connection import connection


def get_all_goals():
    sql_read = f"SELECT id, name FROM goal"
    cursor = connection.cursor()
    cursor.execute(sql_read)
    result = cursor.fetchall()
    # print(result)
    return result


# work in progress (not completed!)
def create_goal_reached(game_id, goal_id):
    sql_update = f"INSERT INTO goal_reached (game_id, goal_id) " \
                 f"VALUES ('{game_id}', '{goal_id}'"
    cursor = connection.cursor()
    cursor.execute(sql_update)
