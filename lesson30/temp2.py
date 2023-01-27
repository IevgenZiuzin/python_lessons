import numbmenu
import authorize

auth = authorize.init()


def main():
    print('Welcome to Testify 0.1')
    run_menu = numbmenu.init(['Sign in', 'Sign up'], [auth.sign_in, auth.sign_up])
    run_menu.run()


main()
