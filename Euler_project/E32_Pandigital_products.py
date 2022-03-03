"""
Pandigital products / Problem 32 / 11 Oct 21 / 13:00 - 16:42
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

ANSWER: 45228
"""
res = set()
for i in range(2, 9 + 1):
    for j in range(1000, 9999 + 1):
        i_j_str = str(i) + str(j)
        product_str = str(i * j)
        number_str = i_j_str + product_str
        if '0' in number_str:
            continue
        if len(product_str) < 5 and len(set(number_str)) == 9:
            res.add(int(product_str))


for i in range(10, 99+1):
    for j in range(100, 999+1):
        i_j_str = str(i) + str(j)
        product_str = str(i * j)
        number_str = i_j_str + product_str
        if '0' in number_str:
            continue
        if len(product_str) < 5 and len(set(number_str)) == 9:
            res.add(int(product_str))
print(sum(res))
