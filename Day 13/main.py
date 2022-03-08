# def my_function():
#     for i in range(1,21):
#         if i == 20:
#             print("You got it")
# my_function()

# from random import randint
# dice_imgs = ["1", "2", "3", "4", "5", "6"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# year = int(input("What's ur year of birth? "))
# if year > 1980 and year <= 1994:
#     print("You are a millenial.")
# elif year > 1994:
#     print("You are a gen Z.")


# age = int(input("How old are you? "))
# if age > 18:
#     print(f"You can drive at age {age}")

# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)
#
# mutate([1,2,3,5,8,13])

# number = int(input("which num to check? "))
# if number % 2 == 0:
#     print("Even number")
# else:
#     print("Odd num")

# year_check = int(input("Enter year to check: "))
# if year_check % 4 == 0:
#     if year_check % 100 == 0:
#         if year_check % 400 == 0:
#             print(f"So the year {year_check} is a leap year")
#         else:
#             print(f"So the year {year_check} is not a leap year")
#     else:
#         print(f"So the year {year_check} is a leap year")
# else:
#     print(f"So the year {year_check} is not a leap year")

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)