import time


def sum_square_difference(period):
    """Разность между суммой квадратов и квадратом суммы. Проект Эйлера. Задача 6(11.01.21)

    Сумма квадратов первых десяти натуральных чисел равна
    1**2 + 2**2 + ... + 10**2 = 385
    Квадрат суммы первых десяти натуральных чисел равен
    (1 + 2 + ... + 10)**2 = 552 = 3025
    Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел составляет
    3025 − 385 = 2640.
    Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел."""
    start_time, sum_of_sqrs, sqr_of_sum, diff = time.time(), 0, 0, 0
    for i in range(1, period+1):
        sum_of_sqrs += i**2
        sqr_of_sum += i
    diff = sqr_of_sum**2 - sum_of_sqrs
    print(diff, "--- %s seconds ---" % (time.time() - start_time), sep="\n")

    start_time = time.time()
    sum_of_sqrs = sum([i ** 2 for i in range(1, period + 1)])
    sqr_of_sum = sum([i for i in range(1, period + 1)])**2
    diff = sqr_of_sum - sum_of_sqrs
    print(diff, "--- %s seconds ---" % (time.time() - start_time), sep="\n")

    start_time = time.time()
    print(sum([i for i in range(1, period + 1)]) ** 2 - sum([i ** 2 for i in range(1, period + 1)]),
          "--- %s seconds ---" % (time.time() - start_time), sep="\n")


sum_square_difference(100)  # 25164150
