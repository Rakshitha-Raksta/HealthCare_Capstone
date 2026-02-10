import pandas as pd

diag = pd.read_csv("data/raw/mimic-iv-3.1/hosp/diagnoses_icd.csv.gz")
drg = pd.read_csv("data/raw/mimic-iv-3.1/hosp/drgcodes.csv.gz")

# Keep minimal useful columns
diag = diag[["hadm_id", "icd_code"]]
drg = drg[["hadm_id", "drg_type", "drg_severity"]]

# Merge
billing = pd.merge(diag, drg, on="hadm_id", how="left")

billing.to_csv("data/processed/billing_clean.csv", index=False)

print("billing_clean.csv created")
