from itertools import product


def are_equivalent(f, g, n):
    for row in product([False, True], repeat=n):
        if f(*row) != g(*row):
            return False
    return True


def de_morgan_left(a, b):
    return not (a and b)


def de_morgan_right(a, b):
    return (not a) or (not b)


def wrong(a, b):
    return (not a) and (not b)


def implies(a, b):
    return (not a) or b
print(are_equivalent(de_morgan_left, wrong, 2))