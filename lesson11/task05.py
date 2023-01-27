def get_product_in_range(m, n):
    arr = [i for i in range(min(m, n), max(m, n) + 1)]
    result = 1
    for c in arr:
        result *= c
    return result


print(get_product_in_range(1, 4))
