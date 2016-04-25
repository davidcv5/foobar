#!/usr/bin/python


def answer(digest):
    message = [0] * 16

    max = 129 * 255 / 256 + 1
    for i, d in enumerate(digest):
        n = 0 if i == 0 else message[i - 1]
        for r in range(0, max):
            m = ((r * 256 + d) ^ n)
            if m % 129 == 0:
                message[i] = m / 129
                break

    return message


print answer([0, 129, 3, 129, 7, 129, 3, 129, 15, 129, 3, 129, 7, 129, 3, 129])
print answer([0, 129, 5, 141, 25, 137, 61, 149, 113, 145, 53, 157, 233, 185,
              109, 165])
