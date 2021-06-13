"""Задача 3
Наибольший простой делитель
Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?"""
import time
numb, result, k, start_time = 600851475143, set(), 3, time.time()
while k**2 < numb:
    if numb % k == 0:
        result.add(k)
        j = 2
        while j ** 2 <= k:
            if k % j == 0 and k in result:
                result.discard(k)
            j += 1
    k += 2
print(max(list(result)), "--- %s seconds ---" % (time.time() - start_time), sep="\n")  # 6857
# or Bad Decision(longer solution time x2)
# import time
# start_time = time.time()
# result, numb = set(), 600851475143
# [result.add(i) for i in range(2, numb) if numb % i == 0]
# temp_result, result = list(result), list(result)
# [[result.remove(i) for j in range(2, i) if i % j == 0 and i in result] for i in temp_result]
# print(*result, "--- %s seconds ---" % (time.time() - start_time), sep = "\n")

# Same Decision
# import time
# start_time = time.time()                    # начинаем отсчёт времени, чтобы знать сколько выполняется программа
# ish = 600851475143
# s = 3                    # поиск простых делителей начинаем с трёх и увеличиваем число на 2, т.к. чётные числа не могут быть простыми
# lst = []
# marker = False
# while s**2 <= ish:
#     if ish % s == 0:
#         lst.append(s)
#         lst.append(ish//s)                                      # добавляем не только найденный делитель, но и второй делитель, т.к. делителя всегда два.
#     s += 2                                                      # чётное число не может быть простым, так что проходимся только по нечётным
# lst.sort()
# s = 0
# for i in lst:
#     if i > 5 and i % 10 == 5:                                   # если число больше 5 и кончается на 5, оно не простое, т.к. делится на 5
#         continue
#     for j in range(2, int(i/2)):
#         if j * j - 1 > i:                                       # если счёт дошёл до квадратного корня из числа и делителей у числа всё ещё нет, значит оно простое
#             if i > s:
#                 s = i
#                 break
#         if i % j == 0:
#             break
#     else:
#         if i > s:
#             s = i
# print(lst)
# print(s)
# print("--- %s seconds ---" % (time.time() - start_time))        # вывод времени выполнения программы