"""Пользователь вводит с клавиатуры номер месяца (от 1 до 12). В зависимости от полученного номера месяца
программа выводит на экран надпись:
Winter (если введено значение 1,2 или 12),
Spring (если введено значение от 3 до 5),
Summer (если введено значение от 6 до 8),
Autumn (если введено значение от 9 до 11).
Если пользователь ввел значение не в диапазоне от 1 до 12 требуется вывести сообщение об ошибке."""

month_numbers = [str(n) for n in range(1, 13)]
alert = "Wrong value. Try again."

while True:
    month_number = input("Type number of month: ")
    if month_number not in month_numbers:
        print(alert)
        break
    else:
        if month_number in month_numbers[2:5]:
            season = "Spring"
        elif month_number in month_numbers[5:8]:
            season = "Summer"
        elif month_number in month_numbers[8:11]:
            season = "Autumn"
        else:
            season = "Winter"
    print("\nMonth %s refers to %s.\n" % (month_number, season))
    request = input("\nAgain? (y): ")
    if request != "y":
        break
