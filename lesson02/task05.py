"""Пользователь с клавиатуры вводит четырехзначное число. Необходмо перевернуть исло и отобразить результат.
Например, если введено 4512б результат 2154."""


digits = [str(n) for n in range(0, 10)]
inputs_len = 4
alert = "Not four-digit number. Try again."

while True:
    user_digits = []
    user_number = input("Type four-digit number: ")
    if len(user_number) != inputs_len:
        print(alert)
        break
    for i in range(len(user_number)-1, -1, -1):
        if user_number[i] not in digits:
            break
        else:
            user_digits.append(user_number[i])
    if len(user_digits) == inputs_len:
        user_integer = int("".join(user_digits))
        print("Your integer is %d. Next is %d." % (user_integer, user_integer + 1))
        request = input("Again? (y): ")
        if request != "y":
            break
    else:
        print(alert)
        break
