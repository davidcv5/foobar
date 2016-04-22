#!/usr/bin/python


def answer(heights):
    total = 0

    for i in range(len(heights)):
        for x in range(1, heights[i]):
            current = 0
            higher = False
            j = i
            for k in range(j + 1, len(heights)):
                y = heights[k]
                if x > y:
                    current += x - y
                else:
                    higher = True
                    j = k
                    break
            if higher:
                total += current

    return total


print answer([1, 4, 2, 5, 1, 2, 3])
print answer([1, 2, 3, 2, 1])
