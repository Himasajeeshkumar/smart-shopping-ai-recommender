# 🛍️ Smart Shopping AI Recommender

A simple content-based product recommendation system that suggests products to customers based on their **browsing history**, using a probability-ranked matching approach.

---

## 📌 Overview

This project recommends products to a customer by looking at the categories they've browsed before, and matching those categories with available products. The matches are then ranked using a **probability of recommendation** score, and the top results are shown to the user.

---

## 🧠 How It Works

```
Customer ID
     │
     ▼
Look up customer's Browsing History (list of categories)
     │
     ▼
Find products belonging to those categories
     │
     ▼
Sort by Probability_of_Recommendation (high → low)
     │
     ▼
Return Top 5 Subcategories as Recommendation
```

**Approach:** Content-based filtering — recommendations are based on matching product attributes (category) to what the customer has shown interest in, not on similarity between customers.

---

## 📂 Dataset

| File | Description |
|------|-------------|
| `customer_data_collection.csv` | Customer details including `Customer_ID` and `Browsing_History` (categories they've viewed) |
| `product_recommendation_data.csv` | Product details including `Category`, `Subcategory`, and `Probability_of_Recommendation` |

---

## ⚙️ Core Logic (`recomender.py`)

```python
def recommend_products(customer_id):
    # 1. Find the customer using Customer_ID
    # 2. Read their browsing history (list of categories)
    # 3. Filter products that belong to those categories
    # 4. Sort filtered products by recommendation probability
    # 5. Return the top 5 subcategories
```

If the `Customer_ID` doesn't exist in the dataset, the function returns a friendly `"Customer ID not found"` message instead of crashing.

---

## 📁 Project Structure

```
Smart-Shopping-AI-Recommender/
│
├── templates/                       # HTML pages for the web app
├── app.py                           # Main application (Flask web app)
├── create_pickle.py                 # Script to generate df.pkl from CSV data
├── df.pkl                           # Pre-processed data saved for fast loading
├── customer_data_collection.csv     # Customer browsing history dataset
├── product_recommendation_data.csv  # Product dataset
├── recomender.py                    # Core recommendation logic
├── view_pickle.py                   # Utility script to inspect df.pkl contents
├── requirements.txt                 # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Himasajeeshkumar/Smart-Shopping-AI-Recommender.git
cd Smart-Shopping-AI-Recommender
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Generate the pickle file (if not already present)
```bash
python create_pickle.py
```

### 4. Run the app
```bash
python app.py
```

The app should then be accessible locally in your browser (check the terminal output for the exact URL, usually `http://127.0.0.1:5000`).

> **Note:** This project currently runs locally and is not deployed online.

---

## 🛠️ Technologies Used

| Tool | Purpose |
|------|---------|
| Python 3 | Core language |
| Pandas | Data loading and processing |
| Flask | Web application framework |
| Pickle | Storing processed data for quick reuse |
| HTML (Jinja templates) | Front-end pages |

---

## ⚠️ Current Limitations

- Recommendations are based only on category matching — doesn't yet consider customer-to-customer similarity (collaborative filtering)
- Uses `eval()` to convert browsing history string to a list, which works but isn't the safest method for untrusted data
- No user authentication or personalization beyond `Customer_ID`

---

## 🎯 Future Improvements

- [ ] Add collaborative filtering to compare similar customers
- [ ] Replace `eval()` with a safer parsing method (e.g., `ast.literal_eval` or JSON)
- [ ] Add a search/filter UI for browsing all products
- [ ] Deploy the app online (e.g., Render, Railway, or PythonAnywhere)
- [ ] Add user login and personalized dashboards

---

## 👩‍💻 Author

**Hima Sajeesh Kumar**
B.Tech Computer Science Engineering (AI & ML)
GitHub: https://github.com/Himasajeeshkumar

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
