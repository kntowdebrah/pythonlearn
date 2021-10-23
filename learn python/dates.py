import datetime

x = datetime.datetime.now()

print(x)
print(x.year)
print(x.strftime("%A"))


# creating a date object
x = datetime.datetime(2021, 10, 21)

print(x)
print(x.strftime("%B"))
