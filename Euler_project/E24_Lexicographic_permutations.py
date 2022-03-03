"""Problem 24. 24/02/21 -- 93 mins +
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits
1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""
import math


# Works only with c_dig <= 10
def lex_perm(c_dig="10", n_lex_perm="1000000"):  # c_dig -- count of digits, n_lec_perm -- number of lex permutation
    c_dig, n_lex_perm = list(range(int(c_dig)-1, -1, -1)), int(n_lex_perm)
    if n_lex_perm < math.factorial(len(c_dig)):
        lex_perm, result = 0, ""
        for c_of_numb in range(0, len(c_dig)):  # len(c_dig)
            lex_perm += math.factorial(c_dig[c_of_numb])
            i = 0
            while lex_perm < n_lex_perm:
                lex_perm += math.factorial(c_dig[c_of_numb])
                i += 1
                while str(i) in result:
                    i += 1
            while str(i) in result:
                i += 1
            lex_perm -= math.factorial(c_dig[c_of_numb])
            result += str(sorted(c_dig)[i])
        return result
    elif n_lex_perm == math.factorial(len(c_dig)):  # 2783915460, 2783915460
        return "".join([str(i) for i in c_dig])
    else:
        return "Number of lex permutation is more than max lex permutation"


print(lex_perm())
