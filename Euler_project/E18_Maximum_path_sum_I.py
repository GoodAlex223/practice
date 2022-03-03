"""Maximum path sum I
Отправить

 Show HTML problem content
Problem 18
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                            75
                          95 64
                        17 47 82
                      18 35 87 10
                    20 04 82 47 65
                  19 01 23 75 03 34
                88 02 77 73 07 63 67
              99 65 04 28 06 16 70 92
            41 41 26 56 83 40 80 70 33
          41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
      70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
  63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
it cannot be solved by brute force, and requires a clever method! ;o)
решение(идея)(моя реализация оригинальна) -- https://lucidmanager.org/data-science/project-euler-18/
тоже хорошая статья -- https://radiusofcircle.blogspot.com/2016/04/problem-18-project-euler-solution-with-python.html"""
tril = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""".split("\n")
tril_lists = []
[tril_lists.append([int(j) for j in i.split()]) for i in tril]
curr_index = 0
total = tril_lists[0][0]

# Мое решение версия 1.0 (работала)
for curr_step in range(1, len(tril_lists)):
    tril_lists_copy = tril_lists[:]
    for curr_list in range(len(tril_lists_copy)-1, curr_step, -1):  # tril_lists_copy[::-1]:
        temp_list = []
        for numb in range(1, len(tril_lists_copy[curr_list])):
            temp_list.append(max(tril_lists_copy[curr_list][numb:numb+2]))
        tril_lists_copy[curr_list - 1] = []
        for i in range(0, len(tril_lists_copy[curr_list])):
            tril_lists_copy[curr_list - 1].append(tril_lists[curr_list - 1][i] + temp_list[i])
    curr_index = tril_lists_copy[curr_step].index(max(tril_lists_copy[curr_step][curr_index:curr_index + 2]))
    total += tril_lists[curr_step][curr_index]
print(total)

# Мое решение версия 2.0
tril = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""".split("\n")
tril_lists = []
[tril_lists.append([int(j) for j in i.split()]) for i in tril]

for curr_list in range(len(tril_lists)-1, 1, -1):  # tril_lists_copy[::-1]
    for i in range(0, len(tril_lists[curr_list - 1])):
        tril_lists[curr_list-1][i] = tril_lists[curr_list-1][i] + (max(tril_lists[curr_list][i], tril_lists[curr_list][i+1]))
print(max(tril_lists[1]) + tril_lists[0][0])

# Код для прибавления большего числа
# for i in range(1, len(tril_lists)):
#     print(tril_lists[i].index(max(tril_lists[i])))
#     temp_list += [int(tril_lists[i][index]), int(tril_lists[i][index+1])]
#     print(max(temp_list))
#     result += max(temp_list)
#     index = (index, index+1)[temp_list.index(max(temp_list))]
#     temp_list.clear()
# print(result)

# indexes_list = []
# for i in tril_lists:
#     temp_list = i.copy()
#     i_list = []
#     for j in range(len(temp_list)):
#         max_numb = max(temp_list)
#         i_max_numb = temp_list.index(max_numb)
#         i_list.append(i_max_numb)
#         temp_list[i_max_numb] = 0
#     indexes_list.append(i_list)
# print(indexes_list)
# total = tril_lists[indexes_list[0][0]]
# curr_i = 0
# i_place_l_d = {}  # Indexes' place list in dictionary
# i_place_d = {}  # Indexes' place in dictionary
# result_list = [0]  #
# for current_step in range(1, len(indexes_list)):
#     for arr_i in range(current_step, len(indexes_list)):
#         i_place_l_d[curr_i] = i_place_l_d.get(curr_i, []) + [indexes_list[arr_i].index(curr_i)]
#         # Listing all counted places in all lines for current index and index + 1 and saving to dict with key,
#         # respectively
#         i_place_l_d[curr_i + 1] = i_place_l_d.get(curr_i + 1, []) + [indexes_list[arr_i].index(curr_i + 1)]
#     for index in i_place_l_d:
#         i_place_d[index] = (sum(i_place_l_d[index])+len(i_place_l_d[index])) / len(i_place_l_d[index])
#         # Sum all places and dividing by count of rest of lines is indicator of average place in the triangle
#     if i_place_d[curr_i] > i_place_d[curr_i + 1]:
#         curr_i += 1
#     elif i_place_d[curr_i] == i_place_d[curr_i + 1]:
#         i = 1
#         while i_place_d[curr_i] == i_place_d[curr_i + i] and curr_i + i + 1 < len(indexes_list[-1]):
#             i += 1
#             i_place_l_d[curr_i + i] = []
#             for k in range(current_step+i-1, len(indexes_list)):
#                 i_place_l_d[curr_i + i] = i_place_l_d.get(curr_i + i, []) + [indexes_list[k].index(curr_i + i)]
#             i_place_d[curr_i + i] = (sum(i_place_l_d[curr_i + i])+len(i_place_l_d[curr_i + i])) / len(i_place_l_d[curr_i + i])
#         if i_place_d[curr_i] > i_place_d[curr_i + i]:
#             curr_i += 1
#     result_list.append(curr_i)
#     i_place_l_d[curr_i] = []
#     i_place_l_d[curr_i + 1] = []
# print(result_list, len(result_list))