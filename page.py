# Fichier principal : app.py ou autre
import streamlit as st
import pandas as pd

def show_sheets_page():
    st.title("Lecture de Google Sheets dans Streamlit")

    sheet_id = "13itleyU47ijDQO_hyA3xYV93eDVkwvgvj_A7u900kWk"
    sheet_name = "ensam01"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

    try:
        df = pd.read_csv(url)
        st.success("Données chargées avec succès depuis Google Sheets !")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Erreur lors du chargement des données : {e}")

# 💡 Il faut appeler la fonction ici :
show_sheets_page()
