import datetime

data = datetime.datetime.now()
print(str(data.day) + "/" + str(data.month) + "/" + str(data.year))

print(data.strftime("%d/%m/%y"))