# Создайте реализацию паттерна Command. Протестируйте работу созданного класса.

from abc import ABC, abstractmethod
from typing import List


class ICommand(ABC):
    @abstractmethod
    def execute(self) -> None:
        ...


class Engine:
    def __init__(self):
        self.state = False


class RegularStart(Engine):

    def start(self):
        self.state = True
        print('Engine has been started in regular mode.')


class EmergencyStart(Engine):

    def start(self):
        self.state = True
        print('Engine has been started in emergency mode.')


class StartCommand(ICommand):
    def __init__(self, executor):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.start()


class Invoker:
    def __init__(self):
        self.history: List[ICommand] = []

    def add_command(self, command: ICommand) -> None:
        self.history.append(command)

    def run(self) -> None:
        if not self.history:
            print("Is empty")
        else:
            for executor in self.history:
                executor.execute()
        self.history.clear()


if __name__ == "__main__":
    invoker = Invoker()
    query = input('Start engine in emergency mode?(y/n)\n: ').lower()
    if query != 'y':
        invoker.add_command(StartCommand(RegularStart()))
    else:
        invoker.add_command(StartCommand(EmergencyStart()))
    invoker.run()