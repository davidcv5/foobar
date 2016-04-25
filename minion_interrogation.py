#!/usr/bin/python


def answer(minions):
    d = dict([(i, x[0] / (x[1] / float(x[2])))
              for i, x in enumerate(minions)])
    return [m[0] for m in sorted(d.iteritems(), key=lambda(k, v): (v, k))]
