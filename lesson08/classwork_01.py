# Пользователь вводит с клавиатуры арифметическое выражение. Например, 23+12.
# Необходимо вывести на экран результат выражения. В нашем примере это 35.
# Арифметическое выражение может состоять только из трёх частей:
# число, операция, число. Возможные операции: +, -,*,/

import re

expression = input("Type arithmetic expression using integers and +-*/ operators: ")
numbers = re.split(r"[+\-*/]", expression)
print(numbers)
sign = re.findall("\D", expression)[0]
a = int(numbers[0])
b = int(numbers[1])
if sign == "+":
    result = a + b
elif sign == "-":
    result = a - b
elif sign == "*":
    result = a * b
elif sign == "/":
    result = a / b
print(result)
