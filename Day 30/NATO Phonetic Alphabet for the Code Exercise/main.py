import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


# try_again = True
# while try_again:
#     try:
#         word = input("Enter a word: ").upper()
#         output_list = [phonetic_dict[letter] for letter in word]
#         print(output_list)
#         try_again = False
#     except KeyError:
#         print("Sorry, only letter in alphabet pls")
def gene_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letter in alphabet pls")
        gene_phonetic()
    else:
        print(output_list)


gene_phonetic()
