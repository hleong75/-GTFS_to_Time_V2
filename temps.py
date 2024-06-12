import csv
import pandas as pd
from tqdm import tqdm

def main():
    # Étape 1 : Lire le fichier neighbors.txt et reconstruire le dictionnaire
    neighbors = {}
    with open('neighbors.txt', 'r') as file:
        for line in tqdm(file, desc="Reading neighbors.txt"):
            stop, next_stop = line.strip().split(': ')
            stop = stop.strip('"')
            next_stop = next_stop.strip('"')
            if stop not in neighbors:
                neighbors[stop] = []
            neighbors[stop].append(next_stop)

    # Étape 2 : Charger les fichiers GTFS
    stop_times = pd.read_csv('stop_times.txt')

    # Fonction pour convertir les temps au format 'HH:MM:SS' en secondes depuis minuit
    def time_to_seconds(t):
        hours, minutes, seconds = map(int, t.split(':'))
        return hours * 3600 + minutes * 60 + seconds

    # Convertir les heures d'arrivée en secondes depuis minuit
    stop_times['arrival_seconds'] = stop_times['arrival_time'].apply(time_to_seconds)

    # Créer un dictionnaire pour stocker les temps de trajet
    travel_times = {}

    # Parcourir les stop_times pour calculer les temps de trajet
    for trip_id, group in tqdm(stop_times.groupby('trip_id'), desc="Calculating travel times"):
        group = group.sort_values(by='stop_sequence')
        stop_list = group['stop_id'].tolist()
        time_list = group['arrival_seconds'].tolist()
        for i in range(len(stop_list) - 1):
            current_stop = stop_list[i]
            next_stop = stop_list[i + 1]
            travel_time = time_list[i + 1] - time_list[i]
            if current_stop not in travel_times:
                travel_times[current_stop] = {}
            travel_times[current_stop][next_stop] = travel_time

    # Étape 3 : Créer et enregistrer le fichier CSV avec tqdm
    with open('travel_times.csv', 'w', newline='') as csvfile:
        fieldnames = ['current_stop', 'next_stop', 'travel_time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        # Créer un objet tqdm pour afficher la progression
        progress_bar = tqdm(total=len(neighbors.items()), desc="Writing CSV")

        for current_stop, next_stops in neighbors.items():
            for next_stop in next_stops:
                if current_stop in travel_times and next_stop in travel_times[current_stop]:
                    writer.writerow({
                        'current_stop': current_stop,
                        'next_stop': next_stop,
                        'travel_time': travel_times[current_stop][next_stop]
                    })
            # Mettre à jour la barre de progression après chaque élément traité
            progress_bar.update(1)

    # Fermer la barre de progression après le traitement
    progress_bar.close()

    print("Le fichier travel_times.csv a été créé avec succès.")

if __name__ == "__main__":
    main()
