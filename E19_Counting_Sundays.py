"""18.02.21/Problem 19
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
week_day = "Mon"
week_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
month_dict = {
    "Jan": 31, "Feb": 29, "Mar": 31, "Apr": 30, "May": 31, "Jun": 30,
    "Jul": 31, "Aug": 31, "Sep": 30, "Oct": 31, "Nov": 30, "Dec": 31
}
count = 1
for year in range(1900, 2001):
    for month in month_dict.keys():
        if year % 4 == 0 and year % 400 != 0 or month != "Feb":
            number = month_dict[month] - 29 + 1
            # Находим число, через значение которого от последней полной недели наступит первый день след. месяца
            # Полных недель в месяце(кроме невисокосного февраля) -- 4(7*4=28).
            # А значит можно пропустить сразу 28 дней.
            # Тогда от 29(28+1(первый день)) дня настоящего месяца продолжаем поиск дня недели
            # первого дня следующего месяца. Таким образом осуществляеться поиск всех дней всем месяцев во всех годах
        else:
            number = month_dict[month] - 23 + 1
        # Для невисокосного февраля именно 23, а не 22(7*3=21(+1)),
        # чтобы значение в словаре постоянно не менять. Если 28 - 22 = 29 - 23, тогда в словаре постоянное значение 29 в
        # пользу примененния и для високосных лет,
        # а кол. дней, которые можно пропустить -- 23
        week_day = week_days[week_days.index(week_day) + number]
        # Так как опреатор index() находит первое вхождения элемента в список и список с продублированными значениями
        # не возникает проблем с поиском дня недели первого дня месяца по индексу в списке
        if week_day == "Sun" and year > 1900:
            count += 1
            # По условию задаачи необходимо учитывать вскр. с 1901 года
print(count)
