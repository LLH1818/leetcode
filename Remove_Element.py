def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    t = 0
    for num in nums:
        if num != val:
            nums[t] = num
            t += 1
    return t
print(removeElement([0,1,2,2,3,0,4,2], 2))
