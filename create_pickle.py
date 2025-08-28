import pandas as pd
import pickle

# Load customers
customers = pd.read_csv("customer_data_collection.csv")

# Load products
products = pd.read_csv("product_recommendation_data.csv")

# Debug: Show columns
print("Product file columns:", products.columns)

# Choose one column as recommendation (example: Subcategory)
if "Subcategory" in products.columns:
    product_choices = products["Subcategory"].dropna().tolist()
else:
    product_choices = products["Product_ID"].dropna().tolist()

# Repeat products randomly for each customer
recommended_products = pd.Series(product_choices).sample(n=len(customers), replace=True).reset_index(drop=True)

# Combine
df = pd.DataFrame({
    "Customer_ID": customers["Customer_ID"].values,
    "Recommended_Product": recommended_products
})

# Save as pickle
with open("df.pkl", "wb") as f:
    pickle.dump(df, f)

print("✅ df.pkl created successfully with shape:", df.shape)
print(df.head())
