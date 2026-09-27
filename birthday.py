import random
from math import prod


def birthday_probability(people):
    if people > 365:
        return 1.0
    return 1 - prod((365 - i) / 365 for i in range(people))


def simulate_birthday(people, trials):
    return sum(
        len({random.randint(1, 365) for _ in range(people)}) < people
        for _ in range(trials)
    ) / trials
print(birthday_probability(366))
print(simulate_birthday(23, 100000))