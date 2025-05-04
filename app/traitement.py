from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import nltk

# Télécharger les stopwords français s'ils ne sont pas déjà présents
nltk.download('stopwords')

# Charger les stopwords en français
stop_words_fr = stopwords.words('french')

def indexer_textes(textes):
    """
    Prend une liste de textes et retourne le vectoriseur TF-IDF entraîné
    ainsi que la matrice des poids TF-IDF.
    """
    vectoriseur = TfidfVectorizer(stop_words=stop_words_fr)
    tfidf_matrice = vectoriseur.fit_transform(textes)
    return vectoriseur, tfidf_matrice
