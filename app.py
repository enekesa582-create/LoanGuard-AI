import streamlit as st
import pandas as pd
import joblib

# ============================================
# LOANGUARD AI - VERSION 3.0
# ============================================

# Page configuration
st.set_page_config(
    page_title="LoanGuard AI",
    page_icon="🛡️",
    layout="wide"
)

# Load trained model
model = joblib.load("loan_model.pkl")

# ---------- CUSTOM STYLE ----------
st.markdown("""
<style>
.main {
    background-color: #F4F8FF;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.stButton > button {
    background-color: #0B5ED7;
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 12px;
    width: 100%;
    height: 3.2em;
}

.stButton > button:hover {
    background-color: #084298;
}

h1, h2, h3 {
    color: #0B2545;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.title("🛡️ LoanGuard AI")
st.subheader("AI-Powered Loan Default Risk Prediction")

st.info(
    "Enter an applicant's information below to estimate the probability of loan default using a machine learning model trained on Lending Club loan data."
)

st.divider()

# ============================================
# APPLICANT INFORMATION
# ============================================

st.header("📋 Applicant Information")

left, right = st.columns(2)

with left:

    loan_amnt = st.number_input(
        "💰 Loan Amount ($)",
        min_value=500,
        max_value=40000,
        value=10000,
        step=500
    )

    term = st.selectbox(
        "📅 Loan Term",
        [36, 60],
        format_func=lambda x: f"{x} Months"
    )

    int_rate = st.number_input(
        "📈 Interest Rate (%)",
        min_value=0.0,
        max_value=40.0,
        value=12.0,
        step=0.1
    )

    grade = st.selectbox(
        "⭐ Loan Grade",
        ["A", "B", "C", "D", "E", "F", "G"]
    )

    emp_length = st.selectbox(
        "💼 Employment Length",
        list(range(11)),
        format_func=lambda x: "10+ Years" if x == 10 else f"{x} Years"
    )

with right:

    home_ownership = st.selectbox(
        "🏠 Home Ownership",
        ["RENT", "MORTGAGE", "OWN", "OTHER", "ANY", "NONE"]
    )

    annual_inc = st.number_input(
        "💵 Annual Income ($)",
        min_value=0.0,
        value=50000.0,
        step=1000.0
    )

    verification_status = st.selectbox(
        "✅ Verification Status",
        ["Verified", "Source Verified", "Not Verified"]
    )

    purpose = st.selectbox(
        "📝 Loan Purpose",
        [
            "credit_card",
            "car",
            "small_business",
            "other",
            "wedding",
            "debt_consolidation",
            "home_improvement",
            "major_purchase",
            "medical",
            "moving",
            "vacation",
            "house",
            "renewable_energy",
            "educational"
        ]
    )

    dti = st.number_input(
        "📊 Debt-to-Income Ratio (%)",
        min_value=0.0,
        max_value=100.0,
        value=18.0,
        step=0.1
    )

st.divider()

# ============================================
# PREDICTION BUTTON
# ============================================

if st.button("🔮 Predict Default Risk"):

    # Create dataframe exactly as model expects
    input_data = pd.DataFrame({
        "loan_amnt": [loan_amnt],
        "term": [term],
        "int_rate": [int_rate],
        "grade": [grade],
        "emp_length": [emp_length],
        "home_ownership": [home_ownership],
        "annual_inc": [annual_inc],
        "verification_status": [verification_status],
        "purpose": [purpose],
        "dti": [dti]
    })

    # Model prediction
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    # Risk category
    if probability >= 0.80:
        risk_level = "🔴 Critical Risk"

    elif probability >= 0.60:
        risk_level = "🔴 High Risk"

    elif probability >= 0.40:
        risk_level = "🟠 Moderate Risk"

    elif probability >= 0.20:
        risk_level = "🟢 Low Risk"

    else:
        risk_level = "🟢 Very Low Risk"

    # ============================================
    # RESULTS
    # ============================================

    st.success("Prediction Completed Successfully!")

    st.header("📊 Prediction Dashboard")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Risk Level", risk_level)

    with c2:
        st.metric(
            "Probability of Default",
            f"{probability:.1%}"
        )

    with c3:
        st.metric("Loan Grade", grade)

    st.subheader("🎯 Loan Default Risk Score")

    st.progress(float(probability))

    st.write(
        f"### Estimated Default Probability: **{probability:.1%}**"
    )

    # ============================================
    # DECISION MESSAGE
    # ============================================

    st.subheader("🚦 LoanGuard Decision")

    if probability >= 0.80:
        st.error(
            "Critical Risk — This applicant has a very high estimated probability of default."
        )

    elif probability >= 0.60:
        st.error(
            "High Risk — This application may require additional review."
        )

    elif probability >= 0.40:
        st.warning(
            "Moderate Risk — This applicant has a moderate estimated probability of default."
        )

    elif probability >= 0.20:
        st.success(
            "Low Risk — This applicant appears relatively low risk."
        )

    else:
        st.success(
            "Very Low Risk — This applicant appears very low risk."
        )

    # ============================================
    # AI EXPLANATION
    # ============================================

    st.divider()
    st.subheader("🤖 AI Risk Explanation")

    reasons = []

    if grade in ["E", "F", "G"]:
        reasons.append("⭐ Lower loan grades historically had higher default rates.")

    if int_rate >= 20:
        reasons.append("📈 Higher interest rates increase repayment burden.")

    if dti >= 30:
        reasons.append("📊 Higher Debt-to-Income ratio increases repayment risk.")

    if purpose == "small_business":
        reasons.append("💼 Small business loans recorded the highest default rate in the dataset.")

    if home_ownership == "RENT":
        reasons.append("🏠 Renting showed a slightly higher default rate than mortgages.")

    if annual_inc < 50000:
        reasons.append("💵 Lower annual income may reduce repayment capacity.")

    if emp_length == 0:
        reasons.append("👤 Short employment history may increase lending risk.")

    if reasons:
        for reason in reasons:
            st.write(reason)
    else:
        st.success(
            "✅ No major high-risk indicators were detected from the entered information."
        )

    # ============================================
    # APPLICANT SUMMARY
    # ============================================

    st.divider()
    st.subheader("👤 Applicant Summary")

    s1, s2 = st.columns(2)

    with s1:
        st.write(f"**💰 Loan Amount:** ${loan_amnt:,.0f}")
        st.write(f"**📅 Loan Term:** {term} Months")
        st.write(f"**⭐ Loan Grade:** {grade}")
        st.write(f"**💼 Employment Length:** {emp_length} Years")
        st.write(f"**🏠 Home Ownership:** {home_ownership}")

    with s2:
        st.write(f"**💵 Annual Income:** ${annual_inc:,.0f}")
        st.write(f"**📈 Interest Rate:** {int_rate:.1f}%")
        st.write(f"**📊 Debt-to-Income Ratio:** {dti:.1f}%")
        st.write(f"**📝 Loan Purpose:** {purpose.replace('_',' ').title()}")
        st.write(f"**✅ Verification Status:** {verification_status}")

    # ============================================
    # BUSINESS INSIGHTS
    # ============================================

    st.divider()
    st.subheader("📈 Business Insights From LoanGuard Analysis")

    st.markdown("""
    **Key findings from the Lending Club dataset used to train LoanGuard AI**

    - ⭐ Grade **A** loans had the lowest default rate (~6%).
    - ⭐ Grade **G** loans had the highest default rate (~47%).
    - 📊 Higher Debt-to-Income ratios generally showed higher default rates.
    - 💼 Small Business loans recorded the highest default rate among loan purposes.
    - 🏠 Mortgage borrowers generally had lower default rates than renters.
    """)

    # ============================================
    # DISCLAIMER
    # ============================================

    st.divider()
    st.caption(
        "LoanGuard AI is an educational machine learning application built using Python, Scikit-learn, Pandas, and Streamlit. Predictions are based on historical Lending Club loan data and should not be used as real lending decisions."
    )