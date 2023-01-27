def square(side, sign, filled=1, squarer=2):
    sign = str(sign)
    space = " "
    for i in range(side):
        for k in range(side * squarer):
            if filled:
                print(sign, end="")
            else:
                if i == 0 or i == side - 1 or k == 0 or k == (side * squarer) - 1:
                    print(sign, end="")
                else:
                    print(space, end="")
        print("")


square(5, 5, 0)
