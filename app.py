from flask import Flask, render_template, request
import joblib
import pandas as pd
print("app.py has started running")  # Runs as soon as the script starts
app = Flask(__name__) 

# Load the trained pipeline
print("Loading pipeline model from 'pipeline.pkl'...")
pipeline = joblib.load('pipeline.pkl')
print("Pipeline loaded successfully!")
@app.route('/')
def home():
    print("Home page accessed")
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    try:
        print("\n--- New Prediction Request ---")
        input_data = []
        user_input = {}

        # Loop through 15 features
        for i in range(1, 16):
            value = request.form.get(f'feature{i}')
            print(f"Received Feature {i}: {value}")
            user_input[f'feature{i}'] = value
            if not value:
                raise ValueError(f"Feature {i} is missing")
            input_data.append(value)

        # Define column names (must match training)
        columns = [
            'Age', 'Income', 'LoanAmount', 'MonthsEmployed', 'NumCreditLines',
            'InterestRate', 'LoanTerm', 'DTIRatio',
            'Education', 'EmploymentType', 'MaritalStatus',
            'HasMortgage', 'HasDependents', 'LoanPurpose', 'HasCoSigner'
        ]

        # Create DataFrame from input
        final_input_df = pd.DataFrame([input_data], columns=columns)
        print("Formatted Input DataFrame:")
        print(final_input_df)

        # Predict credit score
        credit_score = pipeline.predict(final_input_df)[0]
        credit_score_rounded = round(credit_score, 2)
        print(f"Predicted Credit Score: {credit_score_rounded}")

        # Determine loan eligibility
        eligibility = "Yes" if credit_score_rounded >= 700 else "No"
        print(f"Eligibility for Loan: {eligibility}")
        return render_template(
            'index.html',
            prediction_text=f'Predicted Credit Score: {credit_score_rounded}',
            eligibility_text=f'Eligible for Loan: {eligibility}',
            user_input=user_input
        )
    except Exception as e:
        print(f"Error during prediction: {e}")
        return render_template('index.html', prediction_text=f'Error: {e}')
if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True)
