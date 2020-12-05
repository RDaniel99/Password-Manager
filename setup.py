import database


def create_password_table():
    database.execute(database.sql_create_passwords_table)
