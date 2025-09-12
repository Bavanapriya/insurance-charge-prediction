import streamlit as st
import pandas as pd
import joblib

pipeline = joblib.load('insurance_pipeline.pkl')

st.set_page_config(page_title="Insurance Cost Predictor", layout="centered")
st.title('🩺 Insurance Cost Predictor')
st.write("Enter your details below to get an estimated insurance claim amount.")

col1, col2 = st.columns(2)

with col1:
    st.header("Personal Details")
    age = st.slider('Age', 18, 100, 30)
    sex = st.selectbox('Sex', ['male', 'female'])
    bmi = st.slider('BMI (Body Mass Index)', 15.0, 60.0, 25.0, 0.1)
    no_of_dependents = st.slider('Number of Dependents', 0, 10, 1)

with col2:
    st.header("Health Status")
    smoker = st.selectbox('Smoker', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
    bloodpressure = st.slider('Blood Pressure (Systolic)', 50, 150, 80)
    diabetes = st.selectbox('Diabetes', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
    regular_ex = st.selectbox('Regular Exercise', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')


if st.button('Predict Insurance Cost', use_container_width=True):
    
    input_data = pd.DataFrame({
        'age': [age], 'sex': [sex], 'bmi': [bmi], 'no_of_dependents': [no_of_dependents],
        'smoker': [smoker], 'bloodpressure': [bloodpressure], 'diabetes': [diabetes],
        'regular_ex': [regular_ex]
    })

    prediction = pipeline.predict(input_data)
    
    st.success(f'Predicted Insurance Claim: ${prediction[0]:,.2f}')