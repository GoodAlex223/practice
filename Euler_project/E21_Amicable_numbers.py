"""Problem 21. 19/02/21 -- 1 h 46 m 47 s
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

numb_divs_sum_dict = {}
amic_numbs = set()
for i in range(2, 10000):
    if i in numb_divs_sum_dict:
        divs_sum1 = numb_divs_sum_dict[i]
    else:
        divs_sum1 = sum([j for j in range(1, i // 2 + 1) if i % j == 0])
        numb_divs_sum_dict[i] = divs_sum1

    if divs_sum1 in numb_divs_sum_dict:
        divs_sum2 = numb_divs_sum_dict[divs_sum1]
    else:
        divs_sum2 = sum([k for k in range(1, divs_sum1 // 2 + 1) if divs_sum1 % k == 0])
        numb_divs_sum_dict[divs_sum1] = divs_sum2

    if divs_sum2 == i and i != divs_sum1:
        amic_numbs.update({divs_sum2, i})

print(sum(list(amic_numbs)))  # 31626
