"""Digit cancelling fractions 03.03.22 16.35 - 17.32
Problem 33
(https://projecteuler.net/problem=33)

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator."""

# 10/11 -> 98/99
nominator = 1
denominator = 1
for i in range(10, 98+1):
    for j in range(i+1, 99+1):
        if i / j == int(i/10)/int(j/10):
            continue
        str_i, str_j = str(i), str(j)
        for str_i_d in str_i:
            if str_i_d in str_j:
                str_j = str_j.replace(str_i_d, '', 1)
                str_i = str_i[str_i.index(str_i_d)-1]
                if int(str_j) and i / j == int(str_i) / int(str_j):
                    print(f'{i}/{j} = {str_i}/{str_j}')
                    nominator *= i
                    denominator *= j
                break

print(f'{nominator}/{denominator}')
print(f'Result is {int(denominator/nominator)}')
