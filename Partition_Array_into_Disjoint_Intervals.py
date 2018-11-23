def partitionDisjoint1(A):        #  一个一个比  太慢
    """
    :type A: List[int]
    :rtype: int
    """
    for i in range(A.__len__()):
        black_flag = 0
        left = A[: i + 1]
        right = A[i + 1:]
        for rnum in right:
            for lnum in left:
                if lnum > rnum:
                    black_flag = 1
                    break
            if black_flag == 1:
                break
        if black_flag == 0:
            return i + 1


def partitionDisjoint2(A):     # 左边最大的和右边最小的比
    for i in range(A.__len__()):
        black_flag = 0
        left = A[: i + 1]
        right = A[i + 1:]
        lmax = 0
        rmin = right[0]
        for lnum in left:
            if lnum > lmax:
                lmax = lnum
        for rnum in right:
            if rnum < rmin:
                rmin = rnum
        if lmax > rmin:
            black_flag = 1
        if black_flag == 0:
            return i + 1


def partitionDisjoint3(A):     # 重新审视规则，不用蛮力
    lmax = A[0]
    local_max = lmax
    result = 0
    for i in range(len(A) - 1):
        if lmax > A[i]:
            result = i
            lmax = local_max
        else:
            local_max = max(A[i], local_max)
    return result + 1





print(partitionDisjoint3([24,11,49,80,63,8,61,22,73,85]))

