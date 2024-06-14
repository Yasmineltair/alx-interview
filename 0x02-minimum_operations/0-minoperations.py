#!/usr/bin/python3
""" module to find the minimmum number of operation needed"""


def minOperations(n):
    """ min operations func"""

    if n <= 1:
        return 0
    op_count = 0
    div = 2
    
    while n > 1:
        while n % div == 0:
            op_count += div
            n /= div
        div += 1
    return op_count
