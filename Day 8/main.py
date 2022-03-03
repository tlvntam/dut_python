# import string
#
# def encode():
#     en_mess = input("Type ur mess: ")
#     len_en_mess = len(en_mess)
#     en_mess_list = list(en_mess)
#     de_en_mess = ""
#     letter_array = list(string.ascii_lowercase)
#     the_same = set(en_mess_list) & set(letter_array)
#     print(the_same)
#     # print(f"encode mess ban nè: {en_mess}")
#     # try_again()
#
# def decode():
#     de_mess = [input("Type ur mess: ")]
#     print(f"decode mess ban nè: {de_mess}")
#     try_again()
#
# def shift_number():
#     shift_num = int(input("Type the shift num: "))
#     letter_array = string.ascii_lowercase
#     letter_array_shift_num = ""
#     for n in range(0, shift_num):
#         letter_array_shift_num += letter_array
#     print(letter_array_shift_num)
#
# def try_again():
#     try_more = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")
#     if try_more == "yes":
#         let_start()
#     else:
#         print("Bai bai")
#
# def let_start():
#     choice = input("Type 'encode' or 'decode': ")
#     if choice == "encode":
#         shift_number()
#         encode()
#     elif choice == "decode":
#         shift_number()
#         decode()
#
# let_start()

# def greet():
#     print("Hi")
#     print("How are you?")
# greet()

# def greet_with_name(name):
#     print(f"Hi {name}")
#     print(f"How are you, {name} ?")
#
# greet_with_name("Angela")

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What's it like in {location}")
#
# greet_with(name= "Tam", location= "DaNang")

# def paint_calc(height, width, cover):
#     num_of_cans = (test_h * test_w) / coverage
#     print(f"Number of cans: {round(num_of_cans)}")
#
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height= test_h, width= test_w, cover= coverage)

# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print(f"{number} is a prime number")
#     else:
#         print(f"{number} is not a prime number")
#
# n = int(input("Check this number: "))
# prime_checker(number= n)

import string

def encrypt(en_mess, shift_num):
    de_en_mess = ""
    for letter in en_mess:
        position = alphabet_shift_num.index(letter)
        new_positon = position + shift_num
        new_letter = alphabet_shift_num[new_positon]
        de_en_mess += new_letter
    print(f"Your encode text is {de_en_mess}")

def decrypt(de_mess, shift_num):
    en_de_mess = ""
    for letter in de_mess:
        position = alphabet_shift_num.index(letter)
        new_positon = position - shift_num
        new_letter = alphabet_shift_num[new_positon]
        en_de_mess += new_letter
    print(f"Your encode text is {en_de_mess}")

def caesar(start_text, shift_num, direction):
    end_text = ""
    if direction == "decode":
        shift_num *= -1
    for char in start_text:
        if char in alphabet_shift_num:
            position = alphabet_shift_num.index(char)
            new_positon = position + shift_num
            end_text += alphabet_shift_num[new_positon]
        else:
            end_text += char
    print(f"Your {direction} text is {end_text}")

con = True
while con:
    alphabet = string.ascii_lowercase

    direct = input("Type 'encode' or 'decode':\n ").lower()
    text = input("Type ur mess:\n ")
    shift = int(input("Type the shift num:\n "))

    alphabet_shift_num = ""
    for n in range(0, shift):
        alphabet_shift_num += alphabet
    alphabet_shift_num = list(alphabet_shift_num)

    shift = shift % 26
    caesar(start_text= text, shift_num= shift, direction= direct)

    try_more = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")
    if try_more == "no":
        con = False
        print("Bai bai")



