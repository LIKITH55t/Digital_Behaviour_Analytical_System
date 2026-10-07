import pandas as pd
import matplotlib
# matplotlib.use("Agg")
import matplotlib.pyplot as plt
df=pd.read_csv("digital_behaviour.csv")
df["Total_time"]=df["Instagram_Minutes"]+df["WhatsApp_Minutes"]+df["YouTube_Minutes"]
df["Day_Label"]=[f"{i+1}"  for i in range(30)]
plt.figure(figsize=(12,6))
plt.bar(df["Day_Label"],df["Total_time"])
plt.title("my screen time")
plt.xlabel("day")
plt.ylabel("time")
plt.xticks(rotation=45)
plt.savefig("map.png")
plt.close()
plt.show()
#chart2
app_names=["Instagram","WhatsApp","Youtube"];
app_times=[df["Instagram_Minutes"].sum(),df["WhatsApp_Minutes"].sum(),df["YouTube_Minutes"].sum()]
plt.figure(figsize=(12,6))
plt.bar(app_names,app_times)
plt.title("Total Time by App")
plt.xlabel("Apps")
plt.ylabel("time")
plt.xticks(rotation=45)
plt.savefig("chart_2.png")
plt.close()
plt.show()
#chart3
plt.figure(figsize=(12,6))
plt.plot(df["Day_Label"],df["Study_Minutes"],marker='o',label='study_min_per_day',color='b')
plt.plot(df["Day_Label"],df["Total_time"],marker='o',label='tot_time_per_day',color='g')
legend=plt.legend()
plt.title("Line chart")
plt.xlabel("Apps")
plt.ylabel("time")
plt.xticks(rotation=45)
plt.savefig("chart_3.png")
plt.close()
plt.show()
#chart 4
plt.figure(figsize=(12,6))
plt.pie(app_times,labels=app_names,autopct='%1.1f%%',startangle=90)
plt.title("Pie Chart")
plt.xticks(rotation=45)
plt.savefig("chart_4.png")
plt.close()
plt.show()
