def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def min_to_prime(numbers):
    total = sum(numbers)
    add = 0
    while not is_prime(total + add):
        add += 1
    return add

if __name__ == "__main__":
    assert min_to_prime([3, 1, 2]) == 1
    assert min_to_prime([2, 12, 8, 4, 6]) == 5
    assert min_to_prime([5, 2]) == 0
    assert min_to_prime([1]) == 1
    assert min_to_prime([2]) == 0
    assert min_to_prime([4]) == 1
    assert min_to_prime([10, 10]) == 3
    print("Все проверки пройдены!")
