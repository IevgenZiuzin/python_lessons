num = int(input("Input number of signs: "))

side = 8
step = int(side / 2)
black = "*" * num
white = "_" * num

for x in range(side):
    if x % 2 == 0:
        for y in range(step):
            print(white, black, sep="", end="")
    else:
        for y in range(step):
            print(black, white, sep="", end="")
    print("\n")
