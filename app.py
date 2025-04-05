from flask import Flask, render_template, request
import pickle
import random

app = Flask(__name__)

# Load data
data = pickle.load(open('df.pkl', 'rb'))
customers = data["customers"]
products = data["products"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    customer_id = request.form['customer_id'].strip()
    
    if customer_id not in customers['customer_id'].values:
        return render_template('index.html', error="❌ Customer ID not found!")

    # Recommend 3 random products
    recommended = random.sample(list(products['product_name']), 3)
    return render_template('index.html', recommendations=recommended)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
