import numpy as np
import pandas as pd
from tqdm import tqdm

def main():
    """
    Fonction principale pour lire les arrêts et les temps de trajet à partir de fichiers CSV,
    puis sauvegarder les données dans des fichiers numpy.

    Args:
        None

    Returns:
        None
    """
    # Lecture du fichier des arrêts
    fichier = open("arrets.csv", "r")
    N = fichier.readlines()  # Crée une liste où N[i] contient la i-ème ligne du fichier

    L = []
    M = []
    der = 0

    # Traitement des lignes du fichier des arrêts
    for i in tqdm(N, desc="Traitement des lignes d'arrêt"):
        if i[5:-1] == der:
            n = len(M)
            M.append(i[5:-1] + str(n))
        else:
            L.extend(M)
            M = [i[5:-1]]
            der = M[0]
    L.extend(M)

    D = {L[i]: i for i in range(len(L))}
    fichier.close()

    # Lecture du fichier des temps de trajet
    df = pd.read_csv('travel_time_updated.csv', delimiter=',', header=None).fillna('')
    M = np.zeros((len(L), len(L)))

    # Traitement des temps de trajet
    for row in tqdm(df.values, desc="Traitement des temps de trajet"):
        M[int(row[0]), int(row[1])] = row[2]

    # Sauvegarde des données dans des fichiers numpy
    Dictionnaire='TP14D.npy'
    Matrice='TP14M.npy'
    np.save('TP14D.npy', D)
    np.save('TP14M.npy', M)
    print(f"Traitement de {Dictionnaire} et {Matrice} effectué.")

if __name__ == "__main__":
    main()
