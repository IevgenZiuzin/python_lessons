def get_even_in_range(m, n):
    arr = [i for i in range(min(m, n), max(m, n)) if i % 2 == 0]
    print(*arr)


get_even_in_range(-10, 35)
