import pickle
import pandas as pd

# Load the pickle file
with open("df.pkl", "rb") as f:
    df = pickle.load(f)

print("✅ Type of object:", type(df))
print("✅ Shape:", df.shape)
print("✅ Columns:", df.columns.tolist())
print("\n🔹 First 5 rows:")
print(df.head())
