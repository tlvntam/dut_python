import random
import string
import art
from replit import clear

print(art.game_logo)


def check_answer(player_choice, compare_a_value, compare_b_value):
    if compare_a_value > compare_b_value:
        if player_choice == "A":
            return True
        else:
            return False
    elif compare_a_value < compare_b_value:
        if player_choice == "B":
            return True
        else:
            return False

def score(current_score):
    current_score += 1
    return current_score

def try_again():
    new_game = input("Do you want to try again? (Y/N) \n ")
    if new_game == "Y":
        clear()
        game_h_l()
    else:
        print("Bai bai")

def game_h_l():
    current_score = 0
    game_con = True
    while game_con:
        a_list = {}
        b_list = {}

        for i in range(0, 1):
            a_list[random.choice(string.ascii_lowercase)] = random.randrange(0, 1001, 2)
            b_list[random.choice(string.ascii_lowercase)] = random.randrange(1, 1002, 2)

        # print(a_list)
        compare_a = random.choice(list(a_list))
        compare_a_value = a_list[compare_a]
        print(compare_a)
        print(compare_a_value)

        print(art.vs_logo)

        # print(b_list)
        compare_b = random.choice(list(b_list))
        compare_b_value = b_list[compare_b]
        print(compare_b)
        print(compare_b_value)

        player_choice = input("Which one bigger? Type 'A'/'B': \n")

        game_answer = check_answer(player_choice, compare_a_value, compare_b_value)
        if game_answer:
            current_score += 1
            print(f"You're right!. Current score: {current_score} ")
        else:
            game_con = False
            print(f"Sorry, that's wrong. Final score: {current_score}")
            try_again()

game_h_l()




