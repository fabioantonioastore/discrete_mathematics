items = ["A", "B", "C"]


def permutations(items: list[str]) -> list[list[str]] | list:
    if len(items) == 0:
        return []
    permutations_result = []
    for permutation in __permutations([], items):
        permutations_result.append(permutation)
    return permutations_result


def __permutations(permutation: list[str], items: list[str]):
    if not items:
        yield permutation
    for item in items:
        new_permutation = permutation.copy()
        new_permutation.append(item)
        rest_items = items.copy()
        rest_items.remove(item)
        yield from __permutations(new_permutation, rest_items)


print(permutations(items))
