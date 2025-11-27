# Corey Schafer - Python Tutorial: Datetime module
import datetime
import pytz

# date
d = datetime.date(2026, 8, 1)
today = datetime.date.today()

print(d)
print(datetime.date.today())
print(datetime.date.today().day)
print(datetime.date.today().year)

print(datetime.date.today().weekday) # Monday 0 Sunday 6
print(datetime.date.today().isoweekday) # Monday 1 Sunday 7

# Time Deltas
time_delta = datetime.timedelta(days=7)

print(today + time_delta)
print(today - time_delta)

# date2 = date1 + time_delta
# time_delta = date1 + date2


bday = datetime.date(2026, 1, 8)
till_bday = bday - today

print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds())

# Time

time = datetime.time(9, 30, 45, 100000)

print(time)
print(time.hour)
print(time.minute)

# datetime
date_time = datetime.datetime(2025, 12, 31, 23, 59, 0, 100000)

print(date_time)
print(date_time+time_delta)

# .today
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()
dt_utcnow = datetime.datetime.now(datetime.timezone.utc)

print(dt_today)
print(dt_now)
print(dt_utcnow)

# timezones


# Alwyas use UTC to diminish the misuse of timezones
dt_tz = datetime.datetime(2026, 1, 8, 12, 0, 0, tzinfo=pytz.UTC)
dt_utc_tz = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
dt_now_tz = datetime.datetime.now(tz=pytz.utc) # This is more preferred

print(dt_tz)
print(dt_now_tz)
print(dt_utc_tz)

# for tz in pytz.all_timezones:
#     print(tz)

dt_my_tz_from_utc = dt_now_tz.astimezone(pytz.timezone('Asia/Dhaka'))
print(dt_my_tz_from_utc)

dt_local = datetime.datetime.now() # This is a naive/local datetime, a timezone unware date time

print(dt_local) 

# How to localize a naive datetime
my_tz = pytz.timezone('Asia/Dhaka')

dt_local_tz = my_tz.localize(dt_local)

"""
How to display datetime in different formats
"""
dt_mt = datetime.datetime.now(tz=pytz.timezone('Asia/Dhaka'))

print(dt_mt.isoformat())

#strftime - Formats the datetime (Notice the f)
print(dt_mt.strftime('%B %d, %Y'))

dt_str = 'November 23, 2025'

#strptime - Parses the datetime (Notice the p)
convert_string_to_dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')

print(convert_string_to_dt)

# ArjanCodes - A Deep Dive Into Date And Time In Python

import time

# These returns the time passed since Jan 1st, 1970
print(time.time())
print(time.time_ns())

# 2038 Problem a similar one like 1970 to 2000 as 
# most unix based systems store time in 32 bit 
# which limits the time value retention.

some_date = datetime.datetime(2022, 10, 9, 18, 0, 0)
print(some_date)

# From iso string to actual datetime object
some_date_2 = datetime.datetime.fromisoformat('2025-11-23 15:42:58.666958')
print(some_date_2)

# Timezone Datetime

utc = pytz.timezone('UTC')
loc = utc.localize(some_date)

print(loc)

sydney = pytz.timezone("Australia/Sydney")
print(loc.astimezone(sydney))


import pendulum
