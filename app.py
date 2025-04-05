from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load precomputed data
df = pickle.load(open('df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    customer_id = request.form['customer_id'].strip().lower()

    # Match customer ID in lowercase
    matched = df[df['customer_id'].str.lower() == customer_id]

    if matched.empty:
        return render_template('index.html', error="❌ Customer ID not found. Please try again.")

    index = matched.index[0]
    distances = list(enumerate(similarity[index]))
    sorted_scores = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]
    recommended_products = [df.iloc[i[0]].product_name for i in sorted_scores]

    return render_template('index.html', recommendations=recommended_products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
