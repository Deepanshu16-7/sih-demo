import streamlit as st

# Title
st.title("AI-Based Student Dropout Prediction & Counselling System")

# Step 1: Input student data
st.header("Enter Student Details")
attendance = st.number_input("Attendance %", min_value=0, max_value=100, value=75)
marks = st.number_input("Average Marks %", min_value=0, max_value=100, value=70)
family_income = st.number_input("Family Income (per month, ₹)", min_value=0, value=20000)
stress_level = st.slider("Stress Level (1=Low, 5=High)", 1, 5, 2)

# Step 2: Simple AI logic (rule-based for demo)
risk_score = 0

if attendance < 60:
    risk_score += 2
if marks < 50:
    risk_score += 2
if family_income < 10000:
    risk_score += 1
if stress_level >= 4:
    risk_score += 2

# Decide risk level
if risk_score >= 5:
    risk_level = "High Risk"
    advice = "Immediate counselling required. Provide financial aid & stress management."
elif 3 <= risk_score < 5:
    risk_level = "Medium Risk"
    advice = "Provide mentoring & regular monitoring."
else:
    risk_level = "Low Risk"
    advice = "Normal support & motivation."

# Step 3: Show prediction
st.subheader("Prediction Result")
st.write(f"*Risk Level:* {risk_level}")
st.write(f"*Counselling Advice:* {advice}")

# Step 4: Mock parent/teacher alert
if risk_level == "High Risk":
    st.warning("⚠ Alert: Student at HIGH RISK. Send SMS/Email to parents & teachers.")
elif risk_level == "Medium Risk":
    st.info("ℹ Alert: Student at MEDIUM RISK. Keep monitoring.")
else:
    st.success("✅ Student is at LOW RISK. No urgent action required.")

# Step 5: Dashboard mock
st.header("System Dashboard (Example)")
st.bar_chart({"Low Risk": [15], "Medium Risk": [7], "High Risk": [3]})
