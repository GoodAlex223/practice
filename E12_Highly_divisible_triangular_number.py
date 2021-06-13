import math

"""The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
http://pythoneuler.blogspot.com/2016/10/12.html
"""
len_of_divisors, number, count_of_divisors, counter = 2, 3, 500, 2
while len_of_divisors <= count_of_divisors:
    len_of_divisors = 2  # 1. Первоначальное количество делителей = 2 (чтобы не перебирать 1 и само число)
    number = sum(list(range(1, counter+1)))  # Само треугольное число
    for k in range(2, math.ceil(number**0.5)+1):
        # 2. Делители рассматриваем в промежутке от 2 до квадратного корня числа.
        if number % k == 0:
            len_of_divisors += 2
            # 3. При нахождении делителя увеличиваем их количество на 2 (т.к делители всегда ходят парами)
    if math.ceil(number ** 0.5) ** 2 == number:  # Если число имеет целый квадратный корень, то
        len_of_divisors -= 1
        # 4. Если число представляет собой точный квадрат (имеет целый корень) уменьшаем результирующее
        # количество делителей на 1.
    counter += 1
print(number)  # 76576500
# def is_perf_sq(n):
#     x = math.ceil((math.sqrt(n)))
#     if x*x == n:
#         return True
#     else:
#         return False
#
# # Далее функция, возвращающая первое треугольное число
# def max_triangular(m):
#     x = 3
#     n = 2
#     while n <= m:
#         n = 2
#         num = sum([c for c in range(1, x+1)])
#         for i in range(2, math.ceil(math.sqrt(num))):
#             if num % i == 0:
#                 n += 2
#         if is_perf_sq(num):
#                 n -= 1
#         x += 1
#     return num
# print(max_triangular(500))  #   76576500

# triangular_numbers, temp_max_len = {1: 1, 3: 2}, 0
# number, last_numb = 3, 2
# len_of_divisors = 2  # Cамо число и 1
# temp_len_of_divisors = len_of_divisors
# # while len([k for k in range(3, (number//2)+1) if number % k == 0] + [1, 2, number]) <= count_of_divisors:
# while len_of_divisors <= 500:
#     len_of_divisors = 2
#     last_numb += 1
#     number += last_numb
#     while number % 2 != 0:
#         last_numb += 1
#         number += last_numb
#     counter_for_loop = (number // 2) + 1
#     print(sorted(triangular_numbers, reverse=True))
#     for j in sorted(triangular_numbers, reverse=True):
#         if number % int(j) == 0:
#             len_of_divisors = int(triangular_numbers[j])
#             for k in range(int(j)+1, counter_for_loop):
#                 if number % k == 0:
#                     len_of_divisors += 1
#             # print(len_of_divisors)
#             triangular_numbers[number] = len_of_divisors
#         break
#     # for k in range(2, counter_for_loop):
#     #     if number % k == 0:
#     #         len_of_divisors += 1
#     if len_of_divisors > temp_len_of_divisors:
#         print(number, len_of_divisors)
#         temp_len_of_divisors = len_of_divisors
# # print(len_of_divisors)


# triangular_numbers, count_of_divisors, number, last_numb, temp_max_len = {1: [1]}, 100, 1, 1, 0
# start_time = time.time()
# while len(triangular_numbers[number]) <= count_of_divisors:
#     last_numb += 1
#     number += last_numb
#     triangular_numbers[number] = [1] + [k for k in range(2, (number//2)+1) if number % k == 0] + [number]
#     if len(triangular_numbers[number]) > temp_max_len:
#         print(number, len(triangular_numbers[number]))
#         temp_max_len = len(triangular_numbers[number])
# # print(triangular_numbers)
# print(time.time() - start_time)

# count_of_divisors, start_time = 500, time.time()
# i = 5000
# triangular_number = sum(list(range(1, i+1)))
# list_of_divisors = len([k for k in range(2, (triangular_number//2)+1) if triangular_number % k == 0]) + 2
# while list_of_divisors <= count_of_divisors:
#     i += 1
#     triangular_number = sum(list(range(1, i+1)))
#     while triangular_number % 2 != 0:
#         i += 1
#         triangular_number = sum(list(range(1, i + 1)))
#     list_of_divisors = len([k for k in range(2, (triangular_number//2)+1) if triangular_number % k == 0]) + 2
#     print(triangular_number)  #
# print(time.time() - start_time)  # 92.34728217124939

# count_of_divisors, number, last_numb = 5, 1, 1
# len_of_list = temp_len_of_list = len([k for k in range(2, (number // 2) + 1) if number % k == 0] + [1, number])
# while len_of_list <= count_of_divisors:
#     len_of_list = len([k for k in range(2, (number // 2) + 1) if number % k == 0] + [1, number])
#     print(number)
#     last_numb += 1
#     number += last_numb


#     last_numb += 1
#     number += last_numb
#     list_of_divisors = len([k for k in range(2, (number // 2) + 1) if number % k == 0] + [1, number])
#     if list_of_divisors > temp_list_of_divisors:
#         temp_list_of_divisors = list_of_divisors
#     elif list_of_divisors <= temp_list_of_divisors:
#         last_numb += 1
#         number += last_numb
#     print(number)
# print(number)  # 11103828: last for my prog triangle number

# count_of_divisors, number, last_numb, limit = 500, 1, 1, 50
# while len(str(number)) <= limit:
#     last_numb += 1
#     number += last_numb
#     print(number)
# print(len([k for k in range(1, (number//2)+1) if number % k == 0] + [number]))  # 945555257548450

