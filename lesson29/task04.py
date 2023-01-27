import datetime as d


def set_range(f):
    def inner(a, b):
        start = min(a, b)
        end = max(a, b)
        result = [i for i in f() if start <= i <= end]
        if result:
            print(f'Primes in range from {start} to {end}: {result}')
        else:
            print('No primes in this range. Select in (0, 1000), please.')
        return result
    return inner


def duration(f):
    def inner():
        t1 = d.datetime.now()
        primes = f()
        t2 = d.datetime.now()
        print(f'Primes: {primes}')
        print(f'Founded in duration: {t2 - t1}')
        return primes
    return inner


@set_range
@duration
def get_primes():
    primes = []
    for i in range(1000):
        if i > 0:
            for k in range(2, i):
                if i % k == 0:
                    break
            else:
                primes.append(i)
    return primes


get_primes(10, 20)
