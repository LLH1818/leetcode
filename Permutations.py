def permute1(nums):           # 插入法
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    perms = [[]]
    for n in nums:
        new_perms = []
        for perm in perms:
            for i in range(len(perm) + 1):
                new_perms.append(perm[:i] + [n] + perm[i:])  ###insert n
        perms = new_perms
    return perms


permute1([1, 2, 3])
