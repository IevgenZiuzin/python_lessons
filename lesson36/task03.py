from abc import ABC, abstractmethod
from typing import List
from tabulate import tabulate


class ICommand(ABC):
    @abstractmethod
    def execute(self) -> None:
        ...

class Account:
    def __init__(self, account, amount):
        self.account = account
        self.amount = amount

class Withdraw(Account, ICommand):
    def execute(self):
        self.account.balance -= self.amount

class Income(Account, ICommand):
    def execute(self):
        self.account.balance += self.amount


class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

class Bank:
    def __init__(self):
        self.commands: List[ICommand] = []

    def operation(self, account, amount):
        Command = Withdraw if amount < 0 else Income
        command = Command(account, abs(amount))
        command.execute()
        self.commands.append(command)

    def show_operations(self):
        output = []
        for command in self.commands:
            output.append(
                {'operation': command.__class__.__name__.lower(),
                 'account': command.account._name,
                 'amount': command.amount}
            )
        print(tabulate(output))


bank = Bank()
account1 = BankAccount('Eugen')
bank.operation(account1, 1000)
bank.operation(account1, -50)
account2 = BankAccount('Lida')
bank.operation(account2, 500)
bank.operation(account2, -100)
bank.operation(account2, 150)
bank.show_operations()
print(tabulate([account1.__dict__, account2.__dict__]))
