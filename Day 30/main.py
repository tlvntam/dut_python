"""Key, Index_array, Type Error"""

# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["non_key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_mess:
#     print(f"The key {error_mess} does not exist")
# else:
#     content = file.read
#     print(content)
# finally:
#     raise TypeError("This is an error that I made on")

"""Raise Error"""
# height = float(input("Height: "))
# weight = float(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human height < 3 meter")
# bmi = weight/height ** 2
# print(bmi)

# fruits = ["Apple", "Pear", "Orange"]
#
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + "pie")
#
#
# make_pie(4)

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

# total_likes = 0
#
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         # total_likes += 0
#         pass
# print(total_likes)

