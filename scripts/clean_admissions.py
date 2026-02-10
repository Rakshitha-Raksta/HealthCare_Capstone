import pandas as pd

# Load admissions
df = pd.read_csv("data/raw/mimic-iv-3.1/hosp/admissions.csv.gz")

# Select required columns
df = df[[
    "hadm_id",
    "subject_id",
    "admittime",
    "dischtime",
    "insurance"
]]

# Save cleaned file
df.to_csv("data/processed/admissions_clean.csv", index=False)

print("admissions_clean.csv created")
