# def longestCommonPrefix(strs):
#     """
#     :type strs: List[str]
#     :rtype: str
#     """
#     result = ''
#     pre = []
#     min = 100
#     if strs == []:
#         return ''
#     for i in strs:
#         if min > i.__len__():
#             min = i.__len__()
#     for i in range(min):
#         temp = strs[0][i]
#         for word in strs:
#             if temp is not word[i]:
#                 return result
#         pre.append(temp)
#         result = ''
#         for i in pre:
#             result += i
#     return result
#
#
# print(longestCommonPrefix([]))

# 大神作品
def longestCommonPrefix(strs):
    if not strs:
        return ''
    for i, letter_group in enumerate(zip(*strs)):
        if len(set(letter_group)) > 1:
            return strs[0][:i]
    else:
        return min(strs)


print(longestCommonPrefix(['']))
