import database
import crypter


def print_rows(rows, master_password, pass_index=2):
    if rows == -1:
        return False

    for row in rows:
        row = list(row)
        row[pass_index] = crypter.decrypt(row[pass_index], master_password)
        print(row)

    return True


def execute_list_method(master_password):
    rows = database.select_all()

    return print_rows(rows, master_password)


def execute_get_method(master_password, args):
    rows = database.select_given_website(args[0])

    return print_rows(rows, master_password, 1)


def execute_add_method(master_password, args):
    args[2] = crypter.encrypt(args[2], master_password)
    return database.insert_user(args[0], args[1], args[2])


def execute_edit_method(master_password, args):
    args[3] = crypter.encrypt(args[3], master_password)
    return database.update_user(args[0], args[1], args[2], args[3])


def execute_remove_method(master_password, args):
    accounts_for_website = database.select_given_website(args[0])

    for account in accounts_for_website:
        if account[0] == args[1]:
            _ = crypter.decrypt(account[1], master_password)
            return database.remove_user(args[0], args[1])


def execute(master_password, method, args):
    if method == '-list':
        execute_list_method(master_password)

    if method == '-get':
        execute_get_method(master_password, args)

    if method == '-add':
        execute_add_method(master_password, args)

    if method == '-edit':
        execute_edit_method(master_password, args)

    if method == '-remove':
        execute_remove_method(master_password, args)
