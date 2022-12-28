list_elem = [22, -6, 32, 82, 9, 25]


def if_divisible_by_index(self):
    result = []

    for x, y in enumerate(self):
        if x != 0:
            if y % x == 0:
                result.append(y)

    return result


print(if_divisible_by_index(list_elem))


def if_divisible_by_index2(self):
    result = []

    for x, y in enumerate(self[1:], start=1):
        if x != 0:
            if y % x == 0:
                result.append(y)

    return result


print(if_divisible_by_index2(list_elem))


def mango_discount(self):
    return f' total: ${(self[0] / 3 * 2) * self[1]:.2f}, {self[0] / 3 * 2:.0f} mangoes * ${self[1]:.2f}, ' \
           f'and {self[0] / 3 * 1:.0f} mangoes for free'


print(mango_discount((45, 3)))


def find_next(self, elem):
    for x, y in enumerate(self):
        if y == elem and x < len(self) - 1:
            return self[x + 1]


arr = [1, 2, 3, 4, 5, 6, 7]
print(find_next(arr, 3))

arr = ['Bob', 'Sally', 'Gyt']
print(find_next(arr, 'Gyt'))


def find_next2(self, num):
    it = iter(self)
    for x in it:
        if x == num:
            break

    return next(it, None)


print(find_next2(arr, 'Bob'))
