from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def rechercher_documents(requete, vectoriseur, matrice, noms, k=5):
    vecteur_requete = vectoriseur.transform([requete])
    similarites = cosine_similarity(vecteur_requete, matrice).flatten()
    meilleurs_indices = np.argsort(similarites)[::-1][:k]
    return [(noms[i], similarites[i]) for i in meilleurs_indices]
