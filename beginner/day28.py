from datetime import date, datetime, timedelta

from datetime import date

today = date.today()

print(today)

date_and_time = datetime.now()
print(date_and_time)

d = date(2024, 1, 15)

print(d)

today = date.today()

formatted = today.strftime('%d/%m/%Y')

print(formatted)

d1 = date(2024, 1, 1)
d2 = date(2024, 2, 10)

difference = d2 - d1

print(difference.days)

today = date.today()

future = today + timedelta(days=30)

print(future)

from datetime import date

birth_date = date(2005, 12, 9)

today = date.today()

age = today.year - birth_date.year

# Check if birthday has occurred this year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

print("Age:", age)