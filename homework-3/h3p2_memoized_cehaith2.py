"""
Charles Haithcock                                                                                    
Due 24 March 2017                                                                                    
CSC 505, Dr. Heber                                                                                   
Homework 3                          

Memoization implementation of the Memoization Parenthesization probelm described
in page 388 of "Introduction to Algorithms" 3rd ed. 

Algorithm:
    Given:
        - List of dimensions, d = {d_1, d_2, ... , d_n}
    Init: 
        1. n = d.length - 1
        2. m[n][n]  # Minimum operations possible for subchain between i and j
    Execution:
        3. If the chain length is 0, return 0
        4. If the current subproblem has already been computed, return the 
           precomputed result. 
        5. Otherwise, recurse and compute the solution manually. Return the
           computed solution.
    Post-Execution:
        6. Return the solution at m[1, n]
"""
import sys

rec_calls = 0

def lookup_chain(min_ops, d, i, j):
    global rec_calls

    # If we found a solution, return it
    if min_ops[i][j] < sys.maxint:
        return min_ops[i][j]

    # If the chain length is one matrix long, return 0 since no multiplication
    # can occur on 1 matrix
    if i == j:
        min_ops[i][j] = 0

    # Otherwise, recurse to compute the solution. Attempt all possible splits
    # for the current chain to find the k which produces the minimum amount of
    # multiplications
    else:
        for k in range(i, j):
            kth_min = (lookup_chain(min_ops, d, i, k) +
                            lookup_chain(min_ops, d, k + 1, j) +
                            d[i - 1] * d[k] * d[j])
            rec_calls += 2
            if kth_min < min_ops[i][j]:
                min_ops[i][j] = kth_min
    return min_ops[i][j]

def memoized_matrix_chain(d):
    # Start of the algorithm
    n = len(d)
    min_ops = [[sys.maxint] * n for i in range(n)]
    return lookup_chain(min_ops, d, 1, n - 1)
