def removeDuplicates(nums):    # too slow
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    t = 1
    a = nums[0]
    for num in nums[1:]:
        if num == a:
            nums.pop(t)
        else:
            a = num
            t += 1
    return nums


def removeDuplicates1(nums):
    if not nums:
        return 0
    t = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[t]:
            t += 1
            nums[t] = nums[i]
    return t + 1


print(removeDuplicates([0, 0, 1, 1, 2, 2, 3, 3, 4]))
