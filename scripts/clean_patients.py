import pandas as pd

# Load raw patients file
df = pd.read_csv("data/raw/mimic-iv-3.1/hosp/patients.csv.gz")

# Select useful columns
df = df[["subject_id", "gender", "anchor_age", "anchor_year"]]

# Save cleaned file
df.to_csv("data/processed/patients_clean.csv", index=False)

print("patients_clean.csv created successfully")
