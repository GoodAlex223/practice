def prime_10001st(number):
    """10001st prime. Problem 7. 12.01.21

    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10 001st prime number?"""

    numb_prime, prime = 5, 13

    while numb_prime < number:
        is_prime = True                        # Checking the number for simplicity
        for k in range(3, (prime // 2) + 1):
            if prime % k == 0:
                is_prime = False               # If number is not prime, it skips
                break
        if is_prime:
            numb_prime += 1
            print(prime)
        if numb_prime == number:
            break
        prime += 2
    return numb_prime, prime


print(prime_10001st(10001))  # (10001, 104743)


# start_time, i, primes = time.time(), 3, {1, 2}  # numbers 1, 2, 3 are used everywhere for dividing
#
#     if len(primes) != number:
#         for j in range(2, number//2 + 1):
#             if i % j == 0:
#                 i = i / j
#                 break
#         primes.add(i)                            # Adding a prime number
#     else:
#         break
# print(sorted(list(primes)), len(primes), sorted(list(primes))[number - 1],
#       "--- %s seconds ---" % (time.time() - start_time), sep="\n")

# x, n, start_time = number//2+1, [], time.time()
# while n < number:
#     x += 1
#     z = [i for i in range(1, x+1) if x % i == 0]
#     if len(z) == 2:
#         n.append(x)
# print(len(n), n, x, "--- %s seconds ---" % (time.time() - start_time), sep="\n")

# Don't work
# prime, prime_number, start_time = [2, 3, 5, 7, 11], 13, time.time()
# numb_prime = len(prime)
# #
# while numb_prime < number:
#     is_prime = True  # Checking the number for simplicity
#     for k in range(2, (prime[numb_prime - 1] // 2) + 1):
#         if prime_number % k == 0:
#             is_prime = False  # If number is not prime, it skips
#             break
#     if is_prime:
#         prime.append(prime_number)
#     if numb_prime == number:
#         break
#     prime_number += 2
# print(numb_prime, prime, prime_number, "--- %s seconds ---" % (time.time() - start_time), sep="\n")
