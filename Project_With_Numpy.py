import numpy as np
import csv
                        #""" SUPER CALCULATOR ->NUMPY"""
APP1="Instagram"
APP2="Study"
insta_minutes = []
study_minutes=[]
with open("digital_behaviour.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        insta_minutes.append(int(row[f"{APP1}_Minutes"]))
        study_minutes.append(int(row[f"{APP2}_Minutes"]))
insta_minutes=insta_minutes[24:31]
study_minutes=study_minutes[24:31]
instagram=np.array(insta_minutes)
study=np.array(study_minutes)
print("Instagram ",instagram," Study ",study)
#total=np.sum(instagram)
insta_total=instagram.sum()
insta_average=instagram.mean()
insta_maximum=instagram.max()
insta_days=len(instagram)

print(instagram[0],instagram[-1],instagram[2])
print(instagram[:3])
print(instagram[0::2],instagram[-2:],instagram[1:4])
insta_hours=instagram/60

study_total=study.sum()
study_average=study.mean()
study_maximum=study.max()
study_days=len(study)

print(study[0],study[-1],study[2])
print(study[:3])
print(study[0::2],study[-2:],study[1:4])
study_hours=study/60
study_hours=study_hours.round(2)
print(study_hours)
diff=study-instagram
print(diff)
'''greater=[val for val in difference if val>100] #list comprehension #in python trick
 regular way
 for val in difference:
   if val>100:
      greater.append(val)'''
 
boolean=instagram>100 #in numpy
print(boolean)

#python_filtering=[bool_ for bool_ in boolean if bool_]
#python_filtering=filter(lambda bool_: bool_,boolean)
# in numpy
greater=instagram[instagram>100] #boolean indexing
"""count=(instagram>100)
count=count.sum()
count=(instagram>100).sum() #operator chaining"""
count=greater.sum()
above_avg=instagram[instagram>insta_average]




