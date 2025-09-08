import datetime
today = datetime.datetime.today()
todays = datetime.date(today.year, today.month , today.day)
print("today Is : ",today.year, today.month, today.day)
if today.day > 25 and today.month == 12:
    year1 = today.year +1
    Months_till_christmas = datetime.date(year= year1, month=12, day=25)
    time_left = Months_till_christmas - todays
else:
    months_till_christmas = datetime.date(year = today.year, month=12, day=25)
    time_left = months_till_christmas - todays
print("Christmas is in: ",time_left)
months = int(input("What month where you born "))
if today.month < months:
    days = int(input("What day where you born "))
    time_till_birthday = datetime.date(year = today.year, month=months, day=days)
    time_left = time_till_birthday - todays 
    print(time_left.days)
else:
    if months == today.month:
        days = int(input("What day where you born "))
        if days < today.day:
            year2 = today.year+1
            time_till_birthday = datetime.date(year = year2, month=months, day=days)
        else:
            time_till_birthday = datetime.date(year = today.year, month=months, day=days)
    else:
        days = int(input("What day where you born "))
        year2 = today.year+1
        time_till_birthday = datetime.date(year = year2, month=months, day=days)
if today.month == months and today.day == days:
    print("Happy birthday!!")
else:
    birthday = time_till_birthday - todays
    print(birthday)