# simpan sebagai app.py
import streamlit as st
import random

st.title("Game Tebak Angka - Muhammad Jefri")

if 'angka_rahasia' not in st.session_state:
    st.session_state.angka_rahasia = random.randint(1, 100)
    st.session_state.tebakan = 0

tebakan = st.number_input("Tebak angka antara 1 - 100:", min_value=1, max_value=100, step=1)

if st.button("Tebak"):
    st.session_state.tebakan += 1
    if tebakan < st.session_state.angka_rahasia:
        st.warning("Terlalu kecil")
    elif tebakan > st.session_state.angka_rahasia:
        st.warning("Terlalu besar")
    else:
        st.success(f"Benar! Kamu menang dalam {st.session_state.tebakan} percobaan.")
        st.session_state.angka_rahasia = random.randint(1, 100)
        st.session_state.tebakan = 0
        

        
    


