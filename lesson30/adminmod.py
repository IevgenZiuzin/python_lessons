import numbmenu
import authorize


class Admin_mod:

    @staticmethod
    def users_mod():
        auth = authorize.init()
        u = auth.load_users()
        menu_items = ("Add", "Edit", "Remove", "Save", "Show all",
                      "Search ID", "Search value")
        commands = (u.add, u.edit, u.remove, u.save, u.show_all,
                    u.search_id, u.search_match)

        menu = numbmenu.init(menu_items, commands)
        menu.run()

    @staticmethod
    def tests_mod():
        auth = authorize.init()
        t = auth.load_tests()
        menu_items = ("Add", "Edit", "Remove",
                      "Search by name", "Show all")
        commands = (t.add, t.edit, t.remove, t.search, t.show_all)
        menu = numbmenu.init(menu_items, commands)
        menu.run()

    @staticmethod
    def stats_mod():
        pass


def init():
    return Admin_mod()
