import pandas as pd
import pickle

# Load your original CSVs
customers = pd.read_csv("customer_data_collection.csv")  # should have CustomerID column
products = pd.read_csv("product_recommendation_data.csv")  # should have Product column

# Save them in a dictionary
data = {
    "customers": customers,
    "products": products
}

# Dump to pickle file
with open("df.pkl", "wb") as f:
    pickle.dump(data, f)
