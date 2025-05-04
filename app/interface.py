import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from app.collecte import collecter_textes
from app.traitement import indexer_textes
from app.recherche import rechercher_documents

st.title("🔍 Moteur de Recherche d'Information")

# Chargement et indexation
noms_fichiers, textes = collecter_textes()
vectoriseur, matrice_tfidf = indexer_textes(textes)

requete = st.text_input("Entrez votre requête :")

if requete:
    resultats = rechercher_documents(requete, vectoriseur, matrice_tfidf, noms_fichiers)
    st.subheader("Résultats :")
    for nom, score in resultats:
        st.write(f"**{nom}** — Pertinence : {score:.4f}")
