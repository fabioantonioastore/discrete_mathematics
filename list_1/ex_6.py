factorial_cache = {1: 1}


def factorial(n: int) -> int:
    if n in factorial_cache:
        return factorial_cache[n]
    factorial_cache[n] = n * factorial(n - 1)
    return factorial_cache[n]


def combinations(n: int, k: int) -> int:
    return factorial(n) // (factorial(k) * factorial(n - k))


print(f"Total combinations:\t{combinations(60, 6)}")
print(f"Probability:\t{(1 / combinations(60, 6))}\t(1 in {combinations(60, 6)})")
