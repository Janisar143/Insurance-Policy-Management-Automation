import mysql.connector


def get_policy_details(policy_id):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        possword="password",
        database="insurance_db"
    )

    cursor = connection.cursor()
    cursor.execute(f"SELECT *FROM policy WHERE id = {policy_id}")
    result = cursor.fetchone()
    connection.cursor()
    return result
