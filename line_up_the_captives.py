#!/usr/bin/python


def fact(n): return reduce(lambda x, y: x * y, range(1, n + 1), 1)


def permutations(n):
    return fact(n)


def combinations(k, n):
    return fact(n) / fact(n - k) / fact(k)


def answer(x, y, n):
    if x + y > n + 1:
        return 0

    if x == y == 1:
        return n == 1

    d = {}

    if x == 1:
        return solve(y - 1, n - 1, d)
    if y == 1:
        return solve(x - 1, n - 1, d)

    total = 0
    for i in range(x - 1, (n - y + 1)):
        c = combinations(i, n - 1)
        left = solve(x - 1, i, d)
        right = solve(y - 1, n - i - 1, d)
        total += c * left * right

    return total


def solve(x, n, d):

    if (x, n) in d:
        return d[(x, n)]

    if x == 1:
        result = permutations(n - 1)
        d[(x, n)] = result
        return result

    if x == n:
        result = 1
        d[(x, n)] = result
        return result

    total = 0
    for i in range(x - 1, n):
        c = combinations(i, n - 1)
        left = solve(x - 1, i, d)
        right = permutations(n - i - 1)
        total += c * left * right

    d[(x, n)] = total
    return total

print answer(2, 3, 5)
print answer(1, 2, 6)
print answer(2, 2, 3)
