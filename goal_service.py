from database_connection import connection


def get_all_goals():
    sql_read = f"SELECT id,name FROM goal"

    cursor = connection.cursor()
    cursor.execute(sql_read)
    result = cursor.fetchall()
    # print(result)
    return result


get_all_goals()


def create_game(screen_name, co2_budget, location):
    import uuid
    unique_id = str(uuid.uuid4())[:8]  # unique identifier
    # (str(unique_id)[:8])  # converting it into a string and slicing only 8 characters

    sql_write = f"INSERT INTO game(id, screen_name, co2_budget, location) " \
                f"VALUES('{unique_id}', '{screen_name}', '{co2_budget}', '{location}')"

    cursor = connection.cursor()
    cursor.execute(sql_write)
    return unique_id


def update_game_by_id(id, co2_consumed, location):
    sql_update = f"UPDATE game SET co2_consumed = '{co2_consumed}', location ='{location}' WHERE id = '{id}'"

    cursor = connection.cursor()
    cursor.execute(sql_update)
