import pandas as pd
df = pd.read_csv("digital_behaviour.csv")
print(df.head())
print(df.shape)
print(list(df.columns))
print(df[["Instagram_Minutes", "Study_Minutes"]].describe())
one_column  = df["Instagram_Minutes"]
two_columns = df[["Date", "Instagram_Minutes"]]
df["Instagram_Minutes"].sum()
round(df["Study_Minutes"].mean(), 2)
df["YouTube_Minutes"].max()
heavy_insta = df[df["Instagram_Minutes"] > 100]
good_study  = df[df["Study_Minutes"] > 180]
danger_days = df[
    (df["Instagram_Minutes"] > 100) & (df["Study_Minutes"] < 100)
]
top_insta = df.sort_values("Instagram_Minutes", ascending=False).head(5)
df["Total_Screen_Time"] = (
    df["Instagram_Minutes"]
    + df["YouTube_Minutes"]
    + df["WhatsApp_Minutes"]
    + df["LinkedIn_Minutes"]
)
df["Screen_Hours"] = (df["Total_Screen_Time"] / 60).round(2)
df["Digital_Balance"] = (df["Study_Minutes"] / df["Total_Screen_Time"]).round(2)
df["Day_Type"] = "Normal"
df.loc[df["Total_Screen_Time"] > 300, "Day_Type"] = "Heavy"
print(df["Day_Type"].value_counts())
app_totals = {
    "Instagram": df["Instagram_Minutes"].sum(),
    "YouTube": df["YouTube_Minutes"].sum(),
    "WhatsApp": df["WhatsApp_Minutes"].sum(),
    "LinkedIn": df["LinkedIn_Minutes"].sum(),
}
biggest_app = max(app_totals, key=app_totals.get)
worst_day = df.loc[df["Total_Screen_Time"].idxmax()]
for app, mins in app_totals.items():
    print(f"  {app:<10} {mins:>6} min  ({round(mins/60,1)} hrs)")
df.to_csv("my_analysis.csv", index=False)