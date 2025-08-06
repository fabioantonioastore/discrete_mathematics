items = ["A", "B", "C", "D"]
k = 2


def combinations(items: list[str], k: int) -> list[list[str]]:
    combinations_items = []
    if len(items) == k:
        combinations_items.append(items)
        return combinations_items
    for combination in __combinations([], items, k):
        combinations_items.append(combination)
    return combinations_items


def __combinations(combination: list[str], items: list[str], k: int):
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


print(combinations(items, k))
