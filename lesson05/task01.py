# Вывести на экран фигуры, заполненные звездочками.
# Диалог с пользователем реализовать при помощи меню.

width = 10
half_width = int(width / 2)

sign = " * "
space = "---"

# a
print("\n A \n")
for i in range(1, (width + 1)):
    increment = space * i
    decrement = sign * (width - i)
    print(increment, decrement)

# b
print("\n B \n")
for i in range(1, (width + 1)):
    increment = sign * i
    decrement = space * (width - i)
    print(increment, decrement)

# c
print("\n C \n")
for i in range(1, (half_width + 1)):
    increment = space * i
    decrement = sign * (width - 2 * i)
    print(increment, decrement, increment)

# d
print("\n D \n")
for i in range(half_width):
    increment = sign * i * 2
    decrement = space * (half_width - i)
    print(decrement, increment, decrement)

# e
print("\n E \n")
for i in range(1, (half_width + 1)):
    increment = space * i
    decrement = sign * (width - 2 * i)
    print(increment, decrement, increment)
for i in range(half_width):
    increment = sign * i * 2
    decrement = space * (half_width - i)
    print(decrement, increment, decrement)
#f
print("\n F \n")
for i in range(1, (half_width + 1)):
    increment = sign * i
    decrement = space * (width - 2 * i)
    print(increment, decrement, increment)
for i in range(half_width):
    increment = space * i * 2
    decrement = sign * (half_width - i)
    print(decrement, increment, decrement)
#g
print("\n G \n")
for i in range(1, half_width + 1):
    increment = sign * i
    decrement = space * (width - i)
    print(decrement, increment)
for i in range(half_width):
    increment = space * (half_width + i)
    decrement = sign * (half_width - i)
    print(increment, decrement)
#h
print("\n H \n")
for i in range(1, (half_width + 1)):
    increment = sign * i
    decrement = space * (width - 2 * i)
    print(increment, decrement, increment)
for i in range(half_width):
    increment = space * i * 2
    decrement = sign * (half_width - i)
    print(decrement, increment, decrement)
# i
print("\n I \n")
for i in range(1, (width + 1)):
    increment = space * i
    decrement = sign * (width - i)
    print(decrement, increment)

# j
print("\n J \n")
for i in range(1, (width + 1)):
    increment = sign * i
    decrement = space * (width - i)
    print(decrement, increment)
