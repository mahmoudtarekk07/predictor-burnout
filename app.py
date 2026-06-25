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

# Predict
if st.button("Predict Burnout Risk"):
    input_data = pd.DataFrame([[
        weekly_genai, ai_dependency, anxiety,
        traditional_hours, pre_gpa, post_gpa, skill_retention
    ]], columns=[
        "Weekly_GenAI_Hours", "Perceived_AI_Dependency",
        "Anxiety_Level_During_Exams", "Traditional_Study_Hours",
        "Pre_Semester_GPA", "Post_Semester_GPA", "Skill_Retention_Score"
    ])

    prediction = model.predict(input_data)[0]
    labels = {0: "🟢 Low", 1: "🟡 Medium", 2: "🔴 High"}
    st.success(f"Burnout Risk Level: {labels[prediction]}")