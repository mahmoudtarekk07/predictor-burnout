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
use_case = st.selectbox("Primary Use Case", ["Copywriting/Drafting", "Debugging/Troubleshooting", "Direct_Answer_Generation", "Ideation", "Summarizing_Reading"])
prompt_skill = st.selectbox("Prompt Engineering Skill", ["Beginner", "Intermediate", "Advanced"])

if st.button("Predict Burnout Risk"):
    data = {
        'Pre_Semester_GPA': pre_gpa,
        'Weekly_GenAI_Hours': weekly_genai,
        'Tool_Diversity': tool_diversity,
        'Paid_Subscription': paid,
        'Traditional_Study_Hours': traditional_hours,
        'Perceived_AI_Dependency': ai_dependency,
        'Anxiety_Level_During_Exams': anxiety,
        'Post_Semester_GPA': post_gpa,
        'Skill_Retention_Score': skill_retention,
        'Year_of_Study_Enc': ["Freshman","Sophomore","Junior","Senior","Graduate"].index(year),
        'Prompt_Engineering_Skill_Enc': ["Beginner","Intermediate","Advanced"].index(prompt_skill),
        'Burnout_Risk_Level_Enc': 0,
        'Paid_Subscription_Int': int(paid),
        'Major_Category_Arts': int(major == "Arts"),
        'Major_Category_Business': int(major == "Business"),
        'Major_Category_Humanities': int(major == "Humanities"),
        'Major_Category_Medical': int(major == "Medical"),
        'Major_Category_STEM': int(major == "STEM"),
        'Institutional_Policy_Actively_Encouraged': int(policy == "Actively_Encouraged"),
        'Institutional_Policy_Allowed_With_Citation': int(policy == "Allowed_With_Citation"),
        'Institutional_Policy_Strict_Ban': int(policy == "Strict_Ban"),
        'Year_of_Study_Freshman': int(year == "Freshman"),
        'Year_of_Study_Graduate': int(year == "Graduate"),
        'Year_of_Study_Junior': int(year == "Junior"),
        'Year_of_Study_Senior': int(year == "Senior"),
        'Year_of_Study_Sophomore': int(year == "Sophomore"),
        'Primary_Use_Case_Copywriting/Drafting': int(use_case == "Copywriting/Drafting"),
        'Primary_Use_Case_Debugging/Troubleshooting': int(use_case == "Debugging/Troubleshooting"),
        'Primary_Use_Case_Direct_Answer_Generation': int(use_case == "Direct_Answer_Generation"),
        'Primary_Use_Case_Ideation': int(use_case == "Ideation"),
        'Primary_Use_Case_Summarizing_Reading': int(use_case == "Summarizing_Reading"),
        'Prompt_Engineering_Skill_Advanced': int(prompt_skill == "Advanced"),
        'Prompt_Engineering_Skill_Beginner': int(prompt_skill == "Beginner"),
        'Prompt_Engineering_Skill_Intermediate': int(prompt_skill == "Intermediate"),
    }

    input_df = pd.DataFrame([data])
    prediction = model.predict(input_df)[0]
    labels = {"Low": "🟢 Low", "Medium": "🟡 Medium", "High": "🔴 High"}
    st.success(f"Burnout Risk Level: {labels[prediction]}")
