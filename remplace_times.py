import pandas as pd
from tqdm import tqdm

def replace_stop_names(travel_times_file, stops_file):
    """
    Replace stop IDs with stop names in a travel times DataFrame.

    Parameters:
    - travel_times_file (str): The filename of the travel times CSV file.
    - stops_file (str): The filename of the stops CSV file.

    Returns:
    - None
    """
    # Charger les fichiers CSV en tant que DataFrames
    travel_times_df = pd.read_csv(travel_times_file)
    stops_df = pd.read_csv(stops_file)

    # Créer un dictionnaire pour mapper les identifiants d'arrêt à leurs noms correspondants
    stop_id_to_name = dict(zip(stops_df['stop_id'], stops_df['stop_name']))

    # Créer des objets tqdm pour afficher la progression
    progress_bar_1 = tqdm(total=len(travel_times_df), desc="Processing Travel Times")
    progress_bar_2 = tqdm(total=len(travel_times_df), desc="Processing Stops")

    # Remplacer les identifiants d'arrêt par les noms d'arrêt dans travel_times_df
    travel_times_df['current_stop'] = travel_times_df['current_stop'].map(lambda x: stop_id_to_name.get(x, x))
    travel_times_df['next_stop'] = travel_times_df['next_stop'].map(lambda x: stop_id_to_name.get(x, x))

    # Mettre à jour la première barre de progression
    progress_bar_1.update(len(travel_times_df))
    progress_bar_1.close()

    # Mettre à jour la deuxième barre de progression
    progress_bar_2.update(len(stops_df))
    progress_bar_2.close()

    # Enregistrer le DataFrame modifié dans un nouveau fichier CSV
    travel_times_df.to_csv('travel_times_with_names.csv', index=False)

def main():
    travel_times_file = 'travel_times.csv'
    stops_file = 'arrets.csv'
    replace_stop_names(travel_times_file, stops_file)

if __name__ == "__main__":
    main()
