def execute_list_method(master_password, args):
    return NotImplemented


def execute_get_method(master_password, args):
    return NotImplemented


def execute_add_method(master_password, args):
    return NotImplemented


def execute_remove_method(master_password, args):
    return NotImplemented


def execute(master_password, method, args):
    if method == '-list':
        execute_list_method(master_password, args)

    if method == '-get':
        execute_get_method(master_password, args)

    if method == '-add':
        execute_add_method(master_password, args)

    if method == '-remove':
        execute_remove_method(master_password, args)
