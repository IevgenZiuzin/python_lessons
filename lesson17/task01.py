def is_valid_IP(strng):
    a = strng.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        if len(x) > 1 and x[0] == "0":
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True


test = "123.045.067.089"
print(is_valid_IP(test))
