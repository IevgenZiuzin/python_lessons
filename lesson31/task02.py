import menu


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.item)


class Stack:
    limit = 0

    def __init__(self):
        self.top = None
        self.__size = 0

    def push(self):
        x = input('Type string for stack: ')
        node = Node(x)
        if node is None:
            print('Heap overflow')
            return
        if self.__size < self.__class__.limit:
            node.next = self.top
            self.top = node
            self.__size += 1
            print(f'String \"{x}\" added.')

    def pop(self):
        if self.top is None:
            print('Stack overflow')
            return
        top = self.top.item
        self.top = self.top.next
        self.__size -= 1
        print(top)
        return top

    def is_empty(self):
        print(self.top is None)
        return self.top is None

    def is_full(self):
        print(self.__size == self.__class__.limit)
        return self.__size == self.__class__.limit

    def get_top(self):
        if self.top:
            print(self.top.item)
        else:
            print('Stack is empty!')

    def size(self):
        print(self.__size)

    def clear(self):
        self.top = None
        self.__size = 0


stack = Stack()
titles = ['Push', 'Pop', 'Size', 'Is empty', 'Is full', 'Clear', 'Get top']
commands = [stack.push, stack.pop, stack.size, stack.is_empty, stack.is_full, stack.clear, stack.get_top]
m = menu.init(titles, commands)
m.run()

