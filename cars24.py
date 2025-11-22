import streamlit as st
import pandas as pd
import yfinance as yf
import pickle

st.title("Car Price Prediction App")
#fuel type, transmission, engine, seats
col1, col2=st.columns(2)
with col1:
    fuel_type = st.radio("Fuel Type", ["Petrol", "Diesel", "CNG", "Electric"])
    
with col2:
    transmission = st.selectbox("Transmission Type", ["Manual", "Automatic"])

col3,col4=st.columns(2)
with col3:
    engine = st.slider("Engine Capacity", min_value=500, max_value=5000, step=100)
with col4:
    seats = st.selectbox("Seats", [2,3,4,5,6,7,8,9,10])

model= pickle.load(open('car_pred.pkl', 'rb'))


#with open("car_pred", "rb") as f:
#    model = pickle.load(f)
#xgb.predict(prediction_data)
encode_dict={
    "fuel_type": {"Diesel":1,"Petrol":2, "CNG":3, 'LPG':4, "Electric":5,
    'transmission': {"Manual":1, "Automatic":2}}
}

def model_pred(fuel_type, transmission, engine, seats):
    transmission= encode_dict['transmission'][transmission]
    fuel_type= encode_dict['fuel_type'][fuel_type]

    data= [[2018.0,1,40000,fuel_type, transmission, 18.0, engine,85,seats]] 
    return model.predict(data)

if st.button("Predict Price"):
    st.write(model_pred(fuel_type, transmission, engine, seats))
else:
    st.write("Click on Predict, once you're done with the data")  

#pip freeze > requirement.txt
