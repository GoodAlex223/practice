# Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром,
# полученное умножением двух двузначных чисел – 9009 = 91 × 99.
# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
import time


start_time, result, temp_max = time.time(), [], 0
for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        palin = str(i*j)
        if palin == palin[::-1]:
            result.append(int(palin))
print(max(result), "--- %s seconds ---" % (time.time() - start_time), sep="\n")  # 906609

start_time, result = time.time(), []
for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        palin = str(i*j)
        if palin == palin[::-1]:
            result.append((i, j))
print(sorted([(abs(j-i), i*j) for i, j in result], key=lambda dif: (-dif[1], dif[0]))[0][1], "--- %s seconds ---" %
      (time.time() - start_time), sep="\n")

start_time, x, y, z = time.time(), 999, 999, 0
while y > 100:
    c = x * y
    if str(c) == str(c)[::-1] and c > z:
        z = c
    else:
        x -= 1
        if x == 100:
            x, y = y, y - 1
print(z, "--- %s seconds ---" % (time.time() - start_time), sep="\n")

# start_time, x, y, z = time.time(), 999, 999, []
# z1 = 0
# while y > 100:
#     c = x * y
#     if str(c) == str(c)[::-1] and c > z1:
#         z1 = c
#         z.clear()
#         z.append([x,y])
#     else:
#         x -= 1
#         if x == 100:
#             x = y
#             y -= 1
# print(z1, "--- %s seconds ---" % (time.time() - start_time), sep = "\n")
