# Создайте реализацию паттерна Command. Протестируйте работу созданного класса.

from abc import ABC, abstractmethod
from typing import List


class ICommand(ABC):
    @abstractmethod
    def execute(self) -> None:
        ...


class Number:
    def __init__(self, number: float):
        self.number = number


class RaiseTwoTimes(Number):

    def get_result(self):
        print(self.number ** 2)
        return self.number ** 2


class RaiseThreeTimes(Number):

    def get_result(self):
        print(self.number ** 3)
        return self.number ** 3


class GetResultCommand(ICommand):
    def __init__(self, executor):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.get_result()


class Invoker:
    def __init__(self):
        self.history: List[ICommand] = []

    def addCommand(self, command: ICommand) -> None:
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
    invoker.addCommand(GetResultCommand(RaiseTwoTimes(3)))
    invoker.addCommand(GetResultCommand(RaiseThreeTimes(3)))
    invoker.run()

