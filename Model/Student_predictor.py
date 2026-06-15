import joblib
model = joblib.load("student_score_model.pkl")
print("model loaded successfully")

hours_studied = float(input("Hours Studied(In a week): "))
attendance = int(input("Attendance: "))

Parental_Involvement = int(input("Parental_Involvement (low=0, medium = 1 ,high = 2)) :  "))

Access_to_Resources = int(input("Access_to_Resources (low=0, medium = 1 ,high = 2)): "))

Sleep_Hours = float(input("Sleep_Hours :  "))

Previous_Scores= int(input("Previous_Scores(max is 100): "))

Motivation_Level = int(input("Motivation_Level(low=0, medium = 1 ,high = 2) :  "))

Tutoring_Sessions = int(input("Tutoring_Sessions: "))

Family_Income = int(input("Family_Income(low=0, medium = 1 ,high = 2) :  "))

Teacher_Quality = int(input("Teacher_Quality(low=0, medium = 1 ,high = 2): "))

Peer_Influence = int(input("Peer_Influence (Negative=0, Neutral = 1 ,positive = 2):  "))


Physical_Activity = int(input("Physical_Activity(average_hours_in_a_week) :  "))

Parental_Education_Level = int(input("Parental_Education_Level (High school=0, college = 1 ,postgraduate = 2) : "))

Distance_from_Home = int(input("Distance_from_Home (Near=0, moderate = 1 ,far = 2):  "))

Female= int(input("Female (yes =1 , no = 0): "))

Male = int(input("Male (yes =1 , no = 0):  "))

School_Type_Private= int(input("School_Type_Private (yes =1 , no = 0): "))

School_Type_Public = int(input("School_Type_Public (yes =1 , no = 0) :  "))

Internet_Access_No= int(input("Internet_Access_No (yes =1 , no = 0): "))

Internet_Access_Yes = int(input("Internet_Access_Yes (yes =1 , no = 0):  "))

Extracurricular_Activities_No= int(input("Extracurricular_Activities_No (yes =1 , no = 0): "))

Extracurricular_Activities_Yes = int(input("Extracurricular_Activities_Yes (yes =1 , no = 0):  "))

Learning_Disabilities_No = int(input("Learning_Disabilities_No (yes =1 , no = 0): "))

Learning_Disabilities_Yes = int(input("Learning_Disabilities_Yes (yes =1 , no = 0): "))

print("-----------Student_Detail-----------\n")
print("Hours_studied :  ",hours_studied)
print("Attendence:  ", attendance)
print("parental_involment: ",Parental_Involvement)
print("access_to_resources: ", Access_to_Resources)
print("Sleep_hours: ", Sleep_Hours)
print("previous_score: ",Previous_Scores)
print("Motivation_level: ",Motivation_Level)
print("Tutoring_sessions: ", Tutoring_Sessions)
print("Family_Income", Family_Income)
print("Teacher_Quality",Teacher_Quality)
print("Peer_Influence",Peer_Influence)
print("physical_Activity",Physical_Activity)
print("parental_Education_Level",Parental_Education_Level)
print("Distance_from_Home",Distance_from_Home)
print("is female(1 =yes , 0 = no)",Female)
print("is male (yes =1 , no = 0)", Male)
print("Is_private(yes =1 , no = 0)",School_Type_Private)
print("Is_publec(yes =1 , no = 0)",School_Type_Public)
print("is_Internet_access(yes =1 , no = 0)",Internet_Access_No)
print("Is_Extracurricular_Activities(yes =1 , no = 0)",Extracurricular_Activities_No)
print("Learning_ability(yes =1 , no = 0)",Learning_Disabilities_No)




print("------------End_Here-------------\n")

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
    Learning_Disabilities_Yes
]]

predicted_score = model.predict(new_student)
print("---------Predicted_Score-----------\n")

print("Predicted Score =", predicted_score[0])


print("---------Run_successfully------------")
    