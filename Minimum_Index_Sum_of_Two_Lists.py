def findRestaurant(list1, list2):
    """
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """
    if not list1 or not list2:
        return None
    cache = {}
    result_num = []
    result_restaurant = []
    result = []
    for i in range(len(list1)):
        cache[list1[i]] = i
    for j in range(len(list2)):
        if list2[j] in cache.keys():
            result_num.append(cache[list2[j]] + j)
            result_restaurant.append(list2[j])
    _min = min(result_num)
    for t in range(len(result_num)):
        if result_num[t] == _min:
            result.append(t)
    return [result_restaurant[t] for t in result]


def findRestaurant2(list1, list2):
    """
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """
    Aindex = {u: i for i, u in enumerate(list1)}
    best, ans = 1e9, []
    for j, v in enumerate(list2):
        i = Aindex.get(v, 1e9)
        if i + j < best:
            best = i + j
            ans = [v]
        elif i + j == best:
            ans.append(v)
    return ans



print(findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Burger King","Tapioca Express","Shogun"]))
