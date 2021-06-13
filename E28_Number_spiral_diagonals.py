"""https://projecteuler.net/problem=28
Starting with the number 1 and moving to the right in a clockwise
direction a 5 by 5 spiral is formed as follows:
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
formed in the same way?"""
import time
import decimal


def sum_spiral_diagonals(n):
    """Min n == 3"""
    n = n**2  # 8100**2(4,5 sec)
    start = time.time()
    spiral = list(range(1, n+1))
    # defining the spiral nxn, where last number is n**2
    step = 2  # 2, 4, 6, 8, 10...
    limit_to = 3  # 9, 25, 49, 81, 121...
    # Right-up diagonal number increases according to the rule (limit_to+2)**2
    # After every square of limit_to number step size increase by 2
    diagonals_numbers = spiral[:limit_to**2-1:step]
    # Defining diagonals_numbers with first diagonal numbers
    while (limit_to + 2) ** 2 <= n:
        # Defining that is next limit_to number less than last number of spiral
        step += 2
        diagonals_numbers += spiral[(limit_to ** 2) - 1
                                    :(limit_to + 2) ** 2 - 1
                                    :step]
        # Next diagonal numbers from last limit_to number to next limit_to border
        # with a step increased from the previous sample by 2
        limit_to += 2
    return sum(diagonals_numbers) + n, time.time() - start  # plus last number of the spiral
    # 669171001, 0.062399864196777344s. -- EZ


def sum_spiral_diagonals_ver2(n):
    """Idea from Neitsa(Thu, 25 Aug 2005, 15:31)
    https://projecteuler.net/thread=28#1639
    Min n == 5;
    n == 101101012 -> (688930226604001104723984, 22.74283742904663s.)
    --------------------------------------------------|
    |Square   | 3*3 | 5*5 | 7*7 | 9*9 | 11*11 | 13*13 |
    |---------------------------------|-------|-------|
    |Diag sum |  25 | 101 | 261 | 537 |  961  |  1565 |
    |-----------------------------------------|--------
    |Diff.        |+76 |+160 |+276 | +424 | +604  |
    |--------------------------------------------------
    |Diff of diff    [84]  [116]  [148] [180]
                      |      ^ |    ^
                      +      | |    |
                      3      | |    |
                      2      | |   +32
                      |      | |    |
                      --------  ----"""
    diff_of_diff = 84  # const first diff of diff for both even and odd
    step = 32  # const incrementing diff of diff
    diff_of_numbs = 164 if n % 2 == 0 else 160
    # Incremented diff between 6x6 and 8x8 by diff_of_diff
    # Incremented diff between 3x3 and 5x5 by diff_of_diff
    sum_of_spiral = 112 if n % 2 == 0 else 101
    # sum of spiral 6x6 and 5x5 appropriately
    start = time.time()
    for i in range(6, n, 2):
        # Summation occurs a little less than n//2 times
        # This range(from 6 to n) was discovered by accident
        # and I don't understand why so
        sum_of_spiral += diff_of_numbs
        diff_of_diff += step
        diff_of_numbs += diff_of_diff
    return sum_of_spiral, time.time() - start
    # 101101012 - (688930226604001104723984, 22.74283742904663)


def sum_spiral_diagonals_ver3(n):
    """Lumble USA Python (Wed, 2 Sep 2015, 01:04)"""
    start = time.time()
    decimal.getcontext().prec = 2**len(str(n))
    s = decimal.Decimal(n - 1) / 2  # s = (n - 1) / 2
    return int((16 * s ** 3 + 30 * s ** 2 + 26 * s + 3) / 3), time.time() - start
    # 111111111111111111111111111111 -
    # (914494741655235482395976223140146319158664837677183356195840420667581161408321902149061, 5.194809198379517)
    # (914494741655235482395976223140146319158664837677183356195840420667581161408321902149061, 7.160412549972534)


a = 1111111111111111111111111111111
# print(sum_spiral_diagonals(a))
# print(sum_spiral_diagonals_ver2(a))
# print(sum_spiral_diagonals_ver3(a))
