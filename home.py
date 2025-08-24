import streamlit as st
import pandas as pd                    
import numpy as np                     
import matplotlib.pyplot as plt        
import seaborn as sns                  
from sklearn.model_selection import train_test_split    
from sklearn.metrics import confusion_matrix            
from sklearn.metrics import classification_report       
from sklearn.linear_model import LogisticRegression    
from sklearn.ensemble import RandomForestClassifier    
# st.sidebar.markdown("""
#    <div>
#             <h1>Health Statistics</h1>
#     </div>
# """,unsafe_allow_html=True)
def app():
    st.markdown("""
            <h1 style='text-align:center;color:brown;'><b>We are here to predict your stress</b></h1>
    """,unsafe_allow_html=True)
    form=st.form("form1")
    sr=form.number_input("Snoring Rate",key="1")
    rr=form.number_input("Respiration Rate",key="2")
    bt=form.number_input("Body Temperature",key="3")
    lm=form.number_input("Limb Movement",key="4")
    bo=form.number_input("Blood Oxygen",key="6")
    em=form.number_input("Eye Movement",key="7")
    sh=form.number_input("Sleeping Hours",key="8")
    hr=form.number_input("Heart Rate",key="9")
    submit=form.form_submit_button("Submit Data")
    st.subheader("Let us predict your stress....")
    
    # col1,col2=st.columns(2)
    # st.sidebar.button("Home")
    # st.sidebar.button("About")
    # st.sidebar.button("Contact Us")
    # Reading the CSV file 'SaYoPillow.csv' and storing the data in a DataFrame called 'data'
    data = pd.read_csv("Stress_Prediction.csv")
    # Displaying the first 5 rows of the dataset
    #st.dataframe(data)
    # Shape of our data
    print("Rows and Columns of the dataset :- ",data.shape)
    # Identifying information about composition and potential data quality
    data.info()
    # Displaying the columns in our dataset
    # data.columns
    # Renaming the columns of the DataFrame for better readability and understanding
    data.columns=['snoring_rate', 'respiration_rate', 'body_temperature', 'limb_movement', 'blood_oxygen','eye_movement', 'sleeping_hours', 'heart_rate', 'stress_level']
    #st.dataframe(data)
    # To show statistical summary of the columns of our data
    data.describe(include="all")
    #checking for null values in the dataframe
    data.isnull().sum() 
    # To display number of samples on each class
    # data['stress_level'].value_counts()
    # # sns.countplot(x='stress_level', data=data)

    # # Setting the label for the x-axis
    # plt.xlabel('Label')

    # # Setting the label for the y-axis
    # plt.ylabel('Count')

    # # Setting the title of the plot
    # plt.title('Distribution of the target variable')

    # Displaying the plot
    # plt.show()
    plt.figure(figsize=(10, 8))
    correlation_matrix = data.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='YlGnBu', fmt='.2f')
    plt.title("Correlation Matrix Heatmap")
    # plt.show()
    
    X = data.drop(['stress_level'], axis=1)
    y = data['stress_level']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("X_train shape:", X_train.shape)
    print("y_train shape:", y_train.shape)
    print("X_test shape:", X_test.shape)
    print("y_test shape:", y_test.shape)
    
    forest = RandomForestClassifier(n_estimators=500, random_state=1)

    
    forest.fit(X_train, y_train.values.ravel())
    
    importances = forest.feature_importances_

    # Loop over each feature and its importance
    for i in range(X_train.shape[1]):
        # Print the feature number, name, and importance score
        print("%2d) %-*s %f" % (i + 1, 30, data.columns[i], importances[i]))
    # Plotting the feature importances as a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(range(X_train.shape[1]), importances, align='center')
    plt.title('Feature Importance')
    plt.xticks(range(X_train.shape[1]), X_train.columns, rotation=90)
    plt.xlabel('Features')
    plt.ylabel('Importance Score')
    plt.tight_layout()
    plt.show()
    random_forest = RandomForestClassifier(n_estimators=13)
    random_forest.fit(X_train,y_train)
    random_forest.score(X_test,y_test)
    y_predict = random_forest.predict(X_test)

    matrix = confusion_matrix(y_test, y_predict)

    print("Confusion Matrix:")
    print(matrix)
    report = classification_report(y_test, y_predict)
    print("Classification Report:")
    print(report)
    log_reg = LogisticRegression(max_iter=1000, C=0.1)
    log_reg.fit(X_train, y_train)
    log_reg.score(X_test, y_test)
    y_predict = log_reg.predict(X_test)
    matrix = confusion_matrix(y_test, y_predict)

    print("Confusion Matrix:")
    print(matrix)
    if submit:
        new_data = pd.DataFrame([[sr,rr,bt, lm, bo, em, sh,hr]], columns=X.columns)
    
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
        st.markdown("""<h2>Stress Level:</h2>""",unsafe_allow_html=True)
        st.subheader(predicted_stress_label)
    # st.markdown("""<style>
    #             .dvn-scroller.glideDataEditor{
    #             visibility:hidden;
    #             }
    #             </style>""",unsafe_allow_html=True)