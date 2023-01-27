"""Пользователь водит с клавиатуры целое шестизначное число. Нписать программу, которая определяет,
является ли введенно ечисло - счастливым (Счастливым считается шестизначное число, у которого
сумма первых трех цифр равна сумме вторых трех цифр).
Например, 123321 - счастливое число.
Если пользователь ввел не шестизначное число требуется вывести сообщение об ошибке"""

digits = [str(n) for n in range(0, 10)]
input_len = 6
alert = "Not six-digit number. Try again."

while True:
    user_number = input("Input six-digit number: ")
    user_digits = []
    for i in range(len(user_number)):
        if user_number[i] not in digits:
            continue
        else:
            user_digits.append(int(user_number[i]))
    if len(user_digits) == input_len:
        if sum(user_digits[:int(input_len/2)]) == sum(user_digits[int(input_len/2):]):
            print("It\'s happy number!")
        else:
            print("It\'s not happy number.")
    else:
        print("Wrong value. Try Again.")
    request = input("Again? (y): ")
    if request != "y":
        break
