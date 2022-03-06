# import random
# card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#
# def play_BJ():
#     want_play = input("Want to try BJ type 'y' or 'n':\n ")
#     if want_play == "y":
#         black_jack()
#         play_BJ()
#     else:
#         print("Thử để ghiền .,.")
#         play_BJ()
#
# def black_jack():
#     player_card = {"p_card_1": random.choice(card_list), "p_card_2": random.choice(card_list)}
#     player_card_1 = player_card["p_card_1"]
#     player_card_2 = player_card["p_card_2"]
#     player_total = player_card_1 + player_card_2
#     print(f"Your cards: [{player_card_1}, {player_card_2}]. Current score: {player_total}")
#     if player_total == 21:
#         print("You win Black Jack")
#         play_BJ()
#     bot_card = {"b_card_1": random.choice(card_list)}
#     bot_card_1 = bot_card["b_card_1"]
#     bot_total = bot_card_1
#     print(f"Bot cards: [{bot_card_1}]. Current score: {bot_total}")
#     con = True
#     while con:
#         player_more = input("Type 'y' to get another card, type 'n' to pass:\n")
#
#         bot_card["b_card_2"] = random.choice(card_list)
#         bot_card_2 = bot_card["b_card_2"]
#         bot_total += bot_card_2
#         if player_more == "y":
#             player_card["p_card_3"] = random.choice(card_list)
#             player_card_3 = player_card["p_card_3"]
#             player_total += player_card_3
#             print(f"Your cards: [{player_card_1}, {player_card_2}, {player_card_3}]. Current score: {player_total}")
#             if player_total > 21 and 11 in player_card_1:
#                 player_card_1 = 1
#                 player_total = player_card_1 + player_card_2 + player_card_3
#                 continue
#             elif player_total > 21 and 11 in player_card_2:
#                 player_card_2 = 1
#                 player_total = player_card_1 + player_card_2 + player_card_3
#                 continue
#             elif player_total > 21 and 11 in player_card_3:
#                 player_card_3 = 1
#                 player_total = player_card_1 + player_card_2 + player_card_3
#                 continue
#             elif player_total > 21:
#                 print("You bust - You lose")
#                 play_BJ()
#         else:
#             if player_total < 16:
#                 print("You lose")
#                 play_BJ()
#             con = False
#             print(f"Your cards: [{player_card_1}, {player_card_2}]. Current score: {player_total}")
#             print(f"Bot cards: [{bot_card_1}, {bot_card_2}]. Current score: {bot_total}")
#
#     if bot_total < 17:
#         bot_card["b_card_3"] = random.choice(card_list)
#         bot_card_3 = bot_card["b_card_3"]
#         bot_total += bot_card_3
#         print(f"Bot cards: [{bot_card_1}, {bot_card_2}, {bot_card_3}]. Current score: {bot_total}")
#         if bot_total < 17:
#             bot_card["b_card_4"] = random.choice(card_list)
#             bot_card_4 = bot_card["b_card_4"]
#             bot_total += bot_card_4
#             print(f"Bot cards: [{bot_card_1}, {bot_card_2}, {bot_card_3}, {bot_card_4}]. Current score: {bot_total}")
#             if bot_total < 17:
#                 bot_card["b_card_5"] = random.choice(card_list)
#                 bot_card_5 = bot_card["b_card_5"]
#                 bot_total += bot_card_5
#                 print(f"Bot cards: [{bot_card_1}, {bot_card_2}, {bot_card_3}, {bot_card_4}, {bot_card_5}]. Current score: {bot_total}")
#                 if bot_total < 17:
#                     print("Ngũ linh - Bot win")
#
#     def check_win(player_total, bot_total):
#         if player_total > bot_total:
#             print("You win")
#         elif player_total == bot_total:
#             print("We draw")
#         elif bot_total > 21:
#             print("Bot bust - You win")
#         elif bot_total > player_total:
#             print("You lose")
#
#     check_win(player_total, bot_total)
#
# play_BJ()

import random
from replit import clear

def play_BJ():
    want_play = input("Want to try BJ type 'y' or 'n':\n ")
    if want_play == "y":
        clear()
        play_game()
        play_BJ()
    else:
        print("Thử để ghiền .,.")
        play_BJ()

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score, user_cards, computer_cards):
    if len(user_cards) == 5 and user_score < 21:
        if len(computer_cards) == 5 and computer_socre < user_score:
            print("NguLinh nhỏ hơn - Computer win")
        else:
            print("Ngu Linh - You win")
    elif len(computer_cards) == 5 and computer_socre < 21:
        if len(user_cards) == 5 and user_score < computer_socre:
           print("NguLinh nhỏ hơn - You win")
        else:
            print("Ngu Linh - You lose")

    if user_score == computer_score:
        print("Draw")
    elif computer_score == 0:
        return "Lose, Computer has BlackJack"
    elif user_score == 0:
        return "Win with a BlackJack"
    elif user_score > 21:
        return "You Bust - You lose"
    elif computer_score > 21:
        return "Computer Bust - You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass:\n")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f" Your final hand: {user_cards}, final score: {user_score}")
    print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score, user_cards, computer_cards))

play_BJ()