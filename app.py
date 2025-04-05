from flask import Flask, render_template, request
from recomender import recommend_products
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', recommended_products=None)

@app.route('/recommend', methods=['POST'])
def recommend():
    customer_id = request.form.get('customer_id')
    if customer_id:
        recommended_products = recommend_products(customer_id)
        if recommended_products:
            return render_template('index.html', recommended_products=recommended_products, customer_id=customer_id)
        else:
            return render_template('index.html', recommended_products=[], customer_id=customer_id, message="Customer ID not found.")
    else:
        return render_template('index.html', recommended_products=[], message="Please enter a Customer ID.")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
