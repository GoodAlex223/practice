"""Quadratic primes/Problem 27 -- 14.04.21

Euler discovered the remarkable quadratic formula:
n**2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0<=n<=39.
However, when n = 40, 40**2 + 40 + 41 = 40 * (40 + 1) + 41 is divisible by 41, and certainly when n = 41,
41**2 + 41 + 41 is clearly divisible by 41.

The incredible formula n**2 - 79*n + 1601 was discovered, which produces 80 primes for the consecutive values 0<=n<=79.
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n**2 + a*n + b, where |a| < 1000 and |b| < 1000,
where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes
for consecutive values of n, starting with n = 0.
S O L U T I O N(набросок):
VER.1 -- Сначало, нужно посмотреть каким образом образовываються такие формулы. Для этого можно сделать такие действия:
0.1 Определяем 2 списка простых чисел в диапазоне от -999 до 999 (a_pl, b_pl)
0.2 Определения параметра max_n, который будет хранить значение длины списка prime_list (max_n = 0).
1. Первый цикл для сменны параметра а в уравнении в диапазоне a_pl
2. Второй цикл, вложенный в первый, для сменны параметра в диапазоне b_pl
3. Определения параметра n (n=0)
4. Определения параметра numb, который будет хранить число, которое высчитываетьтся с сформированной списками
формулы
5. Третий цикл, вложенный во второй, для смены параметра n (пока numb не будет не простым*)
* - проверка с помощью генератора списков(while all([numb%check!=0 for check in range(2, int(numb**0.5)+1)]):)
6. Высчитывание числа по сгенерированной формуле (numb = numb**2 + a * numb + b)
7. Во втором цикле определяется проверка, больше или равна ли значение n, чем значение max_n. Если да,
то параметру max_n присваевается значение n, параметры а
"""
import math
import time


# a=3000, time=25.96248507499695s
def QP_ver1(a=2000):  # Если период a = периоду b
    start = time.time()
    a_pl = [2] + [i for i in range(3, a + 1, 2) if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1))]
    a_pl = sorted([-i for i in a_pl]) + a_pl
    # a_pl = [i for i in range(-a+1, a + 1, 2) if all(i % j != 0 for j in range(2, int(abs(i) ** 0.5) + 1))]
    # b_pl = a_pl[:]
    # # b_pl = [i for i in range(-b+1, b + 1, 2) if all(i % j != 0 for j in range(2, int(abs(i) ** 0.5) + 1))]
    max_n = (0, 0, 0)
    for a_n in a_pl:  # range(-a + 1, a):
        for b_n in a_pl:  # range(-b + 1, b):
            n = 0
            numb = n ** 2 + a_n * n + b_n
            while all(numb % i != 0 for i in range(2, int(abs(numb) ** 0.5) + 1)):  # range(2, (numb // 2) + 1)):
                n += 1
                numb = n ** 2 + a_n * n + b_n
            if n > max_n[0]:
                max_n = (n, a_n, b_n)
    return f'{max_n}, {time.time() - start}s'


def QP_ver2(a=2000):  # a=3000, time=1.8481056690216064s
    start = time.time()

    def sieve(n):  # sieve of Eratosthenes
        is_prime = [True] * n
        is_prime[0] = False
        is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            index = i * 2
            while index < n:
                is_prime[index] = False
                index += i
        prime_l = []
        for i in range(n):
            if is_prime[i]:
                prime_l.append(i)
        return prime_l

    b_pl = sieve(a)
    a_pl = sorted([-i for i in b_pl]) + b_pl
    b_ps = set(b_pl)
    max_n = (0, 0, 0)
    for a_n in a_pl:  # range(-a + 1, a):
        for b_n in b_pl:  # range(-b + 1, b):
            n = 0
            numb = n ** 2 + a_n * n + b_n
            # all(numb % i != 0 for i in range(2, int(abs(numb) ** 0.5) + 1)):  # range(2, (numb // 2) + 1)):
            while abs(numb) in b_ps:
                n += 1
                numb = n ** 2 + a_n * n + b_n
            if n > max_n[0]:
                max_n = (n, a_n, b_n)
    return f'{max_n}, {max_n[1] * max_n[2]}, {time.time() - start}s'


print(QP_ver1())  # (71, -61, 971)
print(QP_ver2())
