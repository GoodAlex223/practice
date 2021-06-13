"""Problem 22. 22/02/21
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?"""
alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
with open("p022_names.txt") as names:
    names = sorted(names.read().replace('"', "").split(","))
    for name in names:
        a_val = 0
        for letter in name:
            a_val += alphabet.index(letter) + 1
        names[names.index(name)] = a_val * (names.index(name) + 1)
print(sum(names))  # 871198282
