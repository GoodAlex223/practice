"""If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total. If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British
usage.
"""
hundreds, spec_hundred, from_thirteen_to_twenty, tens = "hundredand", "hundred", "teen", "ty"
spec_numbs_to_hundred = {
    2: "twen", 3: "thir", 4: "for", 5: "fif", 6: "six", 7: "seven", 8: "eigh", 9: "nine"
}
numbers = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen"
}
for number in range(15, 1000):
    if number in {100, 200, 300, 400, 500, 600, 700, 800, 900}:
        numbers[number] = numbers[int(str(number)[0])] + spec_hundred
    elif number > 100:
        numbers[number] = numbers[int(str(number)[0])] + hundreds + numbers[int(str(number)[1:])]
    elif number in {20, 30, 40, 50, 60, 70, 80, 90}:
        numbers[number] = spec_numbs_to_hundred[int(str(number)[0])] + tens
    elif 20 < number < 100:
        numbers[number] = spec_numbs_to_hundred[int(str(number)[0])] + tens + numbers[int(str(number)[1])]
    elif 14 < number < 20:
        numbers[number] = spec_numbs_to_hundred[int(str(number)[1])] + from_thirteen_to_twenty
print(sum([len(i) for i in numbers.values()])+11)  # Сразу посчитали количество букв в цифре one thousand (21124)
