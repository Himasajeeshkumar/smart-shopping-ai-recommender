import pandas as pd
import pickle

# Load the files
customers = pd.read_csv("customer_data_collection.csv")
products = pd.read_csv("product_recommendation_data.csv")

# We’ll just store both in a dictionary for easy access
data = {
    "customers": customers,
    "products": products
}

# Save as a pickle
with open("df.pkl", "wb") as f:
    pickle.dump(data, f)

print("✅ Pickle file created as df.pkl")
