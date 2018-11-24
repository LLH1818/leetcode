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


def maxArea2(height):
    """
    :type height: List[int]
    :rtype: int
    """
    i, j = 0, len(height) - 1
    cache = []
    for i in range()








print(maxArea1([1,8,6,2,5,4,8,3,7]))