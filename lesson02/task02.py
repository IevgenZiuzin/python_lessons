"""Пользователь вводит с клавиатуры число, состоящее из четырех цифр. Требуется найти произведение цифр.
Например, если с клавиатуры введено 1324, тогда результат произведения 1*3*2*4=24."""

digits = [str(n) for n in range(0, 10)]
inputs_len = 4
user_digits = []
alert = "Wrong value"

user_number = input("Type four-digit number: ")
if len(user_number) != inputs_len:
    print(alert)
else:
    for i in range(len(user_number)):
        if user_number[i] not in digits:
            continue
        else:
            user_digits.append(user_number[i])
if len(user_digits) == inputs_len:
    user_integer = 1
    for i in range(len(user_digits)):
        user_integer *= int(user_digits[i])
    print("Product of your number digits is %d. Next is %d." % (user_integer, user_integer + 1))
else:
    print(alert)
