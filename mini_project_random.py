import pandas as pd                    
import numpy as np                     
import matplotlib.pyplot as plt        
import seaborn as sns                  
from sklearn.model_selection import train_test_split    
from sklearn.metrics import confusion_matrix            
from sklearn.metrics import classification_report       
from sklearn.ensemble import RandomForestClassifier    
data = pd.read_csv("Stress_Prediction_Modifying.csv")
print(data.head())
data.columns=['snoring_rate', 'respiration_rate', 'body_temperature', 'limb_movement', 'blood_oxygen','eye_movement', 'sleeping_hours', 'heart_rate', 'stress_level']
print(data.head())
X = data.drop(['stress_level'], axis=1)
y = data['stress_level']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)
print("X_test shape:", X_test.shape)
print("y_test shape:", y_test.shape)

random_forest = RandomForestClassifier(n_estimators=500, random_state=1)
random_forest.fit(X_train,y_train)
print("Accuracy",random_forest.score(X_test,y_test))
y_predict = random_forest.predict(X_test)
matrix = confusion_matrix(y_test, y_predict)
print("Confusion Matrix:")
print(matrix)
report = classification_report(y_test, y_predict)
# Print the classification report
print("Classification Report:")
print(report)
import random
#Low/Normal (0)
# sr = round(random.uniform(40, 51),3)
# print("sr:",sr)
# rr = round(random.uniform(16, 19),3)
# print("rr:",rr)
# bt = round(random.uniform(96,100),3)
# print("bt:",bt)
# lm = round(random.uniform(4, 9),3)
# print("lm:",lm)
# bo = round(random.uniform(95, 98),3)
# print("bo:",bo)
# em = round(random.uniform(60, 81),3)
# print("em:",em)
# sh = round(random.uniform(7, 10),3)
# print("sh:",sh)
# hr = round(random.uniform(50, 55),3)
# print("hr:",hr)

#Medium Low (1)
sr = round(random.uniform(50, 61),3)
print("sr:",sr)
rr = round(random.uniform(18, 21),3)
print("rr:",rr)
bt = round(random.uniform(94,91),3)
print("bt:",bt)
lm = round(random.uniform(8, 11),3)
print("lm:",lm)
bo = round(random.uniform(92,96),3)
print("bo:",bo)
em = round(random.uniform(80,86),3)
print("em:",em)
sh = round(random.uniform(5,8),3)
print("sh:",sh)
hr = round(random.uniform(55, 61),3)
print("hr:",hr)
#Medium (2)
# sr = round(random.uniform(60, 81),3)
# print("sr:",sr)
# rr = round(random.uniform(20, 23),3)
# print("rr:",rr)
# bt = round(random.uniform(92,95),3)
# print("bt:",bt)
# lm = round(random.uniform(10,13),3)
# print("lm:",lm)
# bo = round(random.uniform(90,93),3)
# print("bo:",bo)
# em = round(random.uniform(85,96),3)
# print("em:",em)
# sh = round(random.uniform(2,6),3)
# print("sh:",sh)
# hr = round(random.uniform(60, 66),3)
# print("hr:",hr)

#Medium High (3)
# sr = round(random.uniform(80,91),3)
# print("sr:",sr)
# rr = round(random.uniform(22,26),3)
# print("rr:",rr)
# bt = round(random.uniform(90,93),3)
# print("bt:",bt)
# lm = round(random.uniform(12,18),3)
# print("lm:",lm)
# bo = round(random.uniform(88,91),3)
# print("bo:",bo)
# em = round(random.uniform(95,101),3)
# print("em:",em)
# sh = round(random.uniform(0, 3),3)
# print("sh:",sh)
# hr = round(random.uniform(65,76),3)
# print("hr:",hr)
#                         sr,rr,bt,lm,bo, em, sh,  hr
#new_data = pd.DataFrame([userd], columns=X.columns)

#High(4)
#userd=[sr,rr,bt,lm,bo,em,sh,hr]
# userd=[10,0,1,12,0,12,0,0]
# for i in range(len(userd)):
#   if(i==0):
#     if(userd[i]<40 and userd[i]>100):
#       print("Invalid Data Given")
#       break
#     else:
#       continue
#   elif i==1:
#     if(userd[i]<16 and userd[i]>50):
#       print("Invalid Data Given")
#       break
#     else:
#       continue
#   elif(i==2):
#     if(userd[i]<0 and userd[i]>99):
#       print("Invalid Data Given")
#       break
#     else:
#       continue
#   elif(i==3):
#     if(userd[i]<4 and userd[i]>30):
#       print("Invalid Data Given")
#       break
#     else:
#       continue
#   elif(i==4):
#     if(userd[i]<50 and userd[i]>97):
#       print("Invalid Data Given")
#       break
#     else:
#       continue
#   elif(i==5):
#     if(userd[i]<60 and userd[i]>150):
#       print("Invalid Data Given")
#       break
#     else:
#       continue
#   elif(i==6):
#     if(userd[i]<0 and userd[i]>24):
#       print("Invalid Data Given")
#       break
#     else:
#       continue
#   elif(i==7):
#     if(userd[i]<50 and userd[i]>80):
#       print("Invalid Data Given")
#       break
#     else:
# new_data = pd.DataFrame([userd], columns=X.columns)
print("Random Forest Algorithm")
new_data = pd.DataFrame([[60.514,18.87,91.011,10.341,94.46,80.36,6.154,60.927]], columns=X.columns)
# new_data = pd.DataFrame([[sr,rr,bt,lm,bo,em,sh,hr]], columns=X.columns)
predicted_stress_level = random_forest.predict(new_data)
stress_level_labels = {
    0: "Low/Normal",
    1: "Medium Low",
    2: "Medium",
    3: "Medium High",
    4: "High"
}

# Assuming you already have the 'predicted_stress_level' from the previous code snippet
predicted_stress_label = stress_level_labels[predicted_stress_level[0]]

# Display the human-readable label for the predicted stress level
print("Predicted Stress Label for New Data:",predicted_stress_level[0],"(",predicted_stress_label,")")