# recomender.py

import pandas as pd

# Load the correct file names
customers = pd.read_csv('customer_data_collection.csv')
products = pd.read_csv('product_recommendation_data.csv')

def recommend_products(customer_id):
    # Get the customer info
    customer = customers[customers['Customer_ID'] == customer_id]
    if customer.empty:
        return ["Customer ID not found"]

    browsing = eval(customer.iloc[0]['Browsing_History'])  # Convert string to list

    # Recommend products that match browsing categories
    recommended = products[products['Category'].isin(browsing)]

    # Sort by probability of recommendation (high to low)
    recommended = recommended.sort_values(by='Probability_of_Recommendation', ascending=False)

    # Return top 5 product subcategories as recommendation
    return recommended['Subcategory'].head(5).tolist()
