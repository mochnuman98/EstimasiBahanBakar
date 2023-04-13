import pickle
import streamlit as st

speedukur = pickle.load(open('Estimasi_Konsumsi_Bahan_Bakar.sav', 'rb'))

st.title('Estimasi Konsumsi Bahan Bakar')

distance = st.number_input('Input Jarak Yang Ditempuh')
speed = st.number_input('Input Kecepatan')

predict = ''

if st.button('Estimasi Konsumsi Bahan Bakar'):
    predict = speedukur.predict(
        [[speed,distance]]
        )
    st.write ('Estimasi Konsumsi Bahan Bakar : ', predict)
