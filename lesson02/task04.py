"""Напишите программу, вычиляющую площадь треугольника. Пользователь с клавиатуры вводит
размер основания треугольника и высоты."""

while True:
    base = float(input("Input triangle base value as integer or float: "))
    height = float(input("Input triangle height value as integer or float: "))
    print("\nTriangle area equals: %.2f square units"
          % ((base * height) / 2))
    request = input("Again? (y): ")
    if request != "y":
        break
