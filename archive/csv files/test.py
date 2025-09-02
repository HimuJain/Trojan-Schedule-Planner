import pandas as pd

# Load your CSV
df = pd.read_csv("schedules20231.csv")

# Group by SCT_ID and check for variations
mask = (
    df.groupby("SCT_ID")
    .filter(lambda g: g[["SCH_STARTTIME", "SCH_STARTTIME"]].drop_duplicates().shape[0] > 1)
)

# Optional: sort for clarity
mask = mask.sort_values("SCT_ID")

print(mask)
