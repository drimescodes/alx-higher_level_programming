#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res_tup = (
        tuple_a[0] if len(tuple_a) > 0 else 0,
        tuple_a[1] if len(tuple_a) > 1 else 0,
    )
    res_tup = (
        res_tup[0] + tuple_b[0] if len(tuple_b) > 0 else res_tup[0],
        res_tup[1] + tuple_b[1] if len(tuple_b) > 1 else res_tup[1],
    )
    return res_tup
