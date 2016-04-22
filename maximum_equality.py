#!/usr/bin/python


def answer(x):
    return len(x) - 1 if sum(x) % len(x) > 0 else len(x)


arr = [1000000]*100
print answer(arr)
