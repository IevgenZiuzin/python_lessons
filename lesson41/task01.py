import random
import json
import time
from threading import Thread

desc = """
Користувач вводить з клавітури шлях о файлу. Після чого запучкються три потоки.
Перший потік запоінює файл випадковими числами. Два інші очікують на заповнення.
Коли файл заповнений, обидва потоки стартують.
Перший потік знаходить усі прості числа,
Другий потік знаходить факторіал кожного чила у файлі.
Результати пошуку кожен потік має записати у новий файл.
Виведіть на екран статистику виконаних операцій.
"""


def file_read(path):
    with open(path, 'r') as file:
        return json.loads(file.read())


def file_write(path, body):
    with open(path, 'w') as file:
        file.write(json.dumps(body))


def random_list():
    return [random.randint(1, 11) for _ in range(10)]


def is_prime(number):
    for i in range(2, number):
        if (number % i) == 0:
            return False
    return True


def factorial(number):
    if number == 1:
        return number
    return number * factorial(number - 1)


def get_primes(ls):
    return [i for i in ls if is_prime(i)]


def get_factorials(ls):
    return [factorial(n) for n in ls]


def user_path():
    while True:
        query = input('Your path (.json): ')
        if query != '':
            return query


def fulfill_list(path):
    time.sleep(2)
    file_write(path, random_list())


def primes_of_list(source_path, target_path):
    ls = file_read(source_path)
    file_write(target_path, get_primes(ls))


def factorials_of_list(source_path, target_path):
    ls = file_read(source_path)
    file_write(target_path, get_factorials(ls))


def display_files(*paths):
    for path in paths:
        print(f'In \"{path}\": {file_read(path)}')


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    primes_path = 'primes.json'
    factorial_path = 'factorials.json'
    users_path = user_path()
    threads = [Thread(target=fulfill_list, args=(users_path,)),
               Thread(target=primes_of_list, args=(users_path, primes_path,)),
               Thread(target=factorials_of_list, args=(users_path, factorial_path,)),
               Thread(target=display_files, args=(users_path, primes_path, factorial_path,))]
    for thread in threads:
        thread.start()
        thread.join()
