# height = float(input("Enter ur height in m: "))
# weight = float(input("Enter ur weight in kg: "))
# BMI = weight / (height ** 2)
# if float(BMI) < 18.5:
#     print(f"Ur BMI is {round(BMI)}. U're underweight")
# elif float(BMI) < 25:
#     print(f"Ur BMI is {round(BMI)}. U're normal weight")
# elif float(BMI) < 30:
#     print(f"Ur BMI is {round(BMI)}. U're overweight")
# elif float(BMI) < 35:
#     print(f"Ur BMI is {round(BMI)}. U're obese")
# else:
#     print(f"Ur BMI is {round(BMI)}. U're clinically obese")

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


# height = int(input("Enter your height: "))
# if height >= 120:
#     print("Can ride")
#     age = int(input("Enter your age: "))
#     if age < 12:
#         bill = 5
#         print("U must pay $5 for child ticket")
#     elif age <= 18:
#         bill = 7
#         print("U must pay $7 for youth ticket")
#     elif 45 <= age and age <= 55:
#         bill = 0
#         print("U've free ride")
#     else:
#         bill = 12
#         print("U must pay $12 for adult ticket")
#
#     photo = input("Do u want photo? (Y/N) ")
#     if photo == "Y":
#         bill += 3
#         print(f"Ur total bill is ${int(bill)}")
#     else:
#         print(f"Ur total bill is ${int(bill)}")
# else:
#     print("Can't ride")

# print("Welcome")
# sz_pizza = input("What sz u want? (S, M, L) ")
# add_pepperoni = input("Do u want pepperoni ? (Y or N) ")
# extra_chess = input("Do u want extra chess? (Y or N) ")
# bill = 0
# if sz_pizza == "S":
#     bill += 15
# elif sz_pizza == "M":
#     bill += 20
# elif sz_pizza == "L":
#     bill += 25
# else:
#     print("Sorry we don't have that sz !!!")
#
# if add_pepperoni == "Y":
#     if sz_pizza == "S":
#         bill += 2
#     elif sz_pizza == "M" or sz_pizza == "L":
#         bill += 3
#
# if extra_chess == "Y":
#     bill += 1
#
# print(f"Ur total bill is ${bill}")

# print("Welcome 2 Love Calculator !!!")
# boy_name = input("Enter the boy's name: ").lower()
# girl_name = input("Enter the girl's name: ").lower()
# both_name = boy_name + " " + girl_name
#
# t_total = both_name.count("t")
# r_total = both_name.count("r")
# u_total = both_name.count("u")
# e_total = both_name.count("e")
#
# true_total = t_total + r_total + u_total + e_total
#
# l_total = both_name.count("l")
# o_total = both_name.count("o")
# v_total = both_name.count("v")
#
# love_total = l_total + o_total + v_total + e_total
#
# if true_total >= 10:
#     true_total = 9
# if love_total >= 10:
#     love_total = 9
#
# true_love = true_total + love_total
# if true_love < 10 or true_love > 90:
#     print(f"Your score is {true_total}{love_total}%, you together like coke and mentos")
# elif true_love >= 40 and true_love <= 50:
#     print(f"Your score is {true_total}{love_total}%, you are right together")
# else:
#     print(f"Your score is {true_total}{love_total}%")

# print("Welcome to Tresure Island")
# l_or_r = input("You're at a cross land. Where do you want to go? Type 'left' or 'right': ")
# if l_or_r == "left":
#     w_or_s = input("You come to a lake. Type 'wait' or 'swim': ")
#     if w_or_s == "wait":
#         color = input("There is a house with 3 doors. Which color do you choose? Type 'red', 'yellow' or 'blue' ")
#         if color == "yellow":
#             print("You Win")
#         else:
#             print("Game over")
#     else:
#         print("Game over")
# else:
#     print("Game over")



