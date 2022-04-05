import smtplib
import datetime as dt
import random

# current_time = dt.datetime.now()
# current_date = current_time.weekday()
# print(current_date+2)

# day_of_birth = dt.datetime(year=2022, month=7, day=4)
# print(day_of_birth)

with open("quotes.txt", mode="r") as quote:
    quote_list = quote.read().splitlines()

quote_msg = random.choice(quote_list)

my_email = "tlvnhantam47@gmail.com"
my_password = "04072000"

"""Check thứ 4 / Current day [0] = Thứ 2"""
# if current_date+2 == 4:
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="kieuhuynhhavy2000@gmail.com",
                        msg=f"Subject:Hello\n\n {quote_msg}"
                        )
    print(quote_msg)



