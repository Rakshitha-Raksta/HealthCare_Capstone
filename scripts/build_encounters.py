import pandas as pd

patients = pd.read_csv("data/processed/patients_clean.csv")
admissions = pd.read_csv("data/processed/admissions_clean.csv")
billing = pd.read_csv("data/processed/billing_clean.csv")

# Join patients + admissions
df = pd.merge(admissions, patients, on="subject_id", how="left")

# Join billing
df = pd.merge(df, billing, on="hadm_id", how="left")

df.to_csv("data/processed/encounters_master.csv", index=False)

print("encounters_master.csv created")
