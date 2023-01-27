def main():
    print("Welcome to Testing System.\nAuthorize first")
    login = input("login: ")
    password = input("password: ")
    if login and password:
        if check_admin():
            command()
        else:
            test()




main()