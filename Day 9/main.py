# programing_dictionary = {"Bug": "An error in a program",
#                          "Function": "A piece of code"}
#
# print(programing_dictionary["Bug"])
# empty_dictionary = {}
# programing_dictionary["Loop"] = "The action of doing something over & over again"
# print(empty_dictionary)

# print("Welcome")
# bid_list = {}
# con = True
# while con:
#     player_name = input("Enter your name: ")
#     player_bet = int(input("Enter your bet: $"))
#     bid_list[player_name] = player_bet
#     max = 0
#     for i in bid_list:
#         if max < bid_list[i]:
#            max = bid_list[i]
#            winner_name = i
#
#     player = input("Anyone else ?\n")
#     if player == "no":
#         con = False
#         print(f"The winner is {winner_name} with a bid of ${max}.")

# student_score = {
#     "Harry": 81,
#     "Ron": 78,
#     "Herione": 99,
#     "Drace": 74,
#     "Neville": 62,}

# student_grade ={}
# for i in student_score:
#     if 91 <= student_score[i] <= 100:
#         student_grade[i] ="Outstanding"
#     elif 81 <= student_score[i] <= 90:
#         student_grade[i] = "Exceeds Expectations"
#     elif 71 <= student_score[i] <= 80:
#         student_grade[i] = "Acceptable"
#     elif student_score[i] <= 70:
#         student_grade[i] = "Fail"
# print(student_grade)

# capitals = {
#     "France": "Paris",
#     "VietNam": "HaNoi"
# }

# travel_log = [
#     {
#         "country": "VietNam",
#         "cities": ["HaNoi", "DaNang", "DaLat"],
#         "visits": 5
#     },
#     {
#         "country": "France",
#         "cities": ["Paris", "Lille", "Dijon"],
#         "visits": 12
#     },
# ]

# def add_new_country(country, cities, visits):
#     new_coutry = {}
#     new_coutry["country"] = country
#     new_coutry["cities"] = cities
#     new_coutry["visits"] = visits
#     travel_log.append(new_coutry)
#
# add_new_country("Russia", ["Moscow", "Saint Peterburg"], 2)
# print(travel_log)

# country = input("Enter your new country: ")
# cities = input("Enter your cities visited: ")
# visits = int(input("How many times you have visited in total? "))

# from replit import clear
#
# def find_max(bid_list):
#     max = 0
#     winner_name = ""
#     for i in bid_list:
#         if max < bid_list[i]:
#             max = bid_list[i]
#             winner_name = i
#     print(f"The winner is {winner_name} with a bid of ${max}.")
#
# print("Welcome")
# bid_list = {}
# con = True
# while con:
#     player_name = input("Enter your name: ")
#     player_bet = int(input("Enter your bet: $"))
#     bid_list[player_name] = player_bet
#
#     player = input("Anyone else ?\n")
#     if player == "no":
#         con = False
#         find_max(bid_list)
#     else:
#         clear()
