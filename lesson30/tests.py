import json
import test
import task


class Tests(dict):
    path = 'tests.txt'

    def __init__(self, d=None):
        super().__init__()
        if type(d) == dict:
            self.update(d)

    @staticmethod
    def write(n, t, f):
        file = open(n, f)
        file.write(t)
        file.close()

    @staticmethod
    def read(f):
        file = open(f)
        text = file.read()
        file.close()
        return text

    @staticmethod
    def create_task():
        question = input('Question: ')
        variants = []
        while True:
            variant = input('Variant: ')
            if variant == '':
                break
            variants.append(variant)
        if not variants:
            return
        while True:
            print(variants)
            answer = input('Answer: ')
            if answer in variants:
                return task.init(question, variants, answer)
            else:
                return False

    @staticmethod
    def create_test():
        name = input('Name: ')
        tasks = []
        while True:
            t = Tests.create_task()
            if t:
                tasks.append(t)
            else:
                break
        return test.init({'name': name, 'tasks': tasks})

    def save(self):
        self.__class__.write(self.__class__.path, json.dumps(self), "w")
        print("Saved")

    def switch_adding(self, c):
        b = input('1. Add manually 2. Add from file.py\n')
        if b == '1':
            self[c].append(self.__class__.create_test())
            self.save()
        elif b == '2':
            p = input('Type test file.py path: ')
            t = self.__class__.read(p)
            self[c].append(test.init(t))
            self.save()
        else:
            return

    def add(self):
        for n, i in enumerate(self):
            print(f'{n}. i')
        c = input('Type category: ')
        if self.get(c):
            self.switch_adding(c)
        else:
            q = input(f'Category \"{c}\" not found. Add it? (y/n): ')
            if q == 'y':
                self[c] = []
                self.switch_adding(c)
            else:
                return

    def edit(self):
        pass

    def remove(self):
        pass

    def search(self):
        pass

    def show_all(self):
        pass


def init(d=None):
    return Tests(d)
