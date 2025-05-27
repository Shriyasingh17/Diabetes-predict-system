import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the models 
# Please ensure these files are in the working directory or update the paths accordingly
try:
    pregnancy_model = pickle.load(open('trained_model.sav', 'rb'))
except FileNotFoundError:
    pregnancy_model = None
try:
    young_diabetes_model = pickle.load(open('young_trained_model.sav', 'rb'))
except FileNotFoundError:
    young_diabetes_model = None
try:
    adult_diabetes_model = pickle.load(open('adult_trained_model.sav', 'rb'))
except FileNotFoundError:
    adult_diabetes_model = None


def pregnancy_sidebar():
    st.sidebar.header("Pregnancy Diabetes Prediction Inputs")
    Pregnancies = st.sidebar.text_input('Number of Pregnancies')
    Glucose = st.sidebar.text_input('Glucose Level')
    BloodPressure = st.sidebar.text_input('Blood Pressure Level')
    SkinThickness = st.sidebar.text_input('Skin Thickness Level')
    Insulin = st.sidebar.text_input('Insulin Level')
    BMI = st.sidebar.text_input('BMI Level')
    DiabetesPedigreeFunction = st.sidebar.text_input('Diabetes Pedigree Function')
    Age = st.sidebar.text_input('Age')

    return [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]

def young_diabetes_sidebar():
    st.sidebar.header("Young Diabetes Prediction Inputs")
    Age = st.sidebar.text_input('Age')
    BMI = st.sidebar.text_input('BMI Level')
    Blood_Pressure = st.sidebar.text_input('Blood_Pressure Level')
    Glucose = st.sidebar.text_input('Glucose Level')
    Physical_Activity_Level = st.sidebar.text_input('Physical_Activity_Level Level')
    Sleep_Hours = st.sidebar.text_input('Sleep_Hours Level')
    Stress_Level = st.sidebar.text_input('Stress_Level Function')
    Genetic_Risk_Score= st.sidebar.text_input('Genetic_Risk_Score')

    return [Age,  BMI, Blood_Pressure, Glucose,Physical_Activity_Level, Sleep_Hours,Stress_Level, Genetic_Risk_Score]

def adult_diabetes_sidebar():
    st.sidebar.header("Adult Diabetes Prediction Inputs")
    Gender = st.sidebar.text_input('gender')
    Age = st.sidebar.text_input(' Age')
    Hypertension = st.sidebar.text_input('Hypertension Level')
    Heart_disease = st.sidebar.text_input('Heart_disease Level')
    Smoking_disease = st.sidebar.text_input('Smoking_disease Level')
    BMI = st.sidebar.text_input('BMI Level')
    HbA1c_level = st.sidebar.text_input('HbA1c_level Function')
    blood_glucose_level = st.sidebar.text_input(' blood_glucose_level')

    return [Gender, Age , Hypertension, Heart_disease, Smoking_disease, BMI, HbA1c_level,  blood_glucose_level]

def validate_and_convert(input_list):
    try:
        converted = [float(x) if x else 0.0 for x in input_list]
        return converted
    except ValueError:
        st.error("Please enter valid numeric values for all inputs in the sidebar.")
        return None

def predict_diabetes(model, input_data):
    prediction = model.predict([input_data])
    if prediction[0] == 1:
        return "The person is diabetic."
    else:
        return "The person is not diabetic."

st.title("Diabetes Prediction System")

# Navigation menu in main area since sidebar is used for inputs
selected_option = option_menu("", 
    options=["Pregnancy Diabetes Prediction", "Young Diabetes Prediction System", "Adult Diabetes Prediction System"], 
    icons=["activity", "heart", "person"],
    menu_icon="cast", default_index=0, orientation="horizontal")


if selected_option == "Pregnancy Diabetes Prediction":
    st.header("Pregnancy Diabetes Prediction System")
    if pregnancy_model is None:
        st.error("Pregnancy diabetes model file not found. Please provide pregnancy_model.sav file.")
    else:
        inputs = pregnancy_sidebar()
        data = validate_and_convert(inputs)
        if data and st.button("Predict Diabetes"):
            result = predict_diabetes(pregnancy_model, data)
            st.success(result)

elif selected_option == "Young Diabetes Prediction System":
    st.header("Young Diabetes Prediction System")
    if young_diabetes_model is None:
        st.error("Young diabetes model file not found. Please provide young_diabetes_model.sav file.")
    else:
        inputs = young_diabetes_sidebar()
        data = validate_and_convert(inputs)
        if data and st.button("Predict Diabetes"):
            result = predict_diabetes(young_diabetes_model, data)
            st.success(result)

elif selected_option == "Adult Diabetes Prediction System":
    st.header("Adult Diabetes Prediction System")
    if adult_diabetes_model is None:
        st.error("Adult diabetes model file not found. Please provide adult_diabetes_model.sav file.")
    else:
        inputs = adult_diabetes_sidebar()
        data = validate_and_convert(inputs)
        if data and st.button("Predict Diabetes"):
            result = predict_diabetes(adult_diabetes_model, data)
            st.success(result)

