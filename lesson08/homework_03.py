print("""Пользователь с клавиатуры вводит элементы списка целых и некоторое число.
Необходимо посчитать сколько раз данное число присутствует в списке.
Результат вывести на экран.""")


def collect_integers():
    integers = []
    print(f'not integer for stop adding')
    while True:
        integer = input("Add: ")
        try:
            integers.append(int(integer))
        except ValueError:
            break
    return integers


def count_occur(integers):
    counted = input('\nInteger to count: ')
    print(f'List: {integers}')
    try:
        print(f'\nOccurrences of {counted}: {integers.count(int(counted))}')
    except ValueError:
        print(f'Not integer')


if __name__ == '__main__':
    count_occur(collect_integers())


