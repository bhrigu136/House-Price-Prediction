import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

# --- Page Setup ---
st.set_page_config(page_title="House Price Prediction", page_icon="🏠", layout="centered")

# --- Custom Styling ---
st.markdown("""
    <style>
    body {
        background-color: #0f172a;
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }
    .main {
        background-color: #0f172a;
    }
    h1 {
        color: #38bdf8;
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    .stSlider label, .stNumberInput label {
        font-size: 1.1rem;
        font-weight: 600;
        color: #f8fafc;
    }
    .stButton>button {
        background: linear-gradient(90deg, #2563eb, #38bdf8);
        color: white;
        border-radius: 12px;
        padding: 0.6rem 1.2rem;
        font-weight: bold;
        font-size: 1rem;
        transition: 0.3s;
        border: none;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(90deg, #1e40af, #0ea5e9);
    }
    .prediction-box {
        background: #22c55e;
        color: white;
        padding: 1rem;
        border-radius: 12px;
        font-size: 1.4rem;
        text-align: center;
        margin-top: 20px;
        font-weight: bold;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.title("ℹ️ About the App")
st.sidebar.markdown("""
This **House Price Prediction App** uses a **Linear Regression model**.

You can input the **Overall Quality** and **Living Area (sqft)**, and the app will predict the house price 💰.

---

### 📊 Model Details:
- Algorithm: **Linear Regression**
- Features used:  
  - `OverallQual` (1–10 quality rating)  
  - `GrLivArea` (Above Ground Living Area in sqft)

---

""")

# --- Title ---
st.title("🏡 House Price Prediction")
st.subheader("📊 Enter House Features")

# --- Inputs ---
feature1 = st.slider("Overall Quality (1–10)", min_value=1, max_value=10, value=5)
feature2 = st.number_input("Above Ground Living Area (in sqft)", min_value=300, max_value=5000, value=1500)

# --- Prediction Button ---
if st.button("Predict Price"):
    input_data = np.array([[feature1, feature2]])
    prediction = model.predict(input_data)

    if prediction[0] < 0:
        st.warning("⚠️ Predicted price is negative. Try using more realistic values.")
    else:
        st.markdown(
            f"<div class='prediction-box'>💰 Predicted House Price: ${prediction[0]:,.2f}</div>",
            unsafe_allow_html=True
        )
