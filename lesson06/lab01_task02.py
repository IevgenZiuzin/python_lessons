# Показать на экран все простые числа в диапазоне, указанном пользователем. Число
# называется простым, если оно делится без остатка только на себя и на единицу.
# Например, три — это простое число, а четыре нет.

try:
    sequence = [int(input("Type START integer of range: ")), int(input("Type END integer of range: "))]
    primes = []

    start = min(sequence)
    end = max(sequence)

    for i in range(start, end + 1):
        if i > 1:
            for k in range(2, i):
                if (i % k) == 0:
                    break
            else:
                primes.append(i)
    if primes:
        print(f"Primes in range {start} to {end}: {', '.join(map(str, primes))}")
    else:
        print("No primes in this range")
except TypeError:
    print("wrong value")
