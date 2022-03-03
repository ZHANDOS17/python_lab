import datetime

y, m, d, h, min, s = map(int, input().split())
data1 =  datetime.datetime(y, m, d, h, min, s)

y, m, d, h, min, s = map(int, input().split())
data2 =  datetime.datetime(y, m, d, h, min, s)

s = (data1 - data2).total_seconds()
print(s)
