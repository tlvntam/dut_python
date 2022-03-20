# with open("file1.txt") as file_1:
#     new_file_1 = []
#     for line in file_1:
#         new_file_1.append(int(line))
#     print(new_file_1)
#
# with open("file2.txt") as file_2:
#     new_file_2 = []
#     for line in file_2:
#         new_file_2.append(int(line))
#     print(new_file_2)
#
# result = [num for num in new_file_1 if num in new_file_2 ]
# print(result)

# with open("file1.txt") as file_1:
#     new_file_1 = file_1.readlines()
#
# with open("file2.txt") as file_2:
#     new_file_2 = file_2.readlines()
#
# result = [int(num) for num in new_file_1 if num in new_file_2 ]
# print(result)

# miss_state = [state for state in 50_state if state not in guess_state]

