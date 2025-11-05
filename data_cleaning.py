import pandas as pd

# Load dataset
df = pd.read_csv('ev_charging_data.csv')

# Preview
print("Initial Shape:", df.shape)
print(df.head())

# --- Missing Values ---
print("\nMissing values per column:\n", df.isna().sum())

# Drop rows missing key fields
df = df.dropna(subset=['StartTime', 'EnergyConsumption', 'ChargingDuration'])

# Fill numeric missing with median
num_cols = ['ChargingDuration', 'EnergyConsumption']
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

# Convert datetime
df['StartTime'] = pd.to_datetime(df['StartTime'], errors='coerce')

# Remove rows with invalid dates
df = df.dropna(subset=['StartTime'])

# Feature engineering
df['Hour'] = df['StartTime'].dt.hour
df['Day'] = df['StartTime'].dt.day_name()

# Remove duplicates
df = df.drop_duplicates()

print("\nFinal Shape:", df.shape)

# Save cleaned data
df.to_csv('ev_charging_data_cleaned.csv', index=False)
print("Cleaned dataset saved as ev_charging_data_cleaned.csv")
