import pickle
import streamlit as st

gastype = pickle.load(open('Estimasi_Konsumsi_Bahan_Bakar.sav', 'rb'))

st.title('Estimasi Konsumsi Bahan Bakar')

speed = st.number_input('Input Kecepatan')
temp_inside = st.number_input('Input Suhu Udara Dalam')
temp_outside = st.number_input('Input Jarak Berkendara')

predict = ''

if st.button('Estimasi Konsumsi Bahan Bakar'):
    predict = gastype.predict(
        [[speed,temp_inside,temp_outside]]
        )
    st.write ('Estimasi Konsumsi Bahan Bakar : ', predict)
