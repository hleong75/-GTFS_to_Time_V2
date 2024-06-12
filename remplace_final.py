import pandas as pd
from tqdm import tqdm

def main():
    """
    Fonction principale pour charger les données des fichiers CSV, remplacer les noms d'arrêts par leurs IDs,
    puis sauvegarder les résultats dans un nouveau fichier CSV.

    Args:
        None

    Returns:
        None
    """
    # Charger les données des fichiers CSV
    travel_time_df = pd.read_csv('travel_times_with_names.csv')
    arrets_df = pd.read_csv('arrets.csv')

    # Créer un dictionnaire pour mapper les noms d'arrêts aux ID d'arrêts
    arrets_mapping = dict(zip(arrets_df['stop_name'], arrets_df['stop_id']))

    # Remplacer les noms d'arrêts par les ID d'arrêts dans travel_time_df
    travel_time_df['current_stop'] = travel_time_df['current_stop'].map(arrets_mapping)
    travel_time_df['next_stop'] = travel_time_df['next_stop'].map(arrets_mapping)

    # Suivi de la progression de la sauvegarde du fichier CSV
    with tqdm(total=1, desc="Sauvegarde du fichier CSV") as pbar:
        travel_time_df.to_csv('travel_time_updated.csv', index=False)
        pbar.update(1)

    print("Les colonnes current_stop et next_stop ont été mises à jour avec les IDs d'arrêts correspondants.")

if __name__ == "__main__":
    main()
