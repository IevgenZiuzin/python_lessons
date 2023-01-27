"""Пользователь вводит с клавиатуры три цифры. Необходимо создать число, содержащее эти цифры.
Например, если с клавиатуры введено 1, 5, 7, тогда нужно сформировать число 157."""

digits = [str(n) for n in range(0, 10)]
inputs = 3
user_digits = []

for i in range(inputs):
    user_digit = input("Type digit: ")
    if user_digit not in digits:
        print(user_digit, "is not a digit.")
        continue
    else:
        user_digits.append(user_digit)
if user_digits:
    user_integer = int("".join(user_digits))
    print("Your integer is %d. Next is %d." % (user_integer, user_integer + 1))
else:
    print("Lets\'s try from very beginning. Remember to input digits only.")
