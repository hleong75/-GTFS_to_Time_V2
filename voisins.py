import pandas as pd
from tqdm import tqdm

def main():
    # Charger les fichiers GTFS
    stops = pd.read_csv('stops.txt')
    stop_times = pd.read_csv('stop_times.txt')

    # Trier les données par trip_id et par heure d'arrivée
    stop_times = stop_times.sort_values(by=['trip_id', 'stop_sequence'])

    # Initialiser un dictionnaire pour stocker les voisins des stations
    neighbors = {}

    # Créer un objet tqdm pour afficher la progression
    progress_bar = tqdm(total=len(stop_times['trip_id'].unique()), desc="Processing")

    # Parcourir les stop_times pour remplir le dictionnaire des voisins
    for trip_id, group in stop_times.groupby('trip_id'):
        stops_in_trip = group['stop_id'].tolist()
        for i in range(len(stops_in_trip) - 1):
            current_stop = stops_in_trip[i]
            next_stop = stops_in_trip[i + 1]
            if current_stop not in neighbors:
                neighbors[current_stop] = []
            neighbors[current_stop].append(next_stop)
        # Mettre à jour la barre de progression après chaque élément traité
        progress_bar.update(1)

    # Fermer la barre de progression après le traitement
    progress_bar.close()

    # Supprimer les doublons dans les listes de voisins
    for stop in neighbors:
        neighbors[stop] = list(set(neighbors[stop]))

    # Enregistrer le dictionnaire dans un fichier texte
    with open('neighbors.txt', 'w') as file:
        for stop, next_stops in neighbors.items():
            for next_stop in next_stops:
                file.write(f'"{stop}": "{next_stop}"\n')

    print("Le fichier neighbors.txt a été créé avec succès.")

if __name__ == "__main__":
    main()
