import random
import smtplib
import datetime as dt
import pandas as pd

"""Read CSV"""
data = pd.read_csv("birthdays.csv")
data_dict = data.to_dict()
"""CVS -> DF"""
birth_df = pd.DataFrame(data_dict)
# print(birth_df)

current_time = dt.datetime.now()
current_month = current_time.month
current_day = current_time.day

# print(current_month,current_day)
"""Check row by row in DF"""
for index, row in birth_df.iterrows():
    if birth_df.loc[index, "month"] == current_month and birth_df.loc[index, "day"] == current_day:
        # print(birth_df.loc[index, "email"])
        birth_email = birth_df.loc[index, "email"]
        # print(birth_email)
        my_email = "tlvntamc2.pbchau@gmail.com"
        my_password = "nhantam47"

        # with open("letter_templates/letter_1.txt") as letter_1:
        #     letter_1_content = letter_1.read()
        # with open("letter_templates/letter_2.txt") as letter_2:
        #     letter_2_content = letter_2.read()
        # with open("letter_templates/letter_3.txt") as letter_3:
        #     letter_3_content = letter_3.read()
        # print(letter_1_content)
        # letters = [letter_1_content, letter_2_content, letter_3_content]
        # birth_letter = random.choice(letters).replace(PLACEHOLDER, birth_df.loc[index, "name"])

        file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(file_path) as letter:
            letter_content = letter.read()
        PLACEHOLDER = "[NAME]"
        birth_letter = letter_content.replace(PLACEHOLDER, birth_df.loc[index, "name"])
        # print(birth_letter)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=f"{birth_email}",
                                msg=f"Subject:HPBD\n\n {birth_letter}"
                                )


