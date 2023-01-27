def check_palindrome(n):
    if str(n).isdecimal() and len(str(n)) % 2 == 0:
        n = str(n)
        length = int(len(n) / 2)
        return n[:length] == n[:length - 1:-1]


print(check_palindrome(1122))
print(check_palindrome(1212))
print(check_palindrome(12344321))
