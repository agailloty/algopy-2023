import streamlit as st
import os
import pickle
# Charger en mémoire les modèles
currdir = os.path.dirname(__file__)
os.chdir(currdir)
print(os.getcwd())

with open("model_bg.joblib", "rb") as f:
    MODEL_RF = pickle.load(f)

# Definir l'interface

st.write("# Prédire la probabilité de souscrire à une assurance")

st.write("## Veuillez entrer les caractéristiques de la personne pour laquelle vous voulez calculer la probabilité de souscription à une assurance voyage.")

age = st.number_input("Age", min_value=1,  max_value=100)
annual_income = st.number_input("Revenu annuel")
family_members = st.number_input("Nombre des membres de famille voyageant avec la personne")
chronic_disease = st.checkbox("La personne souffre-t-elle d'une maladie chronique?")
employment_gvmnt = st.checkbox("La personne travaille-t-elle pour le gouvernement de son pays ?")
graduated = st.checkbox("La personne est-elle diplômé d'un Bac +5 et plus ?")
frequent_flyer = st.checkbox("La personne voyage-t-elle souvent ?")
ever_travelled = st.checkbox("La personne a-t-elle déjà voyagé à l'étranger ?")

x_pred = [[age, annual_income, family_members, chronic_disease,employment_gvmnt, 
              graduated, frequent_flyer, ever_travelled]]
proba = MODEL_RF.predict_proba(x_pred)[0][0]

st.button("Calculez la probabilité")
st.text(f"La probabilité que cette personne souscrive à l'assurance est de {proba} ")