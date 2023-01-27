import random as r

arr = [r.randint(-5, 4) for i in range(7)]


def max_sequence(n):
    seq = []
    for i in n:
        if i > sum(seq) and i > 0:
            seq = n[n.index(i):]
    for k in range(len(seq), -1, -1):
        if sum(seq) < sum(seq[:k]):
            seq.pop()
    return sum(seq)


print(arr)
print(max_sequence(arr))


def kadane(A):

    max_so_far = 0
    max_ending_here = 0

    for i in A:
        max_ending_here = max_ending_here + i
        max_ending_here = max(max_ending_here, 0)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


print(kadane(arr))