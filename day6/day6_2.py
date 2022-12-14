import re

Rooms = {
    1: ['name', 'description', False],
    2: ['name', 'description', True],
    3: ['name', 'description', False],
}


class Ball:
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type


ball1 = Ball()
print(ball1.ball_type)

ball2 = Ball('super')
print(ball2.ball_type)


def is_digit(self):
    try:
        float(self)
        return True
    except TypeError and ValueError:
        return False


print(is_digit('5'))
print(is_digit('50 5'))


def is_digit2(self):
    return bool(re.match('^\-?\d+\.?\d*$', self))


print(is_digit2('45'))
print(is_digit2("45 6"))


def is_different_language(self):

    words_hello = {
        'hello': 'english',
        'ciao': 'italian',
        'salut': 'french',
        'hallo': 'german',
        'hola': 'spanish',
        'ahoj': 'crech republic',
        'czesc': 'polish'
    }

    # for word in str.lower(self).split(' '):
    #     if word in words_hello:
    #         return words_hello.get(str.lower(self))

    str.lower(self)
    return words_hello.get(self) if any([self in words_hello]) else 'foreign language not denied'


print(is_different_language('hogla'))


def remove_all_explanation_points_from_the_end(self):

    count = 0
    for char in self[::-1]:
        if char == '!':
            count -= 1
        else:
            return self[:count] if count < 0 else self


print(remove_all_explanation_points_from_the_end('!Hel! lo'))
print('Hello!!!'.rstrip('!'))
print(re.sub(r'!*$', '', 'Hello!!!'))

list_1 = [4,5,6,9,8,5,6,4,2,0]

for i, v in enumerate(list_1):
    print(i, v)

print()
for i, v in reversed(list(enumerate(list_1))):
    print(i, v)


def move_zeros(self):

    count = 0
    result = []
    for number in self:
        if number != 0:
            result.append(number)
            count += 1

    for i in range(count):
        result.append(0)

    return result


list_2 = [1, 0, 1, 2, 0, 5, 1, 0]
print(move_zeros(list_2))
