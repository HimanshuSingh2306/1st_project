import streamlit as st
import joblib

st.title("Student Performance Prediction")

try:
    model = joblib.load("Model/student_score_model.pkl")
    st.success("Model Loaded Successfully")
except Exception as e:
    st.error(f"Error Loading Model: {e}")
    
hours_studied = st.number_input(
  "Hours Studied(Average of Study Hours in a Week)",
  min_value=0.0,
  max_value=90.0
)
attendance = st.number_input(
  "Attendance",
  min_value=0,
  max_value=100
)
study_efficiency = (hours_studied*attendance)
Parental_Involvement = st.selectbox("Parental Involment",["low","Medium","High"])
if Parental_Involvement == "low":
  Parental_Involvement = 0
elif Parental_Involvement == "Medium":
  Parental_Involvement=1
else:
 Parental_Involvement = 2
    

Access_to_Resources = st.selectbox(
  "Access_to_Resources",["low","Medium","High"]
)
if Access_to_Resources == "low":
  Access_to_Resources = 0
elif Access_to_Resources == "Medium":
  Access_to_Resources=1
else:
 Access_to_Resources = 2
 
Sleep_Hours = st.number_input(
  "Sleep_Hours(In a day)",
  min_value=0,
  max_value=24
)
Previous_Scores = st.number_input(
  "Previous_Scores( max = 100 )",
  min_value= 0,
  max_value= 100
)


Motivation_Level = st.selectbox(
  "Motivation_Level",
 ["low","Medium","High"]
)
if Motivation_Level == "low":
  Motivation_Level = 0
elif Motivation_Level == "Medium":
  Motivation_Level=1
else:
 Motivation_Level = 2
 
 
Family_Income = st.selectbox(
  "Family_Income",["low","Medium","High"]
)
if Family_Income == "low":
  Family_Income = 0
elif Family_Income == "Medium":
  Family_Income=1
else:
 Family_Income = 2
 
 
 
Tutoring_Sessions = st.number_input(
  "Tutoring_Sessions",
  min_value=0,
  max_value=100
)



Teacher_Quality = st.selectbox(
  "Teacher_Quality",["low","Medium","High"])
if Teacher_Quality == "low":
  Teacher_Quality = 0
elif Teacher_Quality == "Medium":
  Teacher_Quality=1
else:
 Teacher_Quality = 2
 
 
 

Peer_Influence = st.selectbox(
  "Peer_Influence",["low","Medium","High"]
)
if Peer_Influence == "low":
  Peer_Influence = 0
elif Peer_Influence == "Medium":
  Peer_Influence=1
else:
 Peer_Influence = 2
 
 
 
Physical_Activity = st.number_input(
  "Physical_Activity",
  min_value=0,
  max_value=50
)



Parental_Education_Level = st.selectbox(
  "Parental_Education_Level",["High School","Graduate","Postgraduate"]
)
if Parental_Education_Level == "High School":
    Parental_Education_Level = 0
elif Parental_Education_Level == "Graduate":
  Parental_Education_Level = 1
else:
  Parental_Education_Level = 2
  
  
        
Distance_from_Home = st.selectbox(
  "Distance_from_Home",["Near", "Moderate","Far"]
)
if Distance_from_Home == "Near":
  Distance_from_Home = 0
elif Distance_from_Home == "Moderate":
  Distance_from_Home = 1
else:
  Distance_from_Home = 2
  
      
gender = st.selectbox("Gender",["Male", "Female"])
if gender=="Male":
  Male = 1
  Female = 0
else:
  Male  = 0
  Female = 1  

School_Type = st.selectbox("School Type",["Private","Government"])
if School_Type == "Private":
  School_Type_Private = 1
  School_Type_Public = 0
else:   
  School_Type_Private = 0
  School_Type_Public = 1


Internet_Access = st.selectbox(
  "Internet_Access " , ["Yes", "No"]
)
if Internet_Access == "Yes":
  Internet_Access_Yes = 1
  Internet_Access_No = 0
else:
  Internet_Access_Yes = 0
  Internet_Access_No = 1
    


Extracurricular_Activities = st.selectbox(
  "Extracurricular_Activities ", ["Yes", "No"]
)
if Extracurricular_Activities == "Yes":
  Extracurricular_Activities_Yes = 1
  Extracurricular_Activities_No = 0
else:
    Extracurricular_Activities_Yes = 0
    Extracurricular_Activities_No = 1
    
    

Learning_Disabilities = st.selectbox(
  "Learning_Disabilities",["Yes", "No"])
if Learning_Disabilities == "Yes":
  Learning_Disabilities_Yes = 1
  Learning_Disabilities_No = 0
else:
   Learning_Disabilities_Yes = 0
   Learning_Disabilities_No = 1
    
 
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