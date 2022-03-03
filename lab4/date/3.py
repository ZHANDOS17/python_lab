import datetime
y, m, d, h, min, s, ms = map(int, input().split())
n = datetime.datetime(y, m, d, h, min, s, ms).replace(microsecond = 0)
print(n)