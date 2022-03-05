def func_add(first_num, second_num):
    result = first_num + second_num
    return result

def func_minus(first_num, second_num):
    result = first_num - second_num
    return result

def func_multi(first_num, second_num):
    result = first_num * second_num
    return result

def func_divide(first_num, second_num):
    result = first_num / second_num
    return result

operation = {
    "+": func_add,
    "-": func_minus,
    "*": func_multi,
    "/": func_divide
}
def calculator():
    first_num = float(input("What's the first num?\n"))
    for sym in operation:
        print(sym)
    con = True
    while con:
        operation_calc = input("Pick an operation:\n")
        second_num = float(input("What's the second num?\n"))

        calculation_func = operation[operation_calc]
        result_num = calculation_func(first_num, second_num)

        print(f"{first_num} {operation_calc} {second_num} = {round(result_num, 2)}")
        try_again = input(f"Type 'y' to con with {round(result_num, 2)}, or type 'n' to start a new cal: ")
        if try_again == "n":
            con = False
            print(f"The result is: {result_num}")
            calculator()
        else:
            con = True
            first_num = result_num
calculator()

# def format_name(f_name, m_name, l_name):
#     if f_name == "" or m_name == "" or l_name == "":
#         return "You didn't provide valid inputs."
#     format_f_name = f_name.title()
#     format_m_name = m_name.title()
#     format_l_name = l_name.title()
#     result = format_l_name + " " + format_m_name + " " + format_f_name
#     return result
#
# l_name = input("Enter ur last name:\n")
# m_name = input("Enter ur middle name:\n")
# f_name = input("Enter ur first name:\n")
#
# full_name = format_name(f_name, m_name, l_name)
# print(f"Ur formated full name is: {full_name}")

# def is_leap(year_check):
#     if year_check % 4 == 0:
#         if year_check % 100 == 0:
#             if year_check % 400 == 0:
#                 # print(f"So the year {year_check} is a leap year")
#                 return "Leap"
#             else:
#                 # print(f"So the year {year_check} is not a leap year")
#                 return "Not Leap"
#         else:
#             # print(f"So the year {year_check} is a leap year")
#             return "Leap"
#     else:
#         # print(f"So the year {year_check} is not a leap year")
#         return "Not Leap"
# def days_in_month(year_check, month_check):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     month_days_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year_check) == "Leap":
#         result = month_days_leap[month_check - 1]
#         return result
#     else:
#         result = month_days[month_check - 1]
#         return result
#
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#     # if is_leap(year_check) == "Leap" and month_check == 2:
#     #     return 29
#     # return month_days[month_check - 1]
#
# year_check = int(input("Enter a year: "))
# month_check = int(input("Enter a month: "))
# days = days_in_month(year_check, month_check)
# print(days)




