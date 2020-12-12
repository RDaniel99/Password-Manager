import sqlite3

sql_select_passwords_table = """ SELECT website, user, password from passwords; """
sql_create_passwords_table = """ CREATE TABLE IF NOT EXISTS passwords (
                                            website text NOT NULL,
                                            user text NOT NULL,
                                            password text NOT NULL,
                                            UNIQUE(website, user)
                                ); """
sql_select_given_website = """ SELECT user, password from passwords p where website=\"{}\" """
sql_insert_passwords_table = """ INSERT INTO passwords(website, user, password) 
                                    VALUES(\"{}\", \"{}\", \"{}\"); """
sql_remove_passwords_table = """ DELETE FROM passwords where website = \"{}\" AND user = \"{}\"; """
sql_update_passwords_table = """ UPDATE passwords SET user=\"{}\", password=\"{}\" 
                                 WHERE website = \"{}\" AND user=\"{}\" ; """


def select_all():
    return execute(sql_select_passwords_table, True)


def select_given_website(website):
    return execute(sql_select_given_website.format(website), True)


def insert_user(website, user, password):
    execute(sql_insert_passwords_table.format(website, user, password))


def update_user(website, old_user, user, password):
    execute(sql_update_passwords_table.format(user, password, website, old_user))


def remove_user(website, user):
    execute(sql_remove_passwords_table.format(website, user))


def execute(sql_statement, should_return_rows=False):
    conn = sqlite3.connect("passwords.db")

    rows = []
    if conn is not None:
        try:
            c = conn.cursor()
            c.execute(sql_statement)
            if should_return_rows:
                rows = c.fetchall()
            conn.commit()
        except sqlite3.Error as e:
            print(e)
            return -1

    if should_return_rows:
        return rows
