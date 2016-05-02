#!/usr/bin/python


def fact(n): return reduce(lambda x, y: x * y, range(1, n + 1), 1)


def answer(seq):
    if len(seq) <= 1:
        return 1

    r = seq[0]
    g = []
    l = []
    for x in seq[1:]:
        if x > r:
            g.append(x)
        else:
            l.append(x)

    sg = answer(g)
    sl = answer(l)

    print seq, g, l, sg, sl

    return fact(len(seq) - 1) / fact(len(l)) / fact(len(g)) * sg * sl


print sequences([5, 9, 8, 2, 1])
print sequences([5, 8, 9, 2, 1, 7])
print sequences([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
