# fruits = ["Watermelon", "Logan", "Rambutan"]
# for fruit in fruits:
#     print(fruit)

# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
#
# total_heights = 0
# num_student = 0
# for height in student_heights:
#     total_heights += height
#     num_student += 1
# avg_heights = total_heights / num_student
# print(f"Avg height is: {round(avg_heights)} cm")
# print(sum(student_heights))

# student_score = input("Input a list of student heights ").split()
# for n in range(0, len(student_score)):
#     student_score[n] = int(student_score[n])
# print(student_score)
#
# max_score = 0
# for score in student_score:
#     if score > max_score:
#         max_score = score
# print(f"The highest score in class is: {max_score}")
# print(max(max_score))

# for number in range(1, 11, 3):
#     print(number)
# sum_100 = 0
# for number in range(1, 101):
#     sum_100 += number
# print(sum_100)
# print(sum(range(1,101)))

# sum_even = 0
# for number in range(0, 101, 2):
#     sum_even += number
# print(sum_even)

# for num in range(1, 100):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

# import string
# import random
# letters = string.ascii_letters.lower()
# symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
# numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# print("Welcome to PyPass")
# num_letter = int(input("How many letter would you like in password? \n"))
# num_symbol = int(input("How many symbol would you like in password? \n"))
# num_number = int(input("How many number would you like in password? \n"))
# # 10 letter + 2 sym + 2 num
# ur_pass = ""
# for n in range(0, num_letter):
#     ur_pass += random.choice(letters)
# for n in range(0, num_symbol):
#     ur_pass += random.choice(symbols)
# for n in range(0, num_number):
#     ur_pass += random.choice(numbers)
#
# print(ur_pass)
# ur_pass = list(ur_pass)
# random.shuffle(ur_pass)
# print(ur_pass)
# ran_ur_pass = ""
# for n in range(0, len(ur_pass)):
#     ran_ur_pass += ur_pass[n]
# print(f"Your password is: {ran_ur_pass}")
