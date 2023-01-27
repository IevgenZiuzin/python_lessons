import datetime as d


def duration(f):
    def inner():
        t1 = d.datetime.now()
        primes = f()
        t2 = d.datetime.now()
        print(f'Duration: {t2 - t1}')
        print(f'Primes: {primes}')
        return f()
    return inner


@duration
def get_primes():
    primes = []
    for i in range(1000):
        if i > 1:
            for k in range(2, i):
                if i % k == 0:
                    break
            else:
                primes.append(i)
    return primes


get_primes()


