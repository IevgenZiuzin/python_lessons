"""Пользователь водит шестизначное число. Необходимо поменять в этом числе первую и шестую цифры, а также
вторую и пятую цифры. например, 723895 должно превратиться в 593827.
Если ползователь ввел не шестизначное число требуется вывести сообщение об ошибке."""

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
            user_digits.append(user_number[i])
    if len(user_digits) == input_len:
        print("".join(user_digits), "became:")

        user_digits[0], user_digits[len(user_digits)-1] = user_digits[len(user_digits)-1], user_digits[0]
        user_digits[1], user_digits[len(user_digits) - 2] = user_digits[len(user_digits) - 2], user_digits[1]

        print("".join(user_digits))

        request = input("Again? (y): ")
        if request != "y":
            break
    else:
        print(alert)

