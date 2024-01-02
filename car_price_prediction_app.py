import streamlit as st
import pandas as pd
import datetime
import joblib


model = joblib.load('car_price_predictor.pkl')
#model.load_model('D:\MACHINE LEARNING PROJECTS\car_price\car_price_model.json')

st.title("Car Price Prediction App")

p1 = st.number_input("Currect showroon price?",2.5,25.0, step=1.0)
p2 = st.number_input("Distance completed in kilometers?",0,500000,step=100)

s1 = st.selectbox('What is the fuel type?',('Petrol','Diesel','CNG'))
if s1 == 'Petrol':
    p3 = 0
elif s1 == 'Diesel':
    p3= 1
elif s1 == 'CNG':
    p3 = 2

s2 = st.selectbox('Are you a Dealer or Individual?',('Dealer','Individual'))
if s2 == 'Dealer':
    p4 = 0
elif s2 == 'Individual':
    p4 = 1

s3 = st.selectbox('What is Transmission type?',('Manual','Automatic'))
if s3 == 'Manual':
    p5 = 0
elif s3 == 'Automatic':
    p5 = 1

p6 = st.slider('Number of owners the car previously had?',0,3, step = 1)

date_time = datetime.datetime.now()
years =st.number_input("In which year was the car purchased?",2005,date_time.year)
p7 = date_time.year-years

try:
    if st.button('Predict Car Price'):
        result = model.predict([[p1,p2,p3,p4,p5,p6,p7]])
        if result>0:
            st.balloons()
            st.success("The car can be sold {:.2f} million".format(result[0]))
        else:
            st.warning("You cant sell the car")
except:
    st.warning("The car is too old")
