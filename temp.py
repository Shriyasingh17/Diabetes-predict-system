# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle
import streamlit as st
# # File path for your trained model
model_path = r'C:/Users/DELL/OneDrive/Desktop/diabetesprediction ml model/trained_model.sav'
#import subprocess

# Run Streamlit from Jupyter Notebook using subprocess
#subprocess.run(["streamlit", "run", "C:/Users/DELL/OneDrive/Desktop/diabetesprediction ml model/streamlitcode.py"])

#creating a function for prediction
def diabetes_prediction(input_data):
# Example input data
    input_data = (5, 166, 72, 19, 175, 25.8, 0.587, 51)

# Convert input data to a NumPy array
    input_data_as_numpy_array = np.asarray(input_data)

# Reshape the array for a single instance prediction
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

# Load the trained model correctly
    with open(model_path, 'rb') as file:
       loaded_model = pickle.load(file)

# Make a prediction
    prediction = loaded_model.predict(input_data_reshaped)

# Print the result
    if prediction[0] == 0:
       return'The Person is not Diabetic'
    else:
      return'The Person is Diabetic'

#def main():


    #giving a title
def diabetes_prediction(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age):
    # Your prediction logic here
    # For example, return a dummy diagnosis
  return "The Person is Diabetes " if glucose > 120 else "The Person is not Diabetes"

def main():
    # Input fields for user to enter data
    Pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, value=0)
    Glucose = st.number_input("Glucose Level", min_value=0, max_value=200, value=0)
    BloodPressure = st.number_input("Blood Pressure", min_value=0, max_value=200, value=0)
    SkinThickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=0)
    Insulin = st.number_input("Insulin Level", min_value=0, max_value=1000, value=0)
    BMI = st.number_input("Body Mass Index (BMI)", min_value=0.0, max_value=50.0, value=0.0)
    DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.0)
    Age = st.number_input("Age", min_value=0, max_value=120, value=0)

    # Call the prediction function with the defined variables
    if st.button("Predict"):
        diagnosis = diabetes_prediction(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
        st.write(f"Diagnosis: {diagnosis}")


   #code for prediction
    diagnosis =''


    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diagnosis=diabetes_prediction(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)

    st.success(diagnosis)





if __name__ == '__main__':
   main()