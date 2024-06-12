import pandas as pd
from tqdm import tqdm

def extract_stop_data(gtfs_file_path, output_csv_path):
    """
    Extract stop data from a GTFS file and save it to a CSV file.

    Parameters:
    - gtfs_file_path (str): The path to the GTFS file.
    - output_csv_path (str): The path to save the output CSV file.

    Returns:
    - None
    """
    # Charger les données des arrêts (stops) depuis le fichier GTFS
    stops_df = pd.read_csv(gtfs_file_path + 'stops.txt')

    # Sélectionner les colonnes stop_id et stop_name
    stop_data = stops_df[['stop_id', 'stop_name']]

    # Créer un objet tqdm pour afficher la progression
    progress_bar = tqdm(total=len(stop_data), desc="Extracting Stop Data")

    # Écrire les données dans un fichier CSV
    stop_data.to_csv(output_csv_path, index=False)

    # Mettre à jour la barre de progression
    progress_bar.update(len(stop_data))
    progress_bar.close()

def main():
    extract_stop_data('', 'arrets.csv')
    print(f"Fin d'extraction des arrets.")

if __name__ == "__main__":
    main()
