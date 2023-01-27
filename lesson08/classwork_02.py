# Користувач заповнює список рандомними елементами
# (числа, букви.. )
# якщо введе пробіл(символ) то введення зупинється та показує на екран:
# сумму чисел, обєднання строк, avg. чисел, має показати два списки,
# які мають числа і строки першого списку, і вивести значення списків
# в вигляді пар тобто : [2,5,9,0,1,9], ["as","sd","gf","fd"]
# as = 2
# sd = 5
# gf = 9
# fd = 0


strings = []
numbers = []
average = "No numbers"

while True:
    el = input("Type element: ")
    if el == "":
        break
    else:
        try:
            numbers.append(int(el))
        except:
            strings.append(el)


if len(numbers) > 0:
    average = sum(numbers) / len(numbers)

shorter = min(len(strings), len(numbers))

for i in range(shorter):
    print(f"{strings[i]} = {numbers[i]}")

print(f"Sum of numbers: {sum(numbers)}")
print(f"Average of numbers: {average}")
print(f"Strings joined: {' '.join(strings)}")
print(f"Strings: {strings}\nNumbers: {numbers}")
