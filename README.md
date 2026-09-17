🛡️ LoanGuard AI

AI-Powered Loan Default Risk Prediction

LoanGuard AI is a machine learning application that predicts the probability of loan default based on applicant and loan characteristics.

The project uses historical Lending Club loan data to identify patterns associated with loan defaults and presents the prediction through an interactive Streamlit dashboard.

🎯 Project Objective

The goal of LoanGuard AI is to demonstrate how machine learning can be used to analyze lending data and estimate loan default risk.

The application allows users to enter applicant information and receive:

* Estimated probability of default
* Risk classification
* Risk score visualization
* AI-generated risk explanations
* Applicant summary
* Business insights from the training dataset

📊 Dataset

The model was trained using Lending Club loan data.

The analysis included:

* Loan amount
* Loan term
* Interest rate
* Loan grade
* Employment length
* Home ownership
* Annual income
* Verification status
* Loan purpose
* Debt-to-income ratio

The target variable represents whether a loan was classified as a bad loan based on the project’s default-status definition.

🔎 Exploratory Data Analysis

Key observations from the analysis included:

* Grade A loans had an observed default rate of approximately 6%.
* Grade G loans had an observed default rate of approximately 47%.
* Higher debt-to-income ratios were associated with higher observed default rates.
* Small-business loans recorded the highest observed default rate among the analyzed loan purposes.
* Mortgage borrowers had lower observed default rates than renters in the training data.

🤖 Machine Learning

Several classification models were evaluated during development, including:

* Logistic Regression
* Random Forest
* XGBoost

The final LoanGuard application uses the trained classification pipeline saved as loan_model.pkl.

The pipeline includes preprocessing components such as:

* Feature scaling
* One-hot encoding
* Column transformation
* Logistic Regression classification

🖥️ Application

LoanGuard AI was built with:

* Python
* Pandas
* Scikit-learn
* Joblib
* Streamlit

Users can enter applicant information through the web interface and receive an estimated default probability.

📈 Example Prediction

For an example applicant with:

* Loan Amount: $10,000
* Loan Term: 36 months
* Interest Rate: 12%
* Loan Grade: A
* Annual Income: $50,000
* Home Ownership: RENT
* Debt-to-Income Ratio: 18%

LoanGuard produced an estimated default probability of 31.4% in the application.

⚠️ Disclaimer

LoanGuard AI is an educational machine learning project. Predictions are based on historical Lending Club data and should not be used as actual lending, credit, or financial decisions.

👩🏽‍💻 Author

Esther Nekesa

Data & AI Professional | Data Analytics | Data Science | Machine Learning

GitHub: github.com/enekesa582-create