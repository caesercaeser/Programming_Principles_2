import datetime as dt
#1.Write a Python program to subtract five days from current date.
x = dt.datetime.now()
print(x -dt.timedelta(days=5))



#2.Write a Python program to print yesterday, today, tomorrow.
today = dt.date.today()
yesterday = dt.date(year = today.year, month = today.month, day= today.day - 1)
tomorrow = dt.date(year = today.year, month = today.month, day = today.day + 1)
print(yesterday)
print(today)
print(tomorrow)


#3.Write a Python program to drop microseconds from datetime.
currentdate = dt.datetime.now()
date_without_microseconds = currentdate.replace(microsecond=0)
print(date_without_microseconds)


#4.Write a Python program to calculate two date difference in seconds.
date1 = dt.datetime(2023, 5, 14, 10, 45, 0)  # Example date 1
date2 = dt.datetime(2023, 5, 15, 10, 45, 0)  # Example date 2

timedifference = abs((date2 - date1).total_seconds())
print(timedifference)


