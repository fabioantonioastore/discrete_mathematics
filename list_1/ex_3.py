factorial_cache = {1: 1}


def factorial(n: int) -> int:
    if n in factorial_cache:
        return factorial_cache[n]
    factorial_cache[n] = n * factorial(n - 1)
    return factorial_cache[n]


def combinations(n: int, k: int) -> int:
    if k > n:
        raise "n must be greater than k"
    return factorial(n) // (factorial(k) * factorial(n - k))


def exclusive_combinations(n: int, k: int, q: int) -> float:
    if k > n:
        raise "n must be greater than k"
    total_combinations = combinations(n, k)
    total_exclusive_combinatinos = combinations(n - q, k - q)
    return total_combinations - total_exclusive_combinatinos


print(exclusive_combinations(10, 4, 2))
