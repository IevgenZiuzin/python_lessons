import numbmenu
import authorize


class User_mod:

    @staticmethod
    def tests_mod():
        auth = authorize.init()
        menu_items = []
        commands = []
        menu = numbmenu.init(menu_items, commands)
        menu.run()

    @staticmethod
    def results_mod():
        pass


def init():
    return User_mod()
