import csv
from tqdm import tqdm

def lire_arrets(nom_fichier):
    """
    Lit les arrêts à partir d'un fichier CSV et retourne un dictionnaire des arrêts.

    Args:
        nom_fichier (str): Le nom du fichier CSV contenant les arrêts.

    Returns:
        dict: Un dictionnaire avec les ID des arrêts comme clés et les noms des arrêts comme valeurs.
    """
    arrets = {}
    with open(nom_fichier, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
        for row in tqdm(rows, desc="Lecture des arrêts"):
            arrets[row['stop_id'].zfill(4)] = row['stop_name']
    return arrets

def lire_temps_de_trajet(nom_fichier):
    """
    Lit les temps de trajet à partir d'un fichier CSV et retourne un dictionnaire des temps de trajet.

    Args:
        nom_fichier (str): Le nom du fichier CSV contenant les temps de trajet.

    Returns:
        dict: Un dictionnaire avec les arrêts de départ comme clés et un autre dictionnaire en valeur
              contenant les arrêts de destination et les temps de trajet.
    """
    temps_de_trajet = {}
    with open(nom_fichier, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
        for row in tqdm(rows, desc="Lecture des temps de trajet"):
            current_stop = int(row['current_stop'])
            next_stop = int(row['next_stop'])
            time = float(row['travel_time'])
            if current_stop not in temps_de_trajet:
                temps_de_trajet[current_stop] = {}
            temps_de_trajet[current_stop][next_stop] = time
    return temps_de_trajet

def sauvegarder_donnees(arrets, temps_de_trajet, nom_fichier):
    """
    Sauvegarde les arrêts et les temps de trajet dans un fichier texte.

    Args:
        arrets (dict): Un dictionnaire des arrêts avec les ID comme clés et les noms comme valeurs.
        temps_de_trajet (dict): Un dictionnaire des temps de trajet avec les arrêts de départ comme clés
                                et un autre dictionnaire en valeur contenant les arrêts de destination
                                et les temps de trajet.
        nom_fichier (str): Le nom du fichier texte où les données seront sauvegardées.

    Returns:
        None
    """
    with open(nom_fichier, 'w', encoding='utf-8') as file:
        file.write("[Vertices]\n")
        for stop_id, stop_name in tqdm(arrets.items(), desc="Écriture des arrêts"):
            file.write(f"{stop_id} {stop_name}\n")

        file.write("[Edges]\n")
        for current_stop, destinations in tqdm(temps_de_trajet.items(), desc="Écriture des temps de trajet"):
            for next_stop, time in destinations.items():
                file.write(f"{current_stop} {next_stop} {time}\n")

def main():
    """
    Fonction principale pour exécuter les opérations de lecture et de sauvegarde des données.
    
    Args:
        None

    Returns:
        None
    """
    arrets = lire_arrets('arrets.csv')
    temps_de_trajet = lire_temps_de_trajet('travel_time_updated.csv')
    sauvegarder_donnees(arrets, temps_de_trajet, 'data.txt')
    print("Données sauvegardées dans data.txt")

if __name__ == "__main__":
    main()
