import string
digs = string.digits + string.ascii_letters

def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)


for val in range(1, 51):
    found_match = False
    for base1 in range(2, 10):
        for base2 in range(base1, 11):
            if int2base(val, base2) in int2base(val, base1):
                print(val)
                found_match = True
                break
        if found_match:
            break
