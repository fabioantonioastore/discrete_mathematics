factorial_cache = {1: 1}


def factorial(n) -> int:
    if n in factorial_cache:
        return factorial_cache[n]
    factorial_cache[n] = n * factorial(n - 1)
    return factorial_cache[n]


def combination(n: int, k: int) -> float:
    if not (n > k):
        raise "n not is greater than k"
    return factorial(n) // (factorial(k) * factorial(n - k))


print(combination(5, 2))
