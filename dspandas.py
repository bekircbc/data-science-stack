import pandas as pd

df = pd.read_csv("./data/astronauts.csv", delimiter=",")

# print(df)

# print(df.head())

# print(len(df))

# for name in df["Name"]:
#   print(name)
  
# entry = df.iloc(0)
# print(type(entry))

# print(df.iloc[-5:])

# for row in df.iterrows():
#   pos,d =row
#   print(pos)
#   print(d)
#   # print(row)
#   # print(type(row))
#   break

# for pos, d in df.iterrows():
#   print(["Name"])
  
# print(df[df["Year"]<1990])

df2 = df.sort_values("Name",ascending=False)

for name in df2["Name"]:
  print(name)