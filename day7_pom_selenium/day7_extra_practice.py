list_elem = [22, -6, 32, 82, 9, 25]


def if_divisible_by_index(self):
    result = []

    for x, y in enumerate(self):
        if x != 0:
            if y % x == 0:
                result.append(y)

    return result


print(if_divisible_by_index(list_elem))
