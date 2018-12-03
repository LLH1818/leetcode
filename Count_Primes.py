def countPrimes1(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 1:
        return 0
    cache = []
    A = list(range(1, n))
    for i in range(2, n):
        for j in range(len(A)):
            if j >= i and A[j] % i == 0:
                cache.append(j)
        for t in cache[::-1]:
            A.pop(t)
        cache = []
        if max(A) <= i:
            return len(A) - 1
    return len(A) - 1


def countPrimes2(n):  # 从平方开始，这样只需要一般的时间
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
    return sum(primes)


print(countPrimes2(4))