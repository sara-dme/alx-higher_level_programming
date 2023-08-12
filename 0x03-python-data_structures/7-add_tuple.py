#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x = list(tuple_a)
    y = list(tuple_b)

    while len(x) < 2:
        x.append(0)

    while len(y) < 2:
        y.append(0)

    z = [x[0] + y[0], x[1] + y[1]]
    return (tuple(z))
