import pandas as pd

df = pd.read_csv("dwarf_stars.csv")
print(df.columns)
df=df.dropna()
print(df.dtypes)
df["Radius"] = 0.102763*df["Radius"]
df["Mass"]=df["Mass"].apply(lambda x: x.replace("$","").replace(",","")).astype("float")
df["Mass"] = 0.000954588*df["Mass"]

df.to_csv("stars_converted.csv")