import random
import time
from threading import Thread, Barrier

desc="""
При старте приложения запскаются три потока.
Первый поток заполняет список случайными числами.
Два других потока ожидают заполнения.
Когда список заполнен, оба потока запскаются.
Первый поток наодит сумму элеметов списка,
второй поток - среднеарифметическое значение в списке.
Полученный список, сумма и среднеарифметическое выводятся на экран.
"""

b = Barrier(2)
ls = []


def fulfill_list():
    global ls
    time.sleep(2)
    ls = [random.randint(1, 5) for _ in range(4)]
    # b.wait()
    print(f'List: {ls}')


def sum_of_list():
    global ls
    print(f'Sum: {sum(ls)}')


def average_list():
    global ls
    print(f'Average: {sum(ls) / len(ls)}')


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    fulfil_thread = Thread(target=fulfill_list)
    fulfil_thread.start()
    fulfil_thread.join()
    # b.wait()
    sum_thread = Thread(target=sum_of_list).start()
    average_thread = Thread(target=average_list).start()







