import datetime
n = datetime.date.today()
kun = datetime.timedelta(days = 1)
print ("today: " , n)

print("yesterday: " , n - kun)

print("tomorow: " , n +kun)