"""
https://github.com/karan/Projects - Find e to the Nth Digit
ver1: 31.05.21/16.25 - 31.05.21/19.00
ver2: 01.60.21/12.00 - 01.06.21/14.52
ver3, ver3_decimal and decorating: 01.06.21/14.52 - 01.06.21/17.46
Find e to the Nth Digit -
Just like the previous problem, but with e instead of PI.
Enter a number and have the program generate e up to that many decimal
places. Keep a limit to how far the program will go.
"""
from math import *
from decimal import *
import timeit
import time


def report(fn):
    def wrapper(arg):
        with open("Euler_number(2mill_dig).txt") as true_e:
            true_e = true_e.read().replace("\n", "")
            print(f"Running function: {str(fn.__name__)}(), "
                  f"with param: {str(arg)}")
            print(f"Euler's number exactly up to {arg} is:")
            print(true_e[:arg+2], "(https://apod.nasa.gov/htmltest/gifcity/e.2mil)", sep="\n")
            start = time.time()
            e = fn(arg)
            print("Result of program:", e, sep="\n")
            print(f"Result is equal to const of Number of Euler -- {e in true_e}")
            print(f"Number of decimal places printed: {len(e[2:])}")
            print(f"Program execution time -- {time.time() - start}s.")
            print()
    return wrapper


@report
def e_up_to(n=1000):
    getcontext().prec = n + 10
    e = 0
    for n in range(n + 10):
        e += Decimal('1')/Decimal(factorial(n))
    return str(e)[:-9]


@report
def e_up_to_ver2(count=1000):
    count += 5
    e = 0
    numerator = 10**count
    fact_n = 1
    for n in range(1, count+1):
        e += numerator//fact_n
        fact_n *= n
    e = "2." + str(e)[1:-5]
    return e
# the complexity of the algorithm - O(n**2)


@report
def e_up_to_ver3(count=1000):
    count += 5
    e = 10**count
    numerator = e
    for n in range(2, count+1):
        e = e * n + numerator
    e //= factorial(count)
    e = "2." + str(e)[1:-5]
    return e


@report
def e_up_to_ver3_decimal(count=1000):
    count += 5
    e = 1
    numerator = 1
    for n in range(1, count+1):
        e = e * n + numerator
    getcontext().prec = count
    e /= Decimal(factorial(count))
    e = str(e)[:-4]
    return e


def main():
    number = input("Input number of decimal spaces(up to 100000, > 100000 - very slow):\n")
    while number != "q":
        # e_up_to(1000) # 4th place
        # e_up_to_ver2(1000) # 3rd place
        e_up_to_ver3(int(number))  # fastest - 1st place
        # e_up_to_ver3_decimal(1000)  # 2nd place
        number = input("To quit print: q\nYour number: ")
    print("Finishing the program...")


main()
