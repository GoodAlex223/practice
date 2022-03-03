"""Problem 23. 23/02/21 -- 65 mins
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant
if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two
abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as
the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is
known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""
# ???????????
# def PE023(limit = 28123):
#     somDiv = [1] * (limit+1) # jusk 28123 inclus
#     for i in range(2, int(limit**.5)+1):
#         somDiv[i*i] += i
#     for k in range(i+1, limit//i+1):
#         somDiv[k*i] += k+i
#     abondant, res = set(), 0
#     ajout = abondant.add
#     for n in range(1, limit+1):
#         if somDiv[n] > n:
#             ajout(n)
#         if not any((n-a in abondant) for a in abondant):
#             res += n
#     return res
#
# print(PE023())

result, abun_numbs = set(range(1, 28124)), []
for numb in range(12, 28124):
    if sum([d for d in range(1, numb//2 + 1) if numb % d == 0]) > numb:
        abun_numbs.append(numb)
        for i in abun_numbs:
            result.difference_update({numb + i})
print(sum(result))  # 4179871