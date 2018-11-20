import re
def myAtoi(str):    # 正则表达式学习
    """
    :type str: str
    :rtype: int
    """
    # str = str.replace(' ', '')
    # # str = str.replace('+', '')
    # _str_ = 0
    # symbol = 1
    # if str.__len__() is 0:
    #     return 0
    # for i in str:
    #     if i == '-':
    #         symbol = -symbol
    # str = str.replace('-', '')
    # if str.__len__() is 0:
    #     return 0
    # if str[0] > '9' or str[0] < '0':
    #     return 0
    # else:
    #     for i in range(str.__len__()):
    #         if str[i] > '9' or str[i] < '0':
    #             _str_ = str[: i]
    #             break
    #         else:
    #             _str_ = str[: i + 1]
    #     if int(_str_) > 2 ** 31:
    #         return 2147483648 * symbol
    #     return int(_str_) * symbol
    str = str.strip()
    str = re.findall('(^[\+\-0]*\d+)\D*', str)
    # result = int(''.join(str))
    try:
        result = int(''.join(str))
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        if result > MAX_INT > 0:
            return MAX_INT
        elif result < MIN_INT < 0:
            return MIN_INT
        else:
            return result
    except:
        return 0


print(myAtoi("+    1"))




