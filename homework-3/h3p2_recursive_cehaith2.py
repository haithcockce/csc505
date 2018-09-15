"""
Charles Haithcock
Due 24 March 2017
CSC 505, Dr. Heber
Homework 3

Recursive implementation of Matrix Parenthesisation problem as described on page
385 of "Introduction to Algorithms", 3rd Ed. 

Algorithm: 
    Given: 
        - List of dimensions, d = {d_1, d_2, ... , d_n}
        - Indeces i and j of the start and end of the matrix chain to compute
    Init:
        1. min_ops = MAX_INT
    Execution:
        2. When the chain length is 0, report 0 possible operations
        3. Otherwise, walk all possible splits between i and j. 
            3.a Split the chain at k-th index creating a left and right subchain
            3.b Recurse on the left and right subchains and sum the results with
                the product of the left dimension of the left subchain, inner
                dimension of the subchains, and the right dimension of the right
                subchain indicating the amount of operations required for 
                splitting at k
            3.c Store this sum if it is the lowest amount of operations we have
                seen so far. 
        4. Return the minimum amount of operations for a split at the current
           recursion level. 
    Post-exec:
        Print the minimum amount of operations possible
"""

import sys
rec_calls = 0

def recursive_matrix_chain(d, i, j):
    global rec_calls

    # Base case, return 0 ops when the chain length is only 1 matrix long
    if i == j:
        return 0

    # Parse through each k and grab the k producing the minimum amount of ops
    min_ops = sys.maxint
    for k in range(i, j):
        kth_ops = (recursive_matrix_chain(d, i, k) + 
                    recursive_matrix_chain(d, k + 1, j) +
                    d[i - 1] * d[k] * d[j])
        rec_calls += 2
        if kth_ops < min_ops:
            min_ops = kth_ops
    return min_ops
