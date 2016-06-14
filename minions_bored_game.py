#!/usr/bin/python


def answer(t, n):
    if t < n - 1:
        return 0
    d = {}
    return solve(t, n, 1, d) % 123454321


def solve(t, n, i, d):
    if (t, n, i) in d:
        return d[(t, n, i)]

    if i == n or i + t == n:
        result = 1
        d[(t, n, i)] = result
        return result

    right = solve(t - 1, n, i + 1, d)
    stay = solve(t - 1, n, i, d)
    left = solve(t - 1, n, i - 1, d) if i > 1 and i + t > n + 1 else 0

    result = right + stay + left
    d[(t, n, i)] = result
    return result


print answer(1, 2)
print answer(3, 2)
print answer(10, 4)
print answer(20, 7)
