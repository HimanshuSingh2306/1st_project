import streamlit as st
import joblib

st.title("Student Performance Prediction")

try:
    model = joblib.load("Model/student_score_model.pkl")
    st.success("Model Loaded Successfully")
except Exception as e:
    st.error(f"Error Loading Model: {e}")
    
hours_studied = st.number_input(
  "Hours Studied",
  min_value=0.0,
  max_value=50.0
)
attendance = st.number_input(
  "Attendance",
  min_value=0,
  max_value=100
)
study_efficiency = (hours_studied*attendance)
Parental_Involvement = st.number_input(
  "Parental Involment",
  min_value=0,
  max_value=2
)
Access_to_Resources = st.number_input(
  "Access_to_Resources",
  min_value=0,
  max_value=2
)
Sleep_Hours = st.number_input(
  "Sleep_Hours",
  min_value=0,
  max_value=24
)
Previous_Scores = st.number_input(
  "Previous_Scores",
  min_value= 0,
  max_value= 100
)
Motivation_Level = st.number_input(
  "Motivation_Level",
  min_value= 0,
  max_value= 2
)
Family_Income = st.number_input(
  "Family_Income(low=0, medium = 1 ,high = 2)",
  min_value=0,
  max_value=2
)
Tutoring_Sessions = st.number_input(
  "Tutoring_Sessions",
  min_value=0,
  max_value=100
)
Teacher_Quality = st.number_input(
  "Teacher_Quality",
  min_value= 0,
  max_value=2
)
Peer_Influence = st.number_input(
  "Peer_Influence",
  min_value=0,
  max_value=2
)
Physical_Activity = st.number_input(
  "Physical_Activity",
  min_value=0,
  max_value=50
)
Parental_Education_Level = st.number_input(
  "Parental_Education_Level",
  min_value=0,
  max_value=2
)
Distance_from_Home = st.number_input(
  "Distance_from_Home",
  min_value=0,
  max_value=2
)
Female = st.number_input(
  "Female (yes =1 , no = 0)",
  min_value=0,
  max_value=1
)
Male = st.number_input(
  "Male (yes =1 , no = 0):  ",
  min_value=0,
  max_value=1
)
School_Type_Private = st.number_input(
  "School_Type_Private (yes =1 , no = 0)",
  min_value=0,
  max_value=1
)
School_Type_Public = st.number_input(
  "School_Type_Public (yes =1 , no = 0) ",
  min_value=0,
  max_value=1
)
Internet_Access_No = st.number_input(
  "Internet_Access_No (yes =1 , no = 0)",
  min_value=0,
  max_value=1
)
Internet_Access_Yes = st.number_input(
  "Internet_Access_Yes (yes =1 , no = 0)",
  min_value=0,
  max_value=1
)
Extracurricular_Activities_No = st.number_input(
  "Extracurricular_Activities_No (yes =1 , no = 0)",
  min_value=0,
  max_value=1
)
Extracurricular_Activities_Yes = st.number_input(
  "Extracurricular_Activities_Yes (yes =1 , no = 0)",
  min_value=0,
  max_value=1
)
Learning_Disabilities_No = st.number_input(
  "Learning_Disabilities_No (yes =1 , no = 0)",
  min_value=0,
  max_value=1
)
Learning_Disabilities_Yes = st.number_input(
  "Learning_Disabilities_Yes (yes =1 , no = 0)",
  min_value=0,
  max_value=1
)
st.write("Hours studied: ",hours_studied)
st.write("Attendance: ",attendance)
st.write("Study_efficiency: ",study_efficiency)
st.write("Parental_Involvement: ",Parental_Involvement)
st.write("Access to resources: ", Access_to_Resources)
st.write("Sleep hours: ", Sleep_Hours)
st.write("previous score: ", Previous_Scores)
st.write("Motivation_Level",Motivation_Level)
st.write("Tutoring_Sessions",Tutoring_Sessions)
st.write("Family_Income: ",Family_Income)
st.write("Teacher_Quality: ",Teacher_Quality)
st.write("Peer_Influence: ",Peer_Influence)
st.write("Physical_Activity: ",Physical_Activity)
st.write("Parental_Education_Level: ",Parental_Education_Level)
st.write("Distance_from_Home: ", Distance_from_Home)
st.write("Female: ",Female)
st.write("Male: ", Male)
st.write("School type private: ", School_Type_Private)
st.write("school type public: ",School_Type_Public)
st.write("Internet Access no: ",Internet_Access_No)
st.write("Internet access yes: ",Internet_Access_Yes)
st.write("Extracurricular_activities_no: ", Extracurricular_Activities_No)
st.write("Extracurricular acitivities yes: ", Extracurricular_Activities_Yes)
st.write("Learning disability no : ", Learning_Disabilities_No)
st.write("learning disability yes: ", Learning_Disabilities_Yes)
st.write("study efficiency: ", study_efficiency)

predict_button = st.button("Predict Score")

if predict_button:

    new_student = [[
        hours_studied,
        attendance,
        Parental_Involvement,
        Access_to_Resources,
        Sleep_Hours,
        Previous_Scores,
        Motivation_Level,
        Tutoring_Sessions,
        Family_Income,
        Teacher_Quality,
        Peer_Influence,
        Physical_Activity,
        Parental_Education_Level,
        Distance_from_Home,
        Female,
        Male,
        School_Type_Private,
        School_Type_Public,
        Internet_Access_No,
        Internet_Access_Yes,
        Extracurricular_Activities_No,
        Extracurricular_Activities_Yes,
        Learning_Disabilities_No,
        Learning_Disabilities_Yes,
        study_efficiency
    ]]

    predicted_score = model.predict(new_student)

    st.success(
        f"Predicted Exam Score = {predicted_score[0]:.2f}"
    )