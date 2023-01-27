import menu


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Q:
    limit = 3

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def first(self):
        return self.head.data if self.head else None

    def __len__(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def __is_empty(self):
        return self.head is None

    def is_empty(self):
        print(self.__is_empty())

    def __is_full(self):
        return self.size == self.__class__.limit

    def is_full(self):
        print(self.__is_full())

    def show(self):
        if self.head:
            print(f'Your strings:')
            item = self.head
            while item is not None:
                print(item.data)
                item = item.next
        else:
            print(f'Queue is empty')

    def __enqueue(self, data):
        if not self.tail:
            self.head = Node(data)
            self.tail = self.head
            self.size += 1
        else:
            self.tail.next = Node(data)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            self.size += 1

    def enqueue(self):
        if self.size == self.__class__.limit:
            print(f'Queue is full')
            return
        s = input(f'Type string: ')
        self.__enqueue(s)

    def __dequeue(self):
        if not self.head:
            return None
        else:
            item = self.head.data
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return item

    def dequeue(self):
        print(self.__dequeue())


q = Q()
titles = ['Is Empty', 'Is full', 'Enqueue', 'Dequeue', 'Show']
commands = [q.is_empty, q.is_full, q.enqueue, q.dequeue, q.show]
main = menu.init(titles, commands)
main.run()