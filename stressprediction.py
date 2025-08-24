import heartstatistics
import streamlit as st
import pandas as pd                    
import numpy as np                     
import matplotlib.pyplot as plt        
import seaborn as sns                  
from sklearn.model_selection import train_test_split     
from sklearn.metrics import confusion_matrix            
from sklearn.metrics import classification_report      
from sklearn.ensemble import RandomForestClassifier  
import random  
data = pd.read_csv("Stress_Prediction_Modifying.csv")
# print(data.head())
data.columns=['snoring_rate', 'respiration_rate', 'body_temperature', 'limb_movement', 'blood_oxygen','eye_movement', 'sleeping_hours', 'heart_rate', 'stress_level']
# print(data.head())
X = data.drop(['stress_level'], axis=1)
y = data['stress_level']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# print("X_train shape:", X_train.shape)
# print("y_train shape:", y_train.shape)
# print("X_test shape:", X_test.shape)
# print("y_test shape:", y_test.shape)
# forest = RandomForestClassifier(n_estimators=500, random_state=1)
# forest.fit(X_train, y_train.values.ravel())
# importances = forest.feature_importances_
# for i in range(X_train.shape[1]):
#     print("%2d) %-*s %f" % (i + 1, 30, data.columns[i], importances[i]))

random_forest = RandomForestClassifier(n_estimators=500, random_state=1)
random_forest.fit(X_train,y_train)
print("Accuracy",random_forest.score(X_test,y_test))
y_predict = random_forest.predict(X_test)
# matrix = confusion_matrix(y_test, y_predict)
# print("Confusion Matrix:")
# print(matrix)
# report = classification_report(y_test, y_predict)
# # Print the classification report
# print("Classification Report:")
# print(report)
def app():    
    st.markdown("""
                <h1 style='text-align:center;color:brown;'><b>We are here to predict your stress</b></h1>
        """,unsafe_allow_html=True)
    form=st.form("form1")
    sr=form.number_input("Snoring Rate",key="1",min_value=40.0, max_value=100.0)
    form.write("Value should be between 40 and 100")
    rr=form.number_input("Respiration Rate",key="2",min_value=16.0, max_value=30.0)
    form.write("Value should be between 16 and 30")
    bt=form.number_input("Body Temperature",key="3",min_value=80.0, max_value=99.0)
    form.write("Value should be between 80 and 99")
    lm=form.number_input("Limb Movement",key="4",min_value=4.0, max_value=25.0)
    form.write("Value should be between 4 and 25")
    bo=form.number_input("Blood Oxygen",key="6",min_value=80.0, max_value=97.0)
    form.write("Value should be between 80 and 97")
    em=form.number_input("Eye Movement",key="7",min_value=60.0, max_value=110.0)
    form.write("Value should be between 60 and 110")
    sh=form.number_input("Sleeping Hours",key="8",min_value=0.0, max_value=9.0)
    form.write("Value should be between 0 and 9")
    hr=form.number_input("Heart Rate",key="9",min_value=50.0, max_value=100.0)
    form.write("Value should be between 50 and 100")
    submit=form.form_submit_button("Submit Data")
    st.subheader("Let us predict your stress....")
    if submit:
        print("Random Forest Algorithm")
        # new_data = pd.DataFrame([[60.514,18.87,91.011,10.341,94.46,80.36,6.154,60.927]], columns=X.columns)
        new_data = pd.DataFrame([[sr,rr,bt,lm,bo,em,sh,hr]], columns=X.columns)
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
        # st.markdown("""<span>Stress Level:</span>""",unsafe_allow_html=True)
        # st.write(predicted_stress_label)
        if(predicted_stress_level[0]<=2):
            st.markdown(f'<span style="color:green">Stress Level:</span> {predicted_stress_label}', unsafe_allow_html=True)
        else:
            st.markdown(f'<span style="color:red">Stress Level:</span> {predicted_stress_label}', unsafe_allow_html=True)
        # heartstatistics.app(sr,rr,bt,lm,bo,em,sh,hr)
        st.markdown("""<h3>Visit Statistics Section for more Info</h3>""",unsafe_allow_html=True)
        heartstatistics.app(predicted_stress_label,sr,rr,bt,lm,bo,em,sh,hr)