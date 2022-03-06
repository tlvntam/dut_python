# game_level = 3
# def create_enemies():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemies = enemies[0]
#
#     return new_enemies
#
# print(create_enemies())
#
# """Global"""
# enemies = 4
#
# def increse_enemies():
#     """Local"""
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1
#
# enemies = increse_enemies()
# print(f"enemies outside function: {enemies}")
#
# PI = 3.14159

import random
from replit import clear
from art import logo

def live_total(game_level):
    if game_level == "easy":
        return 8
    else:
        return 6

def live_remaining(live_remain):
    live_remain -= 1
    return live_remain

def game_gtn(player_guess, live_remain, correct_num):
    if player_guess == correct_num:
        print(f"You got it! The answer was {correct_num}")
        print(f"Correct num is: {correct_num}")
        try_1_more()
    elif player_guess < correct_num:
        live_remain = live_remaining(live_remain)
        return "Too low"
    elif player_guess > correct_num:
        live_remain = live_remaining(live_remain)
        return "Too high"

def try_1_more():
    try_again = input("Want to try again? (y/n): ")
    if try_again == "y":
        clear()
        game_play()

    else:
        print("Bai bai")
        clear()


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

def game_play():
    game_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    live_total(game_level)

    live_remain = live_total(game_level)

    correct_num = random.randint(1,101)
    # print(correct_num)

    while live_remain != 0:
        print(f"You have {live_remain} attempts remaining to guess the number.")
        player_guess = int(input("Make a guess: "))
        live_remain= live_remaining(live_remain)
        result = game_gtn(player_guess, live_remain, correct_num)
        print(result)

    print("You lose")
    print(f"The correct num is: {correct_num}")
    try_1_more()

game_play()