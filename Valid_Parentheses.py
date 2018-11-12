dic = {'(': ')', '[': ']', '{': '}'}
cache = []


def isvalid1(s):
    s = list(s)
    if not s:
        return True
    if dic.__contains__(s[0]):
        cache.append(s[0])
    else:
        return False
    for item in s[1:]:
        if dic.__contains__(item):
            cache.append(item)
        elif not cache:
            return False
        elif item == dic[cache[-1]]:
            cache.pop()
        else:
            return False
    if not cache:
        return True
    else:
        return False


def isvalid2(s):
    n = len(s)
    if n == 0:
        return True
    if n % 2 != 0:
        return False
    while '()' in s or '[]' in s or '{}' in s:
        s = s.replace('()', '').replace('[]', '').replace('{}', '')
    if s == '':
        return True
    else:
        return False


def isvalid3(s):
    stack = []
    dict = {"]": "[", "}": "{", ")": "("}
    for char in s:
        if char in dict.values():
            stack.append(char)
        elif char in dict.keys():
            if not stack or dict[char] != stack.pop():
                return False
        else:
            return False
    return not stack

# print(isvalid1(''))
print(isvalid3('{)'))



