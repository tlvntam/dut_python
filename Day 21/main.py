"""Inheritance"""
# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#
#     def breathe(self):
#         print("Inhale, exhale")
#
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#
#     def breathe(self):
#         super().breathe()
#         print("doing in the underwater")
#
#     def swim(self):
#         print("moving in water")
#
#
# nemo = Fish()
# nemo.breathe()

"""Slicing"""
import string
alphabet = string.ascii_letters
print(alphabet[2:5])
print(alphabet[::2])
print(alphabet[::-1])