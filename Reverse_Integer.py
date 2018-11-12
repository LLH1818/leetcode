def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    minus = 0
    if x < 0:
        minus = 1
        x = -x
    temp = 0
    while x / 10 != 0:
        temp = temp * 10
        temp += x % 10
        x = x // 10
    if temp > 2**31 - 1 or temp < -(2**31):
        return 0
    if minus == 1:
        return -temp
    else:
        return temp


def reverse1(x):
    a = str(x)
    b = a[::-1]
    return int(str(x)[::-1])


print(reverse1(1234))