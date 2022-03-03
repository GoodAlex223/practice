from timeit import timeit
# (https://www.kontrolnaya-rabota.ru/s/grafik/tochka/)
# Как можно ускорить: в for d in [i for i in range(2, limit) if all(i % k != 0 for k in range(2, int(i ** 0.5) + 1))]:  # for d in range(11, limit):
# в параметре цикла генератора значения отсчета цикла (2 в range(2, limit)) можно заменить int(limit*х), где х - знчение
# от 0 до 1(0.1231, 0.232 и тд), что означает процент, при умножения лимита на который получаеться наибольшее значение
# от которого можно начинать поиск всех простых чисел. Я пробовал разные значения, но для большинства значений лимита
# (>10) подходит значение 0.5, но с лимитом=10000 и больше это до сих пор много.
# Можно пойти еще дальше и построить график функции зависимости значений лимита и
# процента от лимита, который составляет вывод(число, рекурсивное значения десятичных знаков еоторого, являеться
# наибольшим в некотором периоде (до значения лимита)) и, если будет прослеживаться какая-то закономерность, сделать
# параметр х изменчивым, в зависимости от условий (например,лимит = до10, х = 0.7, до30, х = 0.95 и тд.)


def calc_longest_recur_cycle(limit=1000):
    # The maximum length
    max_len = 0
    # The 'd' that has maximum length
    max_d = 1
    for d in [i for i in range(2, limit) if all(i % k != 0 for k in range(2, int(i ** 0.5) + 1))]:  # for d in range(11, limit):
        quotient = {0: 0}
        # Stores the decimal quotient, quotient is initiated as quotient = {0: 0}(instead of list)
        # to eliminate cur_value evaluation on the while loop condition.
        cur_value = 1  # Variable used to perform division as if by hand
        len_recur = 0  # Recurring length

        # Performing division as if by hand.
        while cur_value not in quotient:

            len_recur += 1
            quotient[cur_value] = len_recur
            cur_value = (cur_value % d) * 10
            # cur_value is appended
            # synchronously with incrementing
            # len_recur i.e. the cur_value will get the
            # position equal to len_recur
            # That means that, on this level,
            # cur_value can be mapped to its position
            # contained in len_recur.
        if not cur_value:
            continue

        # Remove number of values that do not recur
        len_recur -= quotient[cur_value]

        if len_recur > max_len:
            max_len = len_recur
            max_d = d

    return max_d
# NOT PRIME NUMBERS -- 9967, 7.224353806000001 (limit=10000)
# PRIME NUMBERS -- 9967, 2.90448182 (limit=10000)


print(calc_longest_recur_cycle())
print(timeit('calc_longest_recur_cycle()', 'from __main__ import calc_longest_recur_cycle', number=1))
