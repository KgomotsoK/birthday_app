
from datetime import datetime
from datetime import timedelta

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

year = eval(input("Enter your birth year: "))
month = eval(input("Enter your birth month: "))
day = eval(input("Enter your birth day: "))

bday = datetime(year, month, day)
old = datetime.today().year - bday.year

for x in range(0, old+5):
    print("In ", bday.year, ", Your birthday is on: ", days[bday.weekday()])
    if x%4 == 2:
        bday = bday + timedelta(days=366)
        print("this is a leap year")
    else:
        bday = bday + timedelta(days=365)