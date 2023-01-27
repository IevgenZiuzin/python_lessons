import sys


class Menu:
    instances = 0

    def __init__(self, titles, commands):
        if len(titles) != len(commands):
            print('Titles and commands amounts are not equal.')
            return
        else:
            self.titles = titles
            self.commands = commands
            self.query = ""
            self._return = False
            if self.__class__.instances >= 1:
                self.titles.append("Return")
                self._return = True
            self.__class__.instances += 1

    def display(self):
        last_num = 0
        quit_num = 0
        for number, title in enumerate(self.titles, 1):
            print(f"{number}.{title}", end="  ")
            last_num = number
            quit_num = number + 1
        print(f"{quit_num}.Quit")
        self.query = input("\n: ")
        if not self.query.isdigit():
            return
        if int(self.query) == last_num and self._return:
            return
        if int(self.query) == quit_num:
            sys.exit()
        self.run()

    def run(self):
        for index, command in enumerate(self.commands, 1):
            if self.query == str(index):
                try:
                    command()
                except TypeError:
                    print(f"TypeError: {command} is not a function.")
                    return
        self.display()


def init(titles, commands):
    return Menu(titles, commands)
