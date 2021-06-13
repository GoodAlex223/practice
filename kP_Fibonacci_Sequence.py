"""(https://github.com/karan/Projects) - Fibonacci Sequence
Fibonacci Sequence - Enter a number and have the program generate
the Fibonacci sequence to that number or to the Nth number.

This program is collection of various methods for solving this problem
that I wrote or found on the internet. And all methods with time tests.
My programs - fib_seq; fib_seq_ver2
Most effective (found by me on the Internet at the bottom) -
fib_method1, fib_method2
"""
import time
import timeit
import math


# number to generate the Fibonacci sequence to that number or to the Nth number(is_index?)
def fib_seq(number, is_index=False):
    """
    Generates the Fibonacci sequence to number or to the Nth number.
    First elem of Fib seq is 0
    """
    fib_list = [0, 1]  # first and second Fib's number
    i = 1  # defining an index to access the last two elements
    start = time.time()

    if is_index:  # number is the index of the number in Fib's sequence?
        while len(fib_list) < number:  # numbers are determined before the given index
            fib_list.append(fib_list[-1] + fib_list[-2])
            # Sum of last two numbers defining next number of sequence
    else:
        while fib_list[-1] < number:
            fib_list.append(fib_list[-1] + fib_list[-2])

    return fib_list, time.time() - start


# print(*fib_seq(10**1000, 0), sep="\n")
# most of the time is spent on displaying a list of numbers in the "to n" mode
# print(timeit.timeit('fib_seq(10**1000, 0)', 'from __main__ import fib_seq', number=10)/10)
# time spent - fib_seq()
# (1000, 1) - 0.0010638262700000001(100)
# (10000, 1) - 0.02263508004(100execs), 0.02174080869
# (70000, 1) - 0.32144645091(100execs), same
# (100000, 1) - 0.60441114071(100execs), 0.5956531040299999
# (200000, 1) - 12.0747116973(10)
#
# fib_seq(10**10000, 0) - 0.15258278752999999(100execs)


def fib_seq_ver2(number, is_index=False, returned_seq=False):
    """
    Generates the Fibonacci sequence to number or to the Nth number
    or just returns a number.
    """
    start = time.time()
    if returned_seq:
        fib_list = [0, 1]  # first and second Fib's number
        i = 1  # defining an index to access the last two elements

        if is_index:  # number is the index of the number in Fib's sequence?
            while len(fib_list) < number:  # numbers are determined before the given index
                fib_list.append(fib_list[-1] + fib_list[-2])
                # Sum of last two numbers defining next number of sequence
        else:
            while fib_list[-1] < number:
                fib_list.append(fib_list[-1] + fib_list[-2])

        return fib_list, time.time() - start
    else:
        first = 0
        second = 1

        if is_index:
            i = 1
            while i <= number:
                first, second = first + second, first
                i += 1
        else:
            while first < number:
                first, second = first + second, first

        return first, time.time() - start


# print(fib_seq_ver2(10**100, 0, 0), sep='\n')
# print(timeit.timeit('fib_seq_ver2(10**100, 0, 0)', 'from __main__ import fib_seq_ver2', number=10)/10)
# time spent - fib_seq_ver2(n, 1, 0)
# (1000, 1, 0) - 0.0003914252999999999(10execs)
# (10000, 1, 0) - 0.011151371799999999(10execs)
# (100000, 1, 0) - 0.40016386839999996(10execs)
# (1000000, 1, 0) - 35.77785849571228(1exec)
#
# time spent - fib_seq_ver2(n, 0, 0)
# (10**10000, 0, 0) - 0.1368276139
# (10**100000, 0, 0) - 7.3748877183


# Interesting implementations:
# 1. https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
"""This another O(n) which relies on the fact that if we n times 
multiply the matrix M = {{1,1},{1,0}} to itself (in other words 
calculate power(M, n)), then we get the (n+1)th Fibonacci number as 
the element at row and column (0, 0) in the resultant matrix.
The matrix representation gives the following closed expression for the
Fibonacci numbers. We can do recursive multiplication to get power(M, n)"""
# Helper function that multiplies
# 2 matrices F and M of size 2*2,
# and puts the multiplication
# result back to F[][]

# Helper function that calculates
# F[][] raise to the power n and
# puts the result in F[][]
# Note that this function is
# designed only for fib() and
# won't work as general
# power function

# function that returns nth
# Fibonacci number
def fib_method1(n):
    F = [[1, 1],
         [1, 0]]
    if n == 0:
        return 0
    power(F, n - 1)  # (n-1) power of matrix gives nth number of Fib

    return F[0][0]


def multiply(F, M):
    """
    Common multiplication of 2x2 and 2x2 matrices
    """
    x = (F[0][0] * M[0][0] +
         F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
         F[1][1] * M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w


# Optimized version of
# power()
def power(F, n):
    if n == 0 or n == 1:
        return

    power(F, n // 2)
    multiply(F, F)

    if n % 2 != 0:
        M = [[1, 1],
             [1, 0]]
        multiply(F, M)
#
#
# n = 1000
# print(fib_method1(n))
# print(*fib_seq_ver2(n, True, False), sep='\n')
# print(timeit.timeit('fib_method1(1000000)', 'from __main__ import fib_method1', number=10)/10)
# time spent - fib_method1 VS fib_seq_ver2
# 10 - 3.2499900000000634e-05(10execs)
# 100 - 7.241220000000076e-05(10execs)
# 1000 - 0.00031217090000000005(10execs) VS 0.0003914252999999999(10execs)
# 10000 - 0.0014682579999999988(10execs) VS 0.011151371799999999(10execs)
# 100000 - 0.031086120900000003(10execs) VS 0.40016386839999996(10execs)
# 1000000 - 0.8144964185000001(10execs) VS 35.77785849571228(1exec)
# 10000000 - 27.1296037796(10execs)

# 2. https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
"""
Below is one more interesting recurrence formula that can be used to find n’th Fibonacci Number in O(Log n) time.  

If n is even then k = n/2:
F(n) = [2*F(k-1) + F(k)]*F(k)

If n is odd then k = (n + 1)/2
F(n) = F(k)*F(k) + F(k-1)*F(k-1)
How does this formula work? 
The formula can be derived from above matrix equation. 
 [[1, 1] ** 2   [[F(index: n+1), F(index: n)]
 [1, 0]]      = [F(index: n)]], F(index: n-1)

https://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form

To get the formula to be proved, we simply need to do the following 
If n is even, we can put k = n/2 
If n is odd, we can put k = (n+1)/2 
"""


# Python3 Program to find n'th fibonacci Number in
# with O(Log n) arithmetic operations


def fib_method2(n):
    MAX = n + 1
    # Create an array for memoization
    f = [0] * MAX

    # Returns n'th fuibonacci number using table f[]
    def fibs(n):
        # Base cases
        if n == 0:
            return 0
        if n == 1 or n == 2:
            f[n] = 1
            return f[n]

        # If fib(n) is already computed
        if f[n]:
            return f[n]

        if n & 1:  # value n&1 is 1 if n is odd, else 0.
            k = (n + 1) // 2
        else:
            k = n // 2

        # Applying above formula [Note value n&1 is 1
        # if n is odd, else 0.]
        fib1 = fibs(k)
        fib2 = fibs(k - 1)
        if n & 1:
            f[n] = (fib1 * fib1 + fib2 * fib2)
        else:
            f[n] = (2 * fib2 + fib1) * fib1

        return f[n]

    return fibs(n)


# n = 1000
# print(fib_method2(n))
# print(fib(n))
# print(timeit.timeit('fib_method2(10)', 'from __main__ import fib_method2', number=1))
# print(timeit.timeit('fib(10000000)', 'from __main__ import fib', number=10)/10)
# time spent - fib_method2 VS fib
# 10 - 1.607889999999945e-05(10) VS 3.2499900000000634e-05(10execs)
# 100 - 5.5136000000000077e-05(10) VS 7.241220000000076e-05(10execs)
# 1000 - 0.00011278069999999945(10) VS 0.00011306569999999932(10execs)
# 10000 - 0.00037662919999999987(100) VS 0.0007424079799999999(100execs)
# 100000 - 0.00873965631(100) VS 0.022700651769999997(100execs)
# 1000000 - 0.15287558721(100) VS 0.64519281328(100execs)
# 10000000 - 5.259207103(10) VS 23.530176919699997(10execs)
# 10**8 - 190.06702181(1exec)
