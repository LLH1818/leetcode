def maxArea1(height):
    """
    :type height: List[int]
    :rtype: int
    """
    global_max = 0
    for i in range(height.__len__()):
        for j in range(height.__len__() - i - 1):
            local_max = (j + 1) * min(height[i], height[i + j + 1])
            if local_max > global_max:
                global_max = local_max
    return global_max


def maxArea2(height):   # 将长度这个参数固定下来，长度从最长逐渐缩短，深度必须要变深
    """
    :type height: List[int]
    :rtype: int
    """
    if not height:
        return 0
    i, j = 0, len(height) - 1
    cache = [(j - i) * min(height[i], height[j])]
    for t in range(len(height) - 1):
        if height[i] < height[j]:
            i += 1
            if height[i] > height[i - 1]:
                cache.append(min(height[i], height[j]) * (j - i))
        else:
            j = j - 1
            if height[j] > height[j + 1]:
                cache.append(min(height[i], height[j]) * (j - i))
    return(max(cache))










print(maxArea2([1,1]))