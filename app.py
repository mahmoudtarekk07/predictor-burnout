import streamlit as st
import pickle
import pandas as pd

# Load the model
with open("decision_tree_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🎓 Student Burnout Risk Predictor")

# Input fields
weekly_genai = st.slider("Weekly GenAI Hours", 0, 40, 5)
ai_dependency = st.slider("Perceived AI Dependency", 1, 10, 3)
anxiety = st.slider("Anxiety Level During Exams", 1, 10, 3)
traditional_hours = st.slider("Traditional Study Hours", 1, 35, 10)
pre_gpa = st.slider("Pre Semester GPA", 1.0, 4.0, 3.0)
post_gpa = st.slider("Post Semester GPA", 1.0, 4.0, 3.0)
skill_retention = st.slider("Skill Retention Score", 10, 100, 75)
paid = st.selectbox("Paid Subscription", [0, 1])
gpa_change = post_gpa - pre_gpa

# Predict
if st.button("Predict Burnout Risk"):
    input_data = pd.DataFrame([[
        weekly_genai, ai_dependency, anxiety,
        traditional_hours, pre_gpa, post_gpa,
        skill_retention, paid, gpa_change
    ]], columns=model.feature_names_in_)

    prediction = model.predict(input_data)[0]
    labels = {0: "🟢 Low", 1: "🟡 Medium", 2: "🔴 High"}
    st.success(f"Burnout Risk Level: {labels[prediction]}")
