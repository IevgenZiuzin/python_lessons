import json


def file_read(path):
    with open(path, 'r') as file:
        return json.loads(file.read())


def file_write(path, body):
    with open(path, 'w') as file:
        return file.write(json.dumps(body))


def check_login(login, db):
    return db.get(login, False)


def check_pass(login, password, db):
    if check_login(login, db) and db[login] == password:
        return True
    return False


def check_auth_data(path, login, password):
    db = file_read(path)
    if not check_login(login, db):
        return False
    return True if check_pass(login, password, db) else False
