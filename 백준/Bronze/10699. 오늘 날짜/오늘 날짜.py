import datetime
res = datetime.datetime.now() + datetime.timedelta(hours=9)
print(res.strftime("%Y-%m-%d"))