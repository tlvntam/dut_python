import random

card_list = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

# def black_jack():


player_card = {"p_card_1": random.choice(card_list), "p_card_2": random.choice(card_list)}
player_card_1 = player_card["p_card_1"]
player_card_2 = player_card["p_card_2"]
print(f"Your cards: [{player_card_1}, {player_card_2}]")

bot_card = {"b_card_1": random.choice(card_list), "b_card_2": random.choice(card_list)}
bot_card_1 = bot_card["b_card_1"]
bot_card_2 = bot_card["b_card_2"]
print(f"Bot cards: [{bot_card_1}, {bot_card_2}]")


# def play_BJ():
#     want_play = input("Want to try BJ type 'y' or 'n': ")
#     if want_play == "y":
#         black_jack()
#         play_BJ()
#     else:
#         print("Thử để ghiền .,.")
#         play_BJ()
#
# play_BJ()