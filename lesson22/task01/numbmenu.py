class Menu:
    def __init__(self, titles, commands):
        self.titles = titles
        self.commands = commands
        self.query = ""

    def menu(self):
        last = 0
        for number, title in enumerate(self.titles):
            print(f"{number + 1}.{title}", end="  ")
            last = number + 1
        print(f"{last + 1}. Quit")
        self.query = input("")
        try:
            if isinstance(int(self.query), int):
                self.send()
        except ValueError:
            return

    def send(self):
        if self.query is None or int(self.query) > len(self.commands):
            return
        for index, command in enumerate(self.commands):
            if self.query == str(index + 1):
                try:
                    command()
                except TypeError:
                    print(f"TypeError: {command} is not a function.")
                    return
            else:
                continue
        self.menu()

    def run(self):
        self.menu()


def init(t, c):
    return Menu(t, c)
