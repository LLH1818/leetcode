def lengthOfLongestSubstring(s):    # 快速的解法和我的思想一直，它利用字典，查找速度变快
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0
    cache = []
    result = []
    for i in range(s.__len__()):
        if s[i] not in cache:
            cache.append(s[i])
        else:
            result.append(cache.__len__())
            cache = cache[cache.index(s[i]) + 1:]
            cache.append(s[i])
        result.append(cache.__len__())
    return max(result)


print(lengthOfLongestSubstring("dvdf"))

