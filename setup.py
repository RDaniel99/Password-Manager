import sqlite3


def create_password_table():
    sql_create_passwords_table = """ CREATE TABLE IF NOT EXISTS passwords (
                                            website text NOT NULL,
                                            user text NOT NULL,
                                            password text NOT NULL
                                        ); """

    conn = sqlite3.connect("passwords.db")

    if conn is not None:
        try:
            c = conn.cursor()
            c.execute(sql_create_passwords_table)
        except sqlite3.Error as e:
            print(e)
