# Дана шахматная доска размером 8х8 и шахматный конь.
# Программа должна запросить у пользователя координаты клетки поля и поставить туда коня.
# Задача программы найти и вывести путь коня, при котором обойдет все клетки доски,
# становясь в каждую клетку только один раз.
# (Так как процесс отыскания пути для разных начальных клеток может затянуться,
# то рекомендуется сначала опробовать задачу на поле размером 6х6).
# В программе необходимо использовать рекурсию.


row = [2, 1, -1, -2, -2, -1, 1, 2, 2]
col = [1, 2, 2, 1, -1, -2, -2, -1, 1]



def isValid(x, y):
    return not (x < 0 or y < 0 or x >= N or y >= N)



def knightTour(visited, x, y, pos):

    visited[x][y] = pos
    if pos >= N * N:
        for r in visited:
            print(r)
        print()
        visited[x][y] = 0
        return

    for k in range(8):
        newX = x + row[k]
        newY = y + col[k]
        if isValid(newX, newY) and visited[newX][newY] == 0:
            knightTour(visited, newX, newY, pos + 1)
    visited[x][y] = 0


if __name__ == '__main__':
    N = 5
    visited = [[0 for x in range(N)] for y in range(N)]
    pos = 1

    knightTour(visited, 0, 0, pos)
