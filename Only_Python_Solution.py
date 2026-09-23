import csv

APP = "Instagram"
minutes = []
with open("digital_behaviour.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        minutes.append(int(row[f"{APP}_Minutes"]))
minutes=minutes[24:31]
print(minutes)
total=sum(minutes)
average=total//len(minutes)
highest=max(minutes)
lowest=min(minutes)
c=0
for i in minutes:
    if i>average:
        c+=1
print(f"APP_NAME: {APP} \nTotal_Minutes_Spent: {total}\n Average_Minutes_Spent: {average}\n Highest_Time: {highest} ")