# method str
# def isPalindrome(x):
#     """
#     :type x: int
#     :rtype: bool
#     """
#     if x < 0:
#         return False
#     else:
#         s = str(x)
#         if s[::-1] == s:
#             return True
#         else:
#             return False
#
#
# print(isPalindrome(-21))



# method without str
def isPalindrome(x):
    if x < 0:
        return False
    cache = []
    t = x
    while t / 10 != 0:
        cache.append(t % 10)
        t = t // 10
    sum = 0
    count = 0
    for i in cache[::-1]:
        sum += i * (10 ** count)
        count += 1
    if sum == x:
        return True
    else:
        return False
print(isPalindrome(12231))