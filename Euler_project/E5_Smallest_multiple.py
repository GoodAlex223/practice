import time


def smallest_multiple(num_period):
    """Outputs smallest positive number that is evenly divisible by all of the numbers from 1 to 20.

    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    Solution:
    Since 1*2*3*4*5*6*7*8*9*10 = 3 628 800, multiplying all numbers up to 10 is wrong solution
    We need simplify and remove unnecessary numbers. If number divides by 8, number divides by 4 and 2. Using this rule
    we can simplify expression to: 5*7*8*9 = 2520. Used numbers: 1, 2, 2, 2, 3, 3, 5, 7. For period from 1 to 20:
    1, 2, 2, 2, 2, 3, 3, 5, 7, 11, 13, 17, 19 --> 1, 5, 7, 9, 11, 13, 16, 17, 19 or another combination.
    How it works:
    Each subsequent number of the cycle is divided by the numbers in the list, if it can be divided without a remainder,
    and at the end is added to the same list. The added number is multiplied by the result"""
    start_time, result, multipliers = time.time(), 6, [1, 2, 3]  # numbers 1, 2, 3 are used everywhere for dividing
    for number in range(4, num_period+1):
        for multip in multipliers:
            if number % multip == 0:
                number = number / multip
                #  if number divided by multiplier in list without any remainder, operation take place
        multipliers.append(number)  # Adding missing divisor to list of multipliers
        result *= number  # result multiplied by missing diviaor
    print(int(result), "--- %s seconds ---" % (time.time() - start_time), sep="\n")


smallest_multiple(20)  # print(smallestMultiple.__doc__)
