"""
Дан текстовый файл. Найти длину самой длинной строки.
"""


def flines(f):
    file = open(f)
    lines = list(map(lambda i: i.strip(), file.readlines()))
    file.close()
    return lines


path_1 = "text_1.txt"
rows = flines(path_1)

rows_length = list(map(len, rows))
longest_row = max(rows_length)
index = rows_length.index(longest_row)

print(f"Longest row: \"{rows[index]}\"")
print(f"Longest row length: {longest_row}")
print("\nOrigin: \n")
for i in rows:
    print(i)


