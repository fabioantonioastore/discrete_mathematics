def permutations(string: str) -> list[str]:
    result = []
    items = list(string)
    for permutation in __permutations("", items):
        result.append(permutation)
    return result


def __permutations(permutation: str, items: list[str]):
    if not items:
        yield permutation
    for item in items:
        new_permutation = permutation
        new_permutation += item
        new_items = items.copy()
        new_items.remove(item)
        yield from __permutations(new_permutation, new_items)


def anagrams(string: str) -> list[str]:
    permutations_list = permutations(string)
    result = set()
    vogal = True
    for permutation in permutations_list:
        valid = True
        for letter in permutation:
            vogal = not vogal
            if vogal and letter in ["a", "e", "i", "o", "u"]:
                continue
            if not vogal and not letter in ["a", "e", "i", "o", "u"]:
                continue
            valid = False
            break
        if valid:
            result.add(permutation)
    vogal = False
    for permutation in permutations_list:
        valid = True
        for letter in permutation:
            vogal = not vogal
            if vogal and letter in ["a", "e", "i", "o", "u"]:
                continue
            if not vogal and not letter in ["a", "e", "i", "o", "u"]:
                continue
            valid = False
            break
        if valid:
            result.add(permutation)
    return list(result)


print(anagrams("amor"))
