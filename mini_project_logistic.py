import pandas as pd                    
import numpy as np                     
import matplotlib.pyplot as plt        
import seaborn as sns                  
from sklearn.model_selection import train_test_split    
from sklearn.metrics import confusion_matrix            
from sklearn.metrics import classification_report       
from sklearn.linear_model import LogisticRegression    
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
log_reg = LogisticRegression(max_iter=5000, C=0.2)
log_reg.fit(X_train, y_train)
print("Accuracy",log_reg.score(X_test, y_test))
# y_predict = log_reg.predict(X_test)
# matrix = confusion_matrix(y_test, y_predict)
# print("Confusion Matrix:")
# print(matrix)
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
#                         sr,     rr,   bt,   lm,bo, em, sh,  hr
#new_data = pd.DataFrame([userd], columns=X.columns)

#High(4)
# new_data = pd.DataFrame([userd], columns=X.columns)
print("Logistic Regression Algorithm")
new_data = pd.DataFrame([[97.216,27.216,86.52,17.608,83.824,101.52,0,78.04]], columns=X.columns)
# new_data = pd.DataFrame([[sr,rr,bt,lm,bo,em,sh,hr]], columns=X.columns)
predicted_stress_level = log_reg.predict(new_data)
stress_level_labels = {
    0: "Low/Normal",
    1: "Medium Low",
    2: "Medium",
    3: "Medium High",
    4: "High"
}
predicted_stress_label = stress_level_labels[predicted_stress_level[0]]
print("Predicted Stress Label for New Data:",predicted_stress_level[0],"(",predicted_stress_label,")")