"""Пользователь вводит с клавиатуры колиество метров. Требуется вывести результат перевода метров
в сантиметры. дециметры. миллимеры, мили."""

cm = 100
dm = 10
mm = 1000
miles = 0.000621371

while True:
    meters = float(input("Input meters value as integer or float: "))
    if not isinstance(meters, float):
        print(meters, "is not a number. Try again.")
    else:
        print("\n%.2f meters equals:\n\n%.2f centimeters\n%.2f decimeters\n%.2f millimeters\n%.2f miles:"
              % (meters, meters*cm, meters*dm, meters*mm, meters*miles)
              )
    request = input("Again? (y): ")
    if request != "y":
        break


