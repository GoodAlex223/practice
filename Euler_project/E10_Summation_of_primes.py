def summation_of_primes(period):
    """Summation of primes Problem 10. 15.01.21

    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million. result = 142913828922
    https://overcoder.net/q/295316/вывести-ряд-простых-чисел-в-python"""

    prime_list = [2]
    for prime in range(3, period+1, 2):
        if all(prime % k != 0 for k in range(2, int(prime**0.5)+1)):
            prime_list.append(prime)
    return prime_list


a = summation_of_primes(2000000)
print(sum(a))

