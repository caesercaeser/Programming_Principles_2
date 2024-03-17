import datetime as dt

x = dt.datetime.now()
print(x)#full date with seconds
print("Year:", x.year)
print("Month:", x.month)
print("Day:", x.day)
print("Hour:", x.hour)
print("Minute:", x.minute)
print("Second:", x.second)


print(x.strftime("%A"))#Weekday, full
print(x.strftime("%a"))#Weekday, short
print(x.strftime("%d"))#Day of month
print(x.strftime("%B"))#Month, full
print(x.strftime("%b"))#Month, short
print(x.strftime("%m"))#Month, as number
print(x.strftime("%Y"))#Year, full
print(x.strftime("%H"))#Hour(00-23)
print(x.strftime("%p"))#AM/PM
print(x.strftime("%T"))#Seconds
print(x.strftime("%j"))#day number of year(365)
print(x.strftime("%x"))#local version of date(mm/dd/yy)
print(x.strftime("%X"))#local version of time


x = dt.datetime(2020, 5, 7) #yy/mm/dd
print(x)

current_date = dt.date.today()#getting only the current date


