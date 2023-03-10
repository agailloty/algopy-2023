import streamlit as st
import pandas as pd
from datetime import datetime
import uuid
import os

os.chdir(os.path.dirname(__file__))

st.write(" # Enquête insertion professionnelle")
st.write("Nous souhaitons constituer une base de donnée partagée permettant aux personnes diplômées de renseigner des informations sur leur insertion professionnelle.")

domaines = ["Physique", "mathématiques",
"Chimie, biochimie, sc. de la vie et de la terre",
"Économie",
"Droit, sciences politiques",
"Histoire, géographie",
"Sociologie",
"Psychologie",
"Français, littérature, philosophie",
"Arts",
"Langues, linguistique",
"Spécialités de la production"
"Commerce, vente",
"Finance, assurances, comptabilité, gestion",
"Communication", "documentation",
"Informatique", "réseaux"]

etablissements = pd.read_csv("etablissements.csv", sep = ";").iloc[:, 1]


col1, col2 = st.columns(2)
with col1:
    st.write("## Diplôme")
    date_diplome = st.date_input("Année obtention diplôme")
    intitule_formation = st.text_input("Intitulé formation")
    domaine_formation = st.selectbox("Domaine formation", domaines)
    etablissement = st.selectbox("Etablissement", etablissements)

with col2:
    st.write("## Recherche d'emploi")
    duree = st.number_input("Durée d'attente avant premier emploi (mois)", min_value=0, max_value=25000)
    meme_ville_formation = st.checkbox("Emploi dans la même ville que la formation")

def save_data():
    timestamp = datetime.now()
    filename = "survey.csv"
    survey_data = pd.DataFrame()
    row = pd.DataFrame({
        "id" : uuid.uuid1(),
        "date_diplome": date_diplome,
        "intitule_formation": intitule_formation,
        "domaine_formation" : domaine_formation,
        "etablissement" : etablissement,
        "duree" : duree,
        "meme_ville_formation" : meme_ville_formation,
        "timestamp" : timestamp
    }, index=[0])

    row.to_csv(filename, index=False, mode="a", header=False)

st.button("Soumettre", on_click=save_data)

# Logique pour rendre les données persistentes

## Enregistrer les résultats en format csv

