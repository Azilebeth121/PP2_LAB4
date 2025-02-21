from datetime import datetime,timedelta

today = datetime.today()
BOTW = datetime(2017,3,3)
tomorow = today + timedelta(days = 1)
yesterday = today - timedelta(days = 1)
differ = abs(today.timestamp() - BOTW.timestamp())
print(f"Today: {today}")
print(f"Yesterday: {yesterday}")
print(f"Tomorow: {tomorow}")
print(f"Microseconds: {today.microsecond}")
print(f"In second Today And BOTW diff: {differ}")