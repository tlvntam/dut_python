import random
# import my_module

# random_integer = random.randint(1, 10)
# print(random_integer)
# random_float = random.random() * 5
# print(random_float)

# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# random_side = random.randint(0, 1)
# if random_side == 1:
#     print("Heads")
# else:
#     print("Tails")

# image_game = ["Rock - ✊", "Paper - ✋", "Scissors - ✌", "Error"]
# print("Ready to lose ???")
# player_name = input("Enter your name: ")
# player_score = 0
# clone_score = 0
#
# while player_score <= 3 or clone_score <= 3:
#     player_choice = int(input("Choose 0 for Rock, 1 for Paper or 2 for Scissors: "))
#     clone_choice = random.randint(0, 2)
#     print(f"Bot choose {image_game[clone_choice]}")
#     if player_choice >= 3:
#         print(f"You choose {image_game[3]}")
#     else:
#         print(f"You choose {image_game[player_choice]}")
#
#     if player_choice >= 3:
#         clone_score += 1
#         print("Invalid num, you lose")
#     if player_choice == clone_choice:
#         print("We draw !!! Try again broooo .,.")
#
#     if player_choice == 0 and clone_choice == 1:
#         clone_score += 1
#         print("You lose!!!")
#     if player_choice == 1 and clone_choice == 2:
#         clone_score += 1
#         print("You lose!!!")
#     if player_choice == 2 and clone_choice == 0:
#         clone_score += 1
#         print("You lose!!!")
#     if clone_choice == 0 and player_choice == 1:
#         player_score += 1
#         print("You Win!!!")
#     if clone_choice == 1 and player_choice == 2:
#         player_score += 1
#         print("You Win!!!")
#     if clone_choice == 2 and player_choice == 0:
#         player_score +=1
#         print("You Win!!!")
#     print(f"\nTỉ số là {player_name}:{player_score} - tum_bot:{clone_score} \n")
#
#     if player_score == 3 or clone_score == 3:
#         if player_score > clone_score:
#             print("Winner winner chicken dinner")
#         else:
#             print("Chicken .,. ")
#         break

# city_vietnam = ["HaNoi", "DaNang", "HCM", "HaiPhong"]
# city_vietnam = [northside, southside]
# city = city_vietnam[1]
# city_vietnam[3] = "DaLat"
# city_vietnam.append("CamRanh")
# city_vietnam.extend(["NhaTrang", "QuyNhon"])
#
# print(city_vietnam)

# test_seed = int(input("Create a seed number "))
# random.seed(test_seed)
#
# namesAsCSV = input("Give me everybody's names: ")
# names = namesAsCSV.split(", ")
# lucky_num = len(names)
# print(f"{names[random.randint(0,lucky_num -1)]} is going to pay")
#
# print(f"{random.choice(names)} is going to pay")

# row_1 = ["⬛", "⬛", "⬛"]         #getemoji
# row_2 = ["⬛", "⬛", "⬛"]
# row_3 = ["⬛", "⬛", "⬛"]
# map = [row_1, row_2, row_3]
# print(f"{row_1}\n{row_2}\n{row_3}")
# position = input("Where do you want tu put the treasure ")
#
# first_num = int(position[0])
# second_num = int(position[1])
#
# row_change = map[second_num -1]
# row_change[first_num -1] = "X"
# print(f"{row_1}\n{row_2}\n{row_3}")
# if first_num == 1:
#     if second_num == 1:
#         row_1[0] = "X"
#     if second_num == 2:
#         row_2[0] = "X"
#     if second_num == 3:
#         row_3[0] = "X"
#
# if first_num == 2:
#     if second_num == 1:
#         row_1[1] = "X"
#     if second_num == 2:
#         row_2[1] = "X"
#     if second_num == 3:
#         row_3[1] = "X"
#
# if first_num == 3:
#     if second_num == 1:
#         row_1[2] = "X"
#     if second_num == 2:
#         row_2[2] = "X"
#     if second_num == 3:
#         row_3[2] = "X"


