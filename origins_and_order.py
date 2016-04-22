#!/usr/bin/python


def answer(x, y, z):
    date = sorted([x, y, z])

    mm = date[0]
    dd = date[1]
    yy = date[2]

    month_max = 30 if mm in [2, 4, 6, 9, 11] else 31

    if ((mm == dd == yy) or
            (yy > month_max and mm == dd) or
            (dd > 12 and yy == dd) or
            (dd > 12 and yy > month_max)):
        return '%02d/%02d/%02d' % (mm, dd, yy)
    else:
        return 'Ambiguous'

print answer(1, 32, 1)
