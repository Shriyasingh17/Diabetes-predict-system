# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 23:47:15 2025
@author: DELL
"""
import pickle
import streamlit as st

# Install the missing package (you need to run this command in your terminal/command prompt first)
# pip install streamlit-option-menu

# Then import the package
from streamlit_option_menu import option_menu

# Loading the saved model
diabetes_model = pickle.load(open('trained_model.sav', 'rb'))
 
# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Diabetes Prediction System',
                          ['Diabetes Prediction',
                           'Young Diabetes Prediction System',
                           'Adult Diabetes Prediction System'],
                          icons=['activity', 'heart', 'person'],
                          default_index=0)

# Diabetes prediction page
if (selected == 'Diabetes Prediction'):
    # Page title
    st.title('Diabetes Prediction Using ML')  
    
    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    
    with col2:
        Glucose = st.text_input('Glucose level')  # Fixed typo in variable name
        
    with col3:
        BloodPressure = st.text_input('Blood Pressure level')  # Standardized variable name
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness level')
        
    with col2:
        Insulin = st.text_input('Insulin level')  
    
    with col3: 
        BMI = st.text_input('BMI level')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function level') 
    
    with col2:
        Age = st.text_input('Age Value')
    
    # Code for prediction
    diab_diagnosis = ''
    
    # Creating a button for prediction
    if st.button('Diabetes Test Result'):
        # Convert inputs to float, with input validation
        try:
            input_data = [
                float(Pregnancies if Pregnancies else 0),
                float(Glucose if Glucose else 0),
                float(BloodPressure if BloodPressure else 0),
                float(SkinThickness if SkinThickness else 0),
                float(Insulin if Insulin else 0),
                float(BMI if BMI else 0),
                float(DiabetesPedigreeFunction if DiabetesPedigreeFunction else 0),
                float(Age if Age else 0)
            ]
            
            # Make prediction
            diab_prediction = diabetes_model.predict([input_data])
            
            if (diab_prediction[0] == 1):
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'
                
        except ValueError:
            diab_diagnosis = 'Please enter valid numerical values for all fields'
            
    st.success(diab_diagnosis)

# Placeholder for Young Diabetes Prediction System
if (selected == 'Young Diabetes Prediction System'):
    st.title('Young Diabetes Prediction System')
    st.write('This feature is coming soon!')

# Placeholder for Adult Diabetes Prediction System
if (selected == 'Adult Diabetes Prediction System'):
    st.title('Adult Diabetes Prediction System')
    st.write('This feature is coming soon!')