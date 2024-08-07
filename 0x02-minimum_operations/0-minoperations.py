#!/usr/bin/python3

"""
Module for calculating the minimum
number of operations
"""

def minOperations(n):
    if n < 2:
        return 0

    operand_1 = 0
    init_length = 1
    operand_2 = 2

    while n > 1:
        while n % operand_2 == 0:
            operand_1 += operand_2
            n //= operand_2
        operand_2 += 1

    return operand_1

