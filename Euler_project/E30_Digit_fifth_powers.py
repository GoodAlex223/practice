"""
Digit fifth powers|Problem 30|https://projecteuler.net/problem=30
01.07.21/13:15-08.07.21/01:03(on average 2 hours a day; only 16h)

Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth
powers of their digits.
Post on Project Euler -- https://projecteuler.net/action=quote;post_id=385244
(available for users that solved this problem)
"""
# Solution of the problem:
# [4150, 4151, 54748, 92727, 93084, 194979]
# 443839
import time
from itertools import combinations_with_replacement


def digit_nth_powers(power=5):
    """My solution"""
    def create_powers_dict(dnp_power):
        new_dict = {}
        for n in range(0, 10):  # Powers of numbers from 0 to 9
            new_dict[str(n)] = n**dnp_power
        return new_dict

    # result = []
    result = 0
    powers_dict = create_powers_dict(power)
    for i in range(max(10, power * 3**power), power * 9**power):
        # Max number for this numbers is power * 9**power
        # Min number for this numbers is power * 3**power
        # Formulas obtained empirically
        if sum(powers_dict[numb] for numb in str(i)) == i:
            # result += [i]
            result += i
    # return sorted(result), sum(result)
    return result


def digit_nth_powers_ver2(power: int = 5) -> int:
    """Sum of powers of 120 is equal to sum of powers of 210 and is, for example, 2**10 + 1**10 + 0**10 = 1025.
    And if sum of powers of 1025 is equal to 1025 this number adds to result.
    This facts allow us to reduce the amount of iterable numbers from
    power * 9**power[Link1]* to
    math.factorial(10 + 4 - 1)/(math.factorial(4) * math.factorial(10 - 1))[Link2],
    where 10 is len('0123456789')
    For example (power = 4):
    4 * 9**4 == 26244
    Formula of combination_with_replacement == 715
    (except for 5 and 7 powers(for the 5th and 7th power + 1),
    because their sum of powers are very close to the border,
    and are not processed by this algorithm)
    For creating combinations of unique numbers uses itertools module
    *Links 1, 3, 4 are available for users that solved this problem
    [Link1: https://projecteuler.net/action=redirect;post_id=475]
    [Link2: https://www.tutorialspoint.com/statistics/combination_with_replacement.htm]
    Thanks to
    [Link3: https://projecteuler.net/action=redirect;post_id=3010]
    [Link4: https://projecteuler.net/action=redirect;post_id=6010]
    for this idea"""
    # result = []  # If u need a list of numbers uncomment such lines and comment others
    result = 0
    pows_dict = {str(j): j**power for j in range(10)}
    if power == 5 or power == 7:  # Numbers that equal to their sum of pows for 5 and 7 are very
        power += 1                # are very close to the border, and are not processed by this algorithm
    # Next expression need to generates numbers with unique signs
    # To reduce the number of unnecessary iterations
    for j in combinations_with_replacement('0123456789', power):
        number = sum(pows_dict[x] for x in j)
        if sum(pows_dict[n] for n in str(number)) == number:
            # result.append(number)
            result += number
    # result.sort()
    # return result[2:], sum(result) - 1  # List includes 0 and 1
    return result - 1


if __name__ == '__main__':
    for i in range(1, 16):
        # Similar solution from xXBlade_Master420Xx(page=8) to check correctness
        # def digit_list(x):
        #     return list(map(int, str(x)))
        #
        # def fxo(ls):
        #     dls = sorted(digit_list(sum(map(lambda x: pow(x, i), ls))))
        #     n = len(ls) - len(dls)
        #     return list(ls) == [0] * n + dls
        #
        #
        # start = time.time()
        #
        # ls9 = list(map(lambda x: pow(x, i, 9), range(10)))
        # lsX = list(map(lambda x: pow(x, i, 10), range(10)))
        #
        # fxn = lambda ls: sum(map(lambda x: ls9[x], ls)) % 9 == sum(ls) % 9
        # fxm = lambda ls: sum(map(lambda x: lsX[x], ls)) % 10 in ls
        #
        # c = combinations_with_replacement(range(10), i+1)
        # f = filter(fxm, c)
        # f2 = filter(fxn, f)
        # f3 = filter(fxo, f2)
        #
        # s = 0
        # for num in f3:
        #     n2 = sum(map(lambda x: pow(x, i), num))
        #     s += n2
        # print('--', s - 1)
        #
        # print(time.time() - start)

        start = time.time()
        print(digit_nth_powers_ver2(i))
        print(time.time() - start)
        print()

# digit_nth_powers() and digit_nth_powers_ver2() time tests:
# 2 -- dnp: 0.004999876022338867s, 0
# 2 -- dnp_ver2: 0.0s, 0
#
# 3 -- dnp: 0.004999876022338867s, 1301
# 3 -- dnp_ver2: 0.004999876022338867s, 1301
#
# 4 -- dnp: 0.10000038146972656s, 19316
# 4 -- dnp_ver2: 0.004999876022338867s, 19316
#
# 5 -- dnp: 1.1950016021728516s, 443839
# 5 -- dnp_ver2: 0.03500032424926758s, 443839
#
# 6 -- dnp: 14.445020198822021s, 548834
# 6 -- dnp_ver2: 0.034999847412109375s, 548834
#
# 7 -- dnp: >137s.s, ?
# 7 -- dnp_ver2: 0.17500019073486328s, 40139604
#
# 8 -- dnp: >137s.s, ?
# 8 -- dnp_ver2: 0.18000030517578125s, 137949578
#
# 9 -- dnp: >137s.s, ?
# 9 -- dnp_ver2: 0.390000581741333s, 2066327172
#
# 10 -- dnp: >137s.s, ?
# 10 -- dnp_ver2: 0.8250012397766113s, 4679307774
#
# 11 -- dnp: >137s.s, ?
# 11 -- dnp_ver2: 1.5300023555755615s, 418030478906
#
# 12 -- dnp: >137s.s, ?
# 12 -- dnp_ver2: 3.750005006790161s, 0
#
# 13 -- dnp: >137s.s, ?
# 13 -- dnp_ver2: 6.620009183883667s, 564240140138
#
# 14 -- dnp: >137s.s, ?
# 14 -- dnp_ver2: 12.825017929077148s, 28116440335967
#
# 15 -- dnp: >137s.s, ?
# 15 -- dnp_ver2: 19.3000271320343s, 0
#
# 16 -- dnp: >137s.s, ?
# 16 -- dnp_ver2: 34.62504816055298s, 8676563538782741
#
# 17 -- dnp: >137s.s, ?
# 17 -- dnp_ver2: 48.05506753921509s, 93647847008958559
#
# 18 -- dnp: >137s.s, ?
# 18 -- dnp_ver2: 77.40010833740234s, 0
