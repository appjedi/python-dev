txt = "2024-10-11 10:15:30"

dt = txt.split(" ")
date = dt[0].split("-")
hours = dt[1].split(":")
year = int(date[0])
print(date)
print(hours)
print (year)