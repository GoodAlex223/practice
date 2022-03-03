# Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром,
# полученное умножением двух двузначных чисел – 9009 = 91 × 99.
# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
import time


# start_time, result, temp_max = time.time(), [], 0
# for i in range(999, 99, -1):
#     for j in range(i, 99, -1):
#         palin = str(i*j)
#         if palin == palin[::-1]:
#             result.append(int(palin))
# print(max(result), "--- %s seconds ---" % (time.time() - start_time), sep="\n")  # 906609

def largest_palindrome(start=999, stop=99):
    start_time, result = time.time(), []
    for i in range(start, stop, -1):
        for j in range(i, stop, -1):
            palin = i * j
            if str(palin) == str(palin)[::-1]:
                result.append((palin, i, j))
    return sorted(result, reverse=True)[0], "--- %s seconds ---" % (time.time() - start_time)


def largest_palindrome_2(start=999, stop=99):
    start_time, result, max_p = time.time(), [], 0
    for i in range(start, stop, -1):
        for j in range(i, stop, -1):
            palin = i * j
            if str(palin) == str(palin)[::-1] and palin > max_p:
                max_p = palin
    return max_p, "--- %s seconds ---" % (time.time() - start_time)


# start, stop = 999, 99
# print(largest_palindrome(start, stop), sep='\n')
# print(largest_palindrome_2(start, stop), sep='\n')
# 999, 99 -- ((906609, 993, 913), '--- 0.8820023536682129 seconds ---')
# 999, 99 -- (906609, '--- 0.7600011825561523 seconds ---')

# For one word test for palindrome most effective algorithm in memory usage:
# word = 'abcdefghihgfedcba' * 10**6
# start = time.time()
# j = len(word) - 1
# for i in range(len(word)//2):
#     if word[i] != word[j]:
#         print("No")
#         break
#     else:
#         j -= 1
# else:
#     print("Yes")
# print(time.time() - start)
#
# start = time.time()
# if word == word[::-1]:
#     print("Yes")
# else:
#     print("No")
# print(time.time() - start)

