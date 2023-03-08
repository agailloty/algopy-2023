import streamlit as st
import pandas as pd
import os, uuid
os.chdir(os.path.dirname(__file__))

@st.cache_data
def load_data():
    return pd.read_csv("etablissements.csv", sep=";").iloc[:, 1]
etablissements = load_data()


st.write("# Enquête insertion professionnelle")
st.write("""
Nous souhaiterons constituer une base de données en ligne similaire dans l'esprit à l'enquête menée par Département des études statistiques de l'enseignement supérieur
https://data.enseignementsup-recherche.gouv.fr/explore/dataset/fr-esr-insertion_professionnelle-master_donnees_nationales/information/
Ce qui différencie toutefois notre étude est le poids que nous accordons aux perceptions des diplômés.
""")



col1, col2 = st.columns(2)
with col1:
    st.write("## Diplôme")
    year = st.number_input("Année obtention diplôme", min_value=1960, max_value=2090)
    etablissement = st.selectbox("Etablissement", etablissements)
    lib_dplome = st.text_input("Libellé du diplôme")

def save_data():
    filename = "survey.csv"
    row = pd.DataFrame({
        "ID" : uuid.uuid1(),
        "Year": year,
        "Etablissement": etablissement,
        "LibDiploma": lib_dplome
    }, index= [0])
    print(row)
    row.to_csv(filename, mode="a", index=False, header=None)

st.button("Save Data", on_click=save_data)



    