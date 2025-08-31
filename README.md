# 🏡 House Price Prediction App  

[![Streamlit](https://img.shields.io/badge/Deploy-Streamlit-brightgreen?logo=streamlit)](https://house-price-prediction-dzypzeofxzpdrl7wtp8ies.streamlit.app/)  

A simple and interactive **Machine Learning web app** built with **Streamlit** to predict house prices based on:  
- **Overall Quality (1–10)**  
- **Above Ground Living Area (sqft)**  

The app uses a **Linear Regression model** trained on the famous **Ames Housing Dataset**.  

---

## 🚀 Live Demo
👉 [Click here to try the app](https://house-price-prediction-dzypzeofxzpdrl7wtp8ies.streamlit.app/)  

---

## ⚙️ Features
- 🎛 User-friendly sliders & inputs for house features  
- 💰 Instant house price prediction  
- 📊 Clean UI with a modern design  
- 🌐 Deployed online using Streamlit Cloud  

---

## 📂 Project Structure
```
├── app.py                # Streamlit app
├── train_model.py        # Script to train and save model
├── house_price_model.pkl # Saved trained model
├── train.csv             # Dataset (Ames Housing)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 🛠️ Tech Stack
- **Python 3.9+**  
- **Streamlit** (Web App Framework)  
- **Scikit-learn** (Machine Learning)  
- **Pandas & NumPy** (Data handling)  

---

## 🖥️ Installation & Usage (Run Locally)

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/house-price-prediction.git
   cd house-price-prediction
   ```

2. Create virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

5. The app will open in your browser at:
   ```
   http://localhost:8501
   ```

---

## 📊 Model Training
To retrain the model:
```bash
python train_model.py
```
This will generate a new `house_price_model.pkl`.

---

## 👩‍💻 Author
**Tamanna Bhrigunath**  
📧 bhrigunathtamanna@gmail.com  
🔗 [GitHub](https://github.com/bhrigu136) | [LinkedIn](https://linkedin.com/in/tamanna-bhrigunath-578b43190)  

---

✨ If you like this project, give it a ⭐ on GitHub!  
