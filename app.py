from flask import Flask, render_template, request
import pickle
import os
import pandas as pd

app = Flask(__name__)

# Load the pickled data
with open("df.pkl", "rb") as f:
    data = pickle.load(f)

customers = data["customers"]
products = data["products"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    customer_id = request.form["customer_id"]
    if customer_id in customers["CustomerID"].values:
        recommended = products["Product"].sample(5).tolist()
        return render_template("index.html", recommendations=recommended)
    else:
        error = "❌ Customer ID not found!"
        return render_template("index.html", error=error)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Use Render's assigned port
    app.run(host="0.0.0.0", port=port)
