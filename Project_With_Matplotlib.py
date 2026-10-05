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
# plt.close()
plt.show()