#!/usr/bin/env python

import matplotlib.pyplot as plot
import multiprocessing as mp
import time

from h3p2_recursive_cehaith2 import recursive_matrix_chain
from h3p2_dp_cehaith2 import matrix_chain_order
from h3p2_memoized_cehaith2 import memoized_matrix_chain

def main():
    phase1()
    print phase2()
    print phase3()

def phase1():
    print 'Phase 1: Checking for correctness'
    print '---------------------------------\n'
    test11()
    test12()
    test13()
    test14()
    test15()


def phase2():
    print 'Phase 2: Chains of square matrices (linear increase)'
    print '----------------------------------------------------\n'
    results = []
    results.append(test21())
    results.append(test22())
    results.append(test23())
    results.append(test24())
    results.append(test25())
    results.append(test26())
    results.append(test27())
    results.append(test28())
    results.append(test29())
    return results
    

def phase3():
    print 'Phase 3: Chains of square matrices (quadratic increase)'
    print '-------------------------------------------------------\n'
    results = []
    print test31()
    print test32()
    print test33()
    print test34()
    print test35()
    print test36()
    print test37()
    print test38()
    print test39()


def test11():
    print 'Test 1.1: d = {1, 1}, i = 1, j = 1'
    d, i, j = [1, 1], 1, 1
    print_results('Test 1.1', test_all(d, i, j), 0)

def test12():
    print 'Test 1.2: d = {1, 1, 1}, i = 1, j = 2'
    d, i, j = [1, 1, 1], 1, 2
    print_results('Test 1.2', test_all(d, i, j), 1)

def test13():
    print 'Test 1.3: d = {1, 2, 1}, i = 1, j = 2'
    d, i, j = [1, 2, 1], 1, 2
    print_results('Test 1.3', test_all(d, i, j), 2)

def test14():
    print 'Test 1.4: d = {2, 2, 2, 2}, i = 1, j = 3'
    d, i, j = [2, 2, 2, 2], 1, 3
    print_results('Test 1.4', test_all(d, i, j), 16)

def test15():
    print 'Test 1.5: d = {2, 2, ... , 2}, |d| = 16, i = 1, j = 15'
    d, i, j = [2] * 16, 1, 15
    print_results('Test 1.5', test_all(d, i, j), 112)

def test21():
    print 'Test 2.1: d = {2, 2, 2}'
    d, i, j = [2, 2, 2], 1, 2
    return test_all(d, i, j)

def test22():
    print 'Test 2.2: d = {2, 2, 2, 2}'
    d, i, j = [2, 2, 2, 2], 1, 3
    return test_all(d, i, j)

def test23():
    print 'Test 2.1: d = {2, 2, 2, 2, 2}'
    d, i, j = [2, 2, 2, 2, 2], 1, 4
    return test_all(d, i, j)

def test24():
    print 'Test 2.1: d = {2, 2, 2, 2, 2, 2}'
    d, i, j = [2, 2, 2, 2, 2, 2], 1, 5
    return test_all(d, i, j)

def test25():
    print 'Test 2.1: d = {2, 2, 2, 2, 2, 2, 2}'
    d, i, j = [2, 2, 2, 2, 2, 2, 2], 1, 6
    return test_all(d, i, j)

def test26():
    print 'Test 2.1: d = {2, 2, 2, 2, 2, 2, 2, 2}'
    d, i, j = [2, 2, 2, 2, 2, 2, 2, 2], 1, 7
    return test_all(d, i, j)

def test27():
    print 'Test 2.1: d = {2, 2, 2, 2, 2, 2, 2, 2, 2}'
    d, i, j = [2, 2, 2, 2, 2, 2, 2, 2, 2], 1, 8
    return test_all(d, i, j)

def test28():
    print 'Test 2.1: d = {2, 2, 2, 2, 2, 2, 2, 2, 2, 2}'
    d, i, j = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 1, 9
    return test_all(d, i, j)

def test29():
    print 'Test 2.1: d = {2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2}'
    d, i, j = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 1, 10
    return test_all(d, i, j)

def test31():
    print 'Test 2.1: d = {2, 2}'
    d, i, j = [2, 2], 1, 1
    return test_all(d, i, j)

def test32():
    print 'Test 2.1: d = {2, 2, 2}'
    d, i, j = [2, 2, 2], 1, 2
    return test_all(d, i, j)

def test33():
    print 'Test 2.1: d = {2, 2, 2, 2, 2}'
    d, i, j = [2, 2, 2, 2, 2], 1, 4
    return test_all(d, i, j)

def test34():
    print 'Test 2.1: d = {2, 2, 2, 2, 2, 2, 2, 2, 2}'
    d, i, j = [2] * 9, 1, 8
    return test_all(d, i, j)

def test34():
    print 'Test 2.1: d = {2, 2, ... , 2}, |d| = 17'
    d, i, j = [2] * 17, 1, 16
    return test_all(d, i, j)

def test35():
    print 'Test 2.1: d = {2, 2, ... , 2}, |d| = 33'
    d, i, j = [2] * 33, 1, 32
    return test_all(d, i, j)

def test36():
    print 'Test 2.1: d = {2, 2, ... , 2}, |d| = 33'
    d, i, j = [2] * 33, 1, 32
    return test_all(d, i, j)

def test37():
    print 'Test 2.1: d = {2, 2, ... , 2}, |d| = 65'
    d, i, j = [2] * 65, 1, 64
    return test_all(d, i, j)

def test38():
    print 'Test 2.1: d = {2, 2, ... , 2}, |d| = 129'
    d, i, j = [2] * 129, 1, 128
    return test_all(d, i, j)

def test39():
    print 'Test 2.1: d = {2, 2, ... , 2}, |d| = 257'
    d, i, j = [2] * 257, 1, 257
    return test_all(d, i, j)





# Test suite functionality 

def print_results(test, results, expected):
    passed = True
    for result in results:
        if result['ops'] != expected:
            passed = False
            print (result['func'] + ': Expected: ' + str(expected) + 
                    ' Found: ' + str(result['ops']))
    print test + (': Passed\n' if passed else ': Failed\n')

def test_all(d, i, j):
    q = mp.Queue()
    p_rec = mp.Process(target=test_rec, args=(d, i, j, q))
    p_dp = mp.Process(target=test_dp, args=(d, q))
    p_mem = mp.Process(target=test_mem, args=(d, q))

    p_rec.start()
    p_dp.start()
    p_mem.start()

    results = [q.get(), q.get(), q.get()]

    p_rec.join()
    p_dp.join()
    p_mem.join()

    return results

def test_rec(d, i, j, q):
    start_t = time.time()
    min_ops = recursive_matrix_chain(d, i, j)
    delta_t = time.time() - start_t
    q.put({'func': 'rec', 'ops': min_ops, 'delta': delta_t})

def test_dp(d, q):
    start_t = time.time()
    min_ops = matrix_chain_order(d)
    delta_t = time.time() - start_t
    q.put({'func': 'dp', 'ops': min_ops, 'delta': delta_t})

def test_mem(d, q):
    start_t = time.time()
    min_ops = memoized_matrix_chain(d)
    delta_t = time.time() - start_t
    q.put({'func': 'mem', 'ops': min_ops, 'delta': delta_t})

if __name__ == "__main__":
    main()
