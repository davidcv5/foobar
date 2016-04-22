#!/usr/bin/python


def answer(x):
    distinct = 0
    rabbits = {}
    for r in x:
        if r not in rabbits:
            rabbits[r] = True
            rabbits[r[::-1]] = True
            distinct += 1
    return distinct

print answer(["foo", "bar", "oof", "bar"])
