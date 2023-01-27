import menu


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.item)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        count = 0
        i = self.head
        while i:
            count += 1
            i = i.next
        return count

    def get_number(self):
        item = input(f'Type number: ')
        if not item.isdigit():
            return
        return int(item)

    def is_empty(self):
        return self.head is None

    def __exist(self, item):
        i = self.head
        while i:
            if i.item == item:
                return True
        return False

    def exist(self):
        item = self.get_number()
        if item:
            print(self.__exist(item))

    def travel_forward(self):
        cur = self.head
        while cur:
            print(f'{cur.item} ==> ', end='')
            cur = cur.next
        print('None')

    def travel_reverse(self):
        cur = self.tail
        while cur:
            print(f'{cur.item} ==> ', end='')
            cur = cur.prev
        print('None')

    def add_to_back(self):
        item = input('Type number: ')
        if not item.isdigit():
            return
        item = int(item)
        node = Node(item)
        if self.head is None:
            self.head = node
            self.tail = node
        elif self.__exist(item):
            print(f'{item} is already present')
            return
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def __remove_occ(self, key):
        if self.is_empty():
            print('List empty')
            return
        cur = self.head
        while cur is not None and cur.item != key:
            cur = cur.next
        if cur is None:
            return

        prev = cur.prev
        if cur.next is None:
            self.tail = prev

        if prev is None:
            self.head = cur.next
            if self.head is not None:
                self.head.prev = None
        else:
            prev.next = cur.next
            cur.prev = None
            if prev.next is not None:
                prev.next.prev = prev
        self.remove_occ(key)

    def remove_occ(self):
        item = self.get_number()
        if item:
            self.__remove_occ(item)

    def __replace_first(self, key, item):
        if self.head is None:
            print('List empty')
            return
        cur = self.head
        while cur and cur.item != key:
            cur = cur.next
        if cur is None:
            return
        cur.item = item
        return True

    def __replace_all(self, key, item):
        while True:
            if not self.__replace_first(key, item):
                break

    def replace_first(self):
        key = input('Type key: ')
        item = input('Type item: ')
        if not key.isdigit() or not item.isdigit():
            return
        self.__replace_first(int(key), int(item))

    def replace_all(self):
        key = input('Type key: ')
        item = input('Type item: ')
        if not key.isdigit() or not item.isdigit():
            return
        self.__replace_all(int(key), int(item))


dl = DoublyLinkedList()
titles = ['Add', 'Remove all occurrences', 'Display forward', 'Display reverse', 'Check existing', 'Replace first', 'Replace all']
commands = [dl.add_to_back, dl.remove_occ, dl.travel_forward, dl.travel_reverse, dl.exist, dl.replace_first, dl.replace_all]
main = menu.init(titles, commands)
main.run()



