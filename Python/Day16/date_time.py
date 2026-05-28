'''Function	Direction
strftime()	datetime → string
strptime()	string → datetime
💡 Simple memory trick
f = format
p = parse

So:

strftime → make readable string
strptime → read/parse string'''


# Day 16 - Date and Time

from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

# Current date and time
now = datetime.now()

print(now)

# Current year, month, day
print(now.year)
print(now.month)
print(now.day)

# Current hour, minute, second
print(now.hour)
print(now.minute)
print(now.second)

# Current date only
today = date.today()

print(today)

# Create custom date
new_date = date(2026, 5, 28)

print(new_date)

# Create custom time
new_time = time(10, 30, 45)

print(new_time)

# Formatting date
formatted = now.strftime("%d/%m/%Y")

print(formatted)

# Formatting time
formatted_time = now.strftime("%H:%M:%S")

print(formatted_time)

# Full formatting
print(now.strftime("%A"))
print(now.strftime("%B"))
print(now.strftime("%Y"))

# Convert string to datetime
date_string = "28 May 2026"

converted = datetime.strptime(date_string, "%d %B %Y")

print(converted)

# Timedelta
current = datetime.now()

future = current + timedelta(days=7)

print(future)

past = current - timedelta(days=5)

print(past)

# Difference between dates
date1 = datetime(2026, 5, 1)
date2 = datetime(2026, 5, 28)

difference = date2 - date1

print(difference.days)

# Timestamp
print(now.timestamp())

# Date difference from user input
date1 = input("Enter first date (dd-mm-yyyy): ")
date2 = input("Enter second date (dd-mm-yyyy): ")

d1 = datetime.strptime(date1, "%d-%m-%Y")
d2 = datetime.strptime(date2, "%d-%m-%Y")

difference = d2 - d1

print("Days difference:", difference.days)

# Age calculator
birth_year = int(input("Enter birth year: "))

current_year = datetime.now().year

age = current_year - birth_year

print("Your age is:", age)

# Countdown example
future_date = datetime(2026, 12, 31)

today = datetime.now()

remaining = future_date - today

print("Days remaining:", remaining.days)

# Current weekday
today = datetime.now()

print(today.strftime("%A"))

# Current month name
print(today.strftime("%B"))

# Current time only
current_time = datetime.now().time()

print(current_time)

# Formatting nicely
now = datetime.now()

formatted = now.strftime("%d-%m-%Y %H:%M:%S")

print(formatted)

"""

📌 Date format symbols
Code	Meaning	Example
%d	day number	28
%m	month number	05
%Y	full year	2026
%y	short year	26
%B	full month name	May
%b	short month name	May
%A	full weekday	Thursday
%a	short weekday	Thu
📌 Time format symbols
Code	Meaning	Example
%H	hour (24hr)	14
%I	hour (12hr)	02
%M	minute	30
%S	second	45
%p	AM/PM	PM
"""