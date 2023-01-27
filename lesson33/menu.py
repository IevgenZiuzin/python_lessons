import sys


class Menu:
    instances = 0

    def __init__(self, titles, commands):
        if len(titles) != len(commands):
            print('Titles and commands amount are not equal.')
            return
        else:
            self.titles = titles
            self.commands = commands
            self.query = ""
            self.end = True
            self.added_return = False
            if self.__class__.instances > 0:
                self.titles.append("Return")
                self.added_return = True
            self.__class__.instances += 1

    def display(self):
        last = 0
        for number, title in enumerate(self.titles, 1):
            print(f"{number}.{title}", end="  ")
            last = number
        print(f"{last + 1}.Quit")
        self.query = input("")
        if self.query.isdigit():
            if int(self.query) == last and self.added_return:
                return
            if int(self.query) == last + 1:
                sys.exit()
            self.run()
        else:
            sys.exit()

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
