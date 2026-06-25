import streamlit as st
import pickle
import pandas as pd

with open("decision_tree_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🎓 Student Burnout Risk Predictor")

# Inputs
pre_gpa = st.slider("Pre Semester GPA", 1.0, 4.0, 3.0)
post_gpa = st.slider("Post Semester GPA", 1.0, 4.0, 3.0)
weekly_genai = st.slider("Weekly GenAI Hours", 0, 40, 5)
traditional_hours = st.slider("Traditional Study Hours", 1, 35, 10)
ai_dependency = st.slider("Perceived AI Dependency", 1, 10, 3)
anxiety = st.slider("Anxiety Level During Exams", 1, 10, 3)
skill_retention = st.slider("Skill Retention Score", 10, 100, 75)
tool_diversity = st.slider("Tool Diversity", 1, 5, 3)
paid = st.selectbox("Paid Subscription", [True, False])
year = st.selectbox("Year of Study", ["Freshman", "Sophomore", "Junior", "Senior", "Graduate"])
major = st.selectbox("Major Category", ["Arts", "Business", "Humanities", "Medical", "STEM"])
policy = st.selectbox("Institutional Policy", ["Actively_Encouraged", "Allowed_With_Citation", "Strict_Ban"])
use_case =[prediction]}")
