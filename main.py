import datetime
from dateutil.relativedelta import relativedelta

start = datetime.datetime(year=2022, month=6, day=15)

now = datetime.datetime.now()

month=0

while now > start + relativedelta(months=1):
    start = start + relativedelta(months=1)
    month += 1

dt = now - start

print("{} month {} day".format(month, str(dt.days)))
