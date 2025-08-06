factorial_cache = {1: 1}


def factorial(n: int) -> int:
    if n in factorial_cache:
        return factorial_cache[n]
    factorial_cache[n] = n * factorial(n - 1)
    return factorial_cache[n]


def permutations(string: str) -> int:
    if not string:
        return 0
    n = len(string)
    dividend = 1
    chars = set(string)
    for char in chars:
        char_count = string.count(char)
        if char_count > 1:
            dividend *= factorial(char_count)
    return factorial(n) // dividend


print(permutations("AAB"))
