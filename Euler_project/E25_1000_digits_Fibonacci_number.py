"""Problem 25. 25/02/21 -- 30 min
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?"""
# def fib_n(numb):
#     if numb == 1 or numb == 2:
#         return 1
#     else:
#         return fib_n(numb - 1) + fib_n(numb - 2)

# prev_number, number, i = 1, 1, 2
# while len(str(number)) < 1000:
#     number, prev_number, i = number + prev_number, number, i + 1
# print(i)
import time


start = time.time()
result = [0, 1]
while len(result) != 1000000:
    result.append(result[-2] + result[-1])
print(time.time() - start, len(str(result[-1])))




