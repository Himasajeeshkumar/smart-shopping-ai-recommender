from flask import Flask, request, render_template
from recomender import recommend_products

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    customer_id = request.form['customer_id']
    recommendations = recommend_products(customer_id)
    return render_template('index.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
