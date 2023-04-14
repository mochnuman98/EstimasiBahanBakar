import pickle
import streamlit as st

gastype = pickle.load(open('Estimasi_Konsumsi_Bahan_Bakar.sav', 'rb'))

st.title('Estimasi Konsumsi Bahan Bakar')

distance = st.number_input('Input Jarak Yang Ditempuh')
speed = st.number_input('Input Kecepatan')
temp_inside = st.number_input('Input Suhu Udara Dalam')
temp_outside = st.number_input('Input Suhu Udara Luar')
gas_type = st.number_input('Input Ron Bahan Bakar')

predict = ''

if st.button('Estimasi Konsumsi Bahan Bakar'):
    predict = gastype.predict(
        [[distance,speed,temp_inside,temp_outside,gas_type]]
        )
    st.write ('Estimasi Konsumsi Bahan Bakar : ', predict)
