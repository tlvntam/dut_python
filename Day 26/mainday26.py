"""new_list = [new_item for item in list if test]"""
# num_list = [1, 2, 3]
# new_num_list = [n+1 for n in num_list]
# print(new_num_list)

# name = "Tam"
# letter_list = [letter for letter in name]
# print(letter_list)

# new_list = [num*2 for num in range(1,5)]
# print(new_list)

# names = ["tam", "thu", "nha", "thang"]
# short_names = [name.upper() for name in names if len(name) > 4]
# print(short_names)


# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_number = [num*num for num in numbers]
# print(squared_number)
# result = [num for num in numbers if num % 2 == 0]
# print(result)

"""new_dict = {new_key: new_value for (key:value) in dictionary.item() if test"""

# import random
#
# names = ["tam", "thu", "nha", "tien"]
# student_score = {student:random.randint(1, 100) for student in names}
# print(student_score)
# # pass_student = {student for student in score if score[student] > 70}
# pass_student = {student:score for (student, score) in student_score.items() if score >=60}
# print(pass_student)

# sentence = "What is the Airspeed"
# sentence_list = sentence.split()
# result = {word:len(word) for word in sentence_list}
#
# print(result)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14
# }
#
# weather_f = {day:(temp * 9/5 +32) for (day, temp) in weather_c.items()}
# print(weather_f)

student_dict = {
    "student": ["tam", "thu", "nha", "tien"],
    "score": [56, 76, 98, 86]
}

"""Loop dict"""
# for (key,value) in student_dict.items():
#     print(key)

# import pandas as pd
#
# student_df = pd.DataFrame(student_dict)
# print(student_df)

