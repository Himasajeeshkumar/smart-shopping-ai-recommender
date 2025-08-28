from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the preprocessed DataFrame
df = pickle.load(open("df.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    customer_id = request.form["customer_id"].strip()
    
    if customer_id in df["Customer_ID"].values:
        recommended_product = df[df["Customer_ID"] == customer_id]["Recommended_Product"].values[0]
        return render_template("index.html", recommendations=[recommended_product])
    else:
        return render_template("index.html", error="Customer ID not found. Please try again.")

if __name__ == "__main__":
    # important: host=0.0.0.0 for deployment (like Render, Heroku, etc.)
    app.run(debug=False, host="0.0.0.0", port=10000)
