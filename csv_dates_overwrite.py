import pandas as pd
from datetime import datetime as dt

def reindex_date(s: str):
    return dt.strftime(dt.strptime(s, "%m-%Y"), '%Y-%m-%d') 

df = pd.read_csv("monthly-cloud-observability-costs.csv")
df["month"] = df["month"].apply(reindex_date)
print(df)
write_path = "monthly_cost_re-dated.csv"
print(f"writing to file `{write_path}` ...")
df.to_csv(write_path, index=False)
print("done.")
