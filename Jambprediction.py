# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 12:32:23 2024

@author: AKIN-JOHNSON
"""

import pickle
import streamlit as st

# loading the logistic trained model
with open("Jamb_pred_lr.sav", 'rb') as file:
    lr_model = pickle.load(file)
# loading the KNN trained model
with open("Jamb_pred_knn.sav", 'rb') as file:
    knn_model = pickle.load(file)

# creating a function for prediction for logistic regression
def jamb_prediction(input_data):
    prediction = lr_model.predict(input_data)
    if (prediction == 0):
        return 'Student Fails Jamb'
    else:
        return 'Student Pass!!!'
    

def main():
    # Giving a Header and title to my streamlit
    st.title('JAMB PREDICTION WEB APP')
    st.header('Predicting whether students pass or fails their jamb exams', divider="green")
    # creating the input data fields
    #    'parent_education',
    #   'internet_access', 'students_jamb_score', 'parental_income',
    #   'health_issues', 'extracurricular_participation'
    math_score = st.text_input('Score for Mathematics')
    english_score = st.text_input('Score for English Language')
    class_attendance = st.text_input('Score for Students attendance')
    study_hours = st.text_input('Students study hours per week')
    study_method = st.text_input('Students preferred study method (Group Study = 0, Indivudual = 1, Tutorials = 2)')
    parent_education = st.text_input('Parents education level (Primary = 0, Secondary = 1, Tertiary = 2)')
    internet_access = st.text_input('Does the student have internet access (No = 0, Yes = 1)')
    jamb_score = st.text_input('Students Jamb Score')
    parental_income = st.text_input('Parents income level (High = 0, Low = 1, Medium = 2)')
    health_issues = st.text_input('Does student have Health issues? (No = 0, Yes = 1)')
    extracurricular = st.text_input('Does Student pertake in extra curricular activities (No = 0, Yes = 1)')
    
    # code for prediction
    outcome = ''
    
    # create a button for the prediction
    if st.button('Outcome'):
        try:
            # Convert inputs to appropriate types
            math_score = int(math_score)
            english_score = int(english_score)
            class_attendance = int(class_attendance)
            study_hours = int(study_hours)
            study_method = int(study_method.split(' ')[-1].strip(')'))  # Convert from string to int
            parent_education = int(parent_education.split(' ')[-1].strip(')'))  # Convert from string to int
            internet_access = int(internet_access.split(' ')[-1].strip(')'))  # Convert from string to int
            jamb_score = int(jamb_score)
            parental_income = int(parental_income.split(' ')[-1].strip(')'))  # Convert from string to int
            health_issues = int(health_issues.split(' ')[-1].strip(')'))  # Convert from string to int
            extracurricular = int(extracurricular.split(' ')[-1].strip(')'))  # Convert from string to int
            
            # Create input array for prediction
            input_data = [[math_score, english_score, class_attendance, study_hours, study_method, parent_education, internet_access, jamb_score, parental_income, health_issues, extracurricular]]
            
            # Get prediction outcome
            outcome = jamb_prediction(input_data)
        except ValueError:
            outcome = 'Please ensure all inputs are valid numbers.'
    # Show outcome
    st.success(outcome)
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
