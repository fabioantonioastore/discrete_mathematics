def combinations(items: list[int], k: int) -> list[list[int]]:
    combinations_items = []
    if len(items) == k:
        combinations_items.append(items)
        return combinations_items
    for combination in __combinations([], items, k):
        combinations_items.append(combination)
    return combinations_items


def __combinations(combination: list[int], items: list[int], k: int):
    if len(combination) == k:
        yield combination
    temp_items = items.copy()
    for item in temp_items:
        new_combination = combination.copy()
        new_combination.append(item)
        new_items = items.copy()
        if not combination:
            items.remove(item)
        new_items.remove(item)
        yield from __combinations(new_combination, new_items, k)


def power_set(items: list[int]) -> list[list[int]]:
    result = []
    for i in range(len(items) + 1):
        for combination in combinations(items.copy(), i):
            result.append(combination)
    return result


print(power_set([1, 2, 3]))
