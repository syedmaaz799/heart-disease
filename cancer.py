import streamlit as st
import joblib

st.title("Heart check")

st.header("Heart Disease Prediction")

st.subheader("A website where you can check your Heart Disease")

#taking a strnig input from a user 


gender = st.radio("Select you grnder",["Male","Female"])

if gender == "Male":
    gender = 1
else:
    gender = 0

Age = st.slider("Select your Age", max_value = 100)

current_smoker = st.radio("Do you still smoke?",["Yes","No"])

if current_smoker == "Yes":
    current_smoker = 1
else:
    current_smoker = 0

cigsperday = st.slider("Ciggerates Per Day", max_value = 100)

bpmeds = st.slider("BP Meds", max_value = 100)

stroke = st.radio("Do you have Stokes",["Yes","No"])

if stroke == "Yes":
    stroke = 1
else:
    stroke = 0

Hypertension = st.radio("Do you have Hypertension",["Yes","No"])

if Hypertension == "Yes":
    Hypertension = 1
else:
    Hypertension = 0

Diabetes = st.radio("Do you have Diabetes",["Yes","No"])

if Diabetes == "Yes":
    Diabetes = 1
else:
    Diabetes = 0

cholosterol =  st.number_input("How much is your Cholosterol?")

systolic_blood_pressure = st.number_input("How much is your systolic blood pressure?")

diastolic_blood_pressure = st.number_input("How much is your diastolic blood pressure?")

bmi = st.slider("What is your BMI rate?", max_value = 100)

heartrate = st.slider("What is your current heart rate?", max_value = 200)

if st.button("Predict!"):
    model = joblib.load("heart.h5")
    prediction = model.predict([[gender,Age,current_smoker,cigsperday,bpmeds,stroke,Hypertension,Diabetes,cholosterol,systolic_blood_pressure,diastolic_blood_pressure,bmi,heartrate]])
    if st.success(prediction):
        prediction == 1
        st.success("you have heart disease")
    else:
        st.success("you are healthy")




