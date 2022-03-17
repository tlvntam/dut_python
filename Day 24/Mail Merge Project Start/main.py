PLACEHOLDER = "[name]"

with open("../Mail Merge Project Start/Input/Names/invited_names.txt", mode="r") as data_in:
    names = data_in.readlines()
    print(names)

with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_in:
    letter_content = letter_in.read()
    for name in names:
        strpped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, strpped_name)
        with open(f"../Mail Merge Project Start/Output/ReadyToSend/letter_for_{strpped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
