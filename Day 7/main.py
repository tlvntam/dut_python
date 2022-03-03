import random
from replit import clear

word_list = ["conga", "logan", "mango"]
chosen_word = random.choice(word_list)

word_blank = []
for blank in range(0, len(chosen_word)):
     word_blank += "_"
print(f"{word_blank} \n")

end_game = False
live_reduce = 3

while not end_game:
    player_guess = input("Let's guess a letter !!! ").lower()
    clear()
    if player_guess in player_answer:
        print(f"You already guess {player_guess}")

    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == player_guess:
            word_blank[i] = letter

    if player_guess not in chosen_word:
        print(f"{player_guess} not in the word")
        live_reduce -= 1
        print(f"You have {live_reduce} life left !!! \n")
    print(f"{word_blank} \n")
\

    if live_reduce == 0:
        print("You lose")
        break

    if "_" not in word_blank:
        end_game = True
        print("You win")

