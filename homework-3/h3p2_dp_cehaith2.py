#!/usr/bin/env python
"""
Charles Haithcock
Due 24 March 2017
CSC 505, Dr. Heber
Homework 3

Dynamic Programming implementation of Matrix Parenthesisation problem as 
described on page 375 of "Introduction to Algorithms", 3rd Ed. 

Algorithm: 
    Given: 
        - List of dimensions, d = {d_1, d_2, ... , d_n}
    Init:
        1. n = d.length - 1
        2. m[n][n]  # Minimum operations possible for subchain between i and j
        3. s[n][n]  # Location of split to minimize operations for subchains
                    # between i and j
    Execution:
        4. Layout the base case by filling in the diagonal of m to 0
        5. 
    Post-exec:
        Print the minimum amount of operations possible
"""

import sys

def matrix_chain_order(d):
    n = len(d)
    min_ops = [[sys.maxint] * n for i in range(n)]
    min_k = [[0] * n for i in range(n)]

    # Set the base case
    for i in range(1, n):
        min_ops[i][i] = 0

    # Compute, bottom up, solutions to subproblems
    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            for k  in range(i, j):
                kth_min = (min_ops[i][k] + min_ops[k + 1][j] + 
                            d[i - 1] * d[k] * d[j])
                if kth_min < min_ops[i][j]:
                    min_ops[i][j] = kth_min
                    min_k[i][j] = kth_min
    return min_ops[1][n - 1]
    
