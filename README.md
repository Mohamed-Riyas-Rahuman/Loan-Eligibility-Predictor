# Loan Default Prediction Web App

A Flask-based web application that predicts a person's **Credit Score** and determines whether they are **eligible for a loan** based on provided details.

# Features
- Web form for user input
- Predicts **Credit Score** using a trained Machine Learning model
- Displays **Loan Eligibility** as "Yes" or "No"
- Simple and user-friendly

# Tech Stack
- **Backend:** Flask (Python)
- **Machine Learning:** Scikit-learn
- **Data Handling:** Pandas, Numpy
- **Model Storage:** Joblib
- **Frontend:** HTML, CSS

# Project Structure
LoanDefaultWebApp/
│
├── app.py # Main Flask app
├── pipeline.pkl # Trained ML model
├── requirements.txt # Dependencies
├── templates/
│ └── index.html # Frontend HTML
└── README.md # Project documentation
# Prediction & Eligibility
- **Credit Score Output:** A numeric value
- **Eligibility Rule:**  
  - Credit Score ≥ 700 → Eligible  
  - Credit Score < 700 →  Not Eligible

# How to Run Locally
1. **Clone the repository**
```bash
git clone https://github.com/YourUsername/LoanDefaultWebApp.git
cd LoanDefaultWebApp
Install dependencies

2.Install dependencies
pip install -r requirements.txt

3.Run the flask app
python app.py

4.Open in browser
http://127.0.0.1:5000


