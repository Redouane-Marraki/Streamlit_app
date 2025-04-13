import streamlit as st
st.title("Ma première application Streamlit")
st.write("Bienvenue dans ce cours !")
nom = st.text_input("Quel est votre nom ?")
if nom:
   st.success(f"Enchanté, {nom} ! ")

age = st.slider("Quel est votre âge ?", 0, 100, 25)

st.write(f"Vous avez {age} ans")
genre = st.radio("Quel est votre genre ?", ["Homme", "Femme", "Autre"])
st.write(f"Genre choisi : {genre}")
if st.button("Cliquez ici"):
   st.balloons()
