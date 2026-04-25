import pandas as pd

df = pd.read_csv("dataset.csv")

filtered_data = df[(df["salary"] > 50000) & (df["department"] == "AI")]

print(filtered_data)