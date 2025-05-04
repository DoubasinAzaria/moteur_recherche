import os
import fitz  # PyMuPDF

def lire_pdf(chemin):
    texte = ""
    with fitz.open(chemin) as doc:
        for page in doc:
            texte += page.get_text()
    return texte

def collecter_textes(depuis='donnees'):
    textes = []
    noms_fichiers = []

    if not os.path.exists(depuis):
        raise FileNotFoundError(f"Le dossier '{depuis}' n'existe pas.")

    fichiers = os.listdir(depuis)
    if not fichiers:
        raise FileNotFoundError(f"Aucun fichier trouvé dans le dossier '{depuis}'.")

    for fichier in fichiers:
        chemin = os.path.join(depuis, fichier)
        if fichier.endswith('.txt'):
            with open(chemin, 'r', encoding='utf-8') as f:
                textes.append(f.read())
                noms_fichiers.append(fichier)
        elif fichier.endswith('.pdf'):
            try:
                texte = lire_pdf(chemin)
                textes.append(texte)
                noms_fichiers.append(fichier)
            except Exception as e:
                print(f"Erreur lors de la lecture de {fichier} : {e}")

    return noms_fichiers, textes
