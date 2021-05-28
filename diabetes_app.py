'''@Author : Rashmi Deshmukh'''
import streamlit as st
import pandas as pd
from PIL import Image
import pickle


model = pickle.load(open('KNN_Model.pkl', 'rb'))

html_temp=""" <div style="background-color:Blue;padding:2px"> """

def run():
    img1 = Image.open('img.png')
    img1 = img1.resize((500, 245))
    st.image(img1, use_column_width=False)
    st.title("Check You Have Diabetes or Not?")

    st.markdown(html_temp, unsafe_allow_html=True)

    Pregnancies=st.slider("1. Number of Pregnancies :",0,17)
    Glucose=st.slider("2. Glucose Level :",0,200)
    BloodPressure=st.slider("3. Blood Pressure :",0,180)
    Insulin=st.slider("4. Insulin Level :",0,900)
    BMI=st.number_input("5.Body Mass Index(BMI):")
    DiabetesPedigreeFunction=st.number_input("6. DiabetesPedigreeFunction(family history ratio value) :")
    #Age=st.number_input("7. Age:")
    Age = st.slider("7. Age:",0,100)
    st.markdown(html_temp, unsafe_allow_html=True)

    if st.button("Submit"):
        features = [[Pregnancies,Glucose,BloodPressure,Insulin,BMI,DiabetesPedigreeFunction,Age]]

        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans==1:
            st.success("You Have Diabetes!")
        else:
            st.success("You Don't Have Diabetes!")
run()
