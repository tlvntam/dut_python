# with open("weather_data.csv") as we_data:
#     day_data = we_data.readlines()
#     print(day_data)

# import csv

# with open("weather_data.csv") as we_data:
#     day_data = csv.reader(we_data)
#     temperature = []
#     for row in day_data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas as pd

# data = pd.read_csv("weather_data.csv")
# print(type(data))
# print(data["day"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()

# avg_temp = sum(temp_list)/len(temp_list)
# print(round(avg_temp, 2))

# print(data["temp"].mean())
# print(data["temp"].max())

"""Get data in column"""
# print(data.condition)

"""Get data in row"""
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

"""Create DF from scratch"""
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# d_f = pd.DataFrame(data_dict)
# # print(d_f)
# d_f.to_csv("new_data.csv")

# d_f = pd.read_csv("Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# d_f_fur_color = d_f["Primary Fur Color"]
# print(d_f_fur_color)
# gray_count = 0
# cinnamon_count = 0
# black_count = 0
# for color in d_f_fur_color:
#     if color == "Gray":
#         gray_count += 1
#     elif color == "Cinnamon":
#         cinnamon_count += 1
#     elif color == "Black":
#         black_count += 1
#
# print(gray_count, cinnamon_count, black_count)
#
# d_f_dict = {
#     "Fur Color": ["grey", "red", "black"],
#     "Count": [gray_count, cinnamon_count, black_count]
# }
# d_f_result = pd.DataFrame(d_f_dict)
# d_f_result.to_csv("squirrel_count.csv")

# d_f = pd.read_csv("Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrel = len(d_f[d_f["Primary Fur Color"] == "Gray"])
# red_squirrel = len(d_f[d_f["Primary Fur Color"] == "Cinnamon"])
# black_squirrel = len(d_f[d_f["Primary Fur Color"] == "Black"])

