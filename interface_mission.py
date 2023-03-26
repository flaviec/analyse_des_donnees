import streamlit as st # installer avec pip install et doc dans : https://docs.streamlit.io/
import matplotlib.pyplot as plt
import pickle
import pandas as pd

# on récupère notre dico de df
# c'est la seule subtilité de streamlit : on ne veut pas charger le dico
# à chaque fois qu'on interragit avec l'appli : trop long !
# donc on va mettre en cache cette partie qui ne bougera plus de toute l'exécution

@st.cache
def load_data():
    with open('D:/ESTACA/4A/Projet industriel/analyse_des_donnees/df_traite.pkl', 'rb') as file:
        dg = pickle.load(file)
    return dg

dg = load_data()

LIST_MISSION = list(dg.unknown_IMISSIONTRAINNUMBER.unique()) 

# on écrit l'interface

# le titre
st.title("Interface d'accès aux données")

# un premier block : on veut choisir la racine à afficher
# on sélectionne dans une liste déroulante et on extrait du dico
st.subheader("Choisir le périmètre d'affichage")
mission = st.selectbox('Mission : ', LIST_MISSION)
df = dg.loc[dg.unknown_IMISSIONTRAINNUMBER == mission]
df

fig, ax = plt.subplots()
#df.plot(x='jour', y='min', color = 'red', ax =ax, marker='o')
df.plot.bar(x='jour', y=['min','median', 'mean','max'], ax = ax)
ax.set_xlabel('Date')
ax.set_ylabel('Consommation')

st.pyplot(fig)