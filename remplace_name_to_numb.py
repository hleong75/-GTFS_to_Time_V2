import pandas as pd
from tqdm import tqdm

def replace_stop_id_with_numbers(filename):
    """
    Replace stop IDs in a CSV file with zero-padded line numbers.

    Parameters:
    - filename (str): The name of the CSV file.

    Returns:
    - None
    """
    # Charge le fichier CSV dans un DataFrame pandas
    df = pd.read_csv(filename)

    # Crée un objet tqdm pour afficher la progression
    progress_bar = tqdm(total=len(df), desc="Processing")

    # Remplace les valeurs dans la colonne 'stop_id' par des numéros de ligne remplis de zéros à gauche
    df['stop_id'] = df.index.map(lambda x: str(x).zfill(4))
    
    # Met à jour la barre de progression
    progress_bar.update(len(df))

    # Écrit le DataFrame modifié dans le fichier CSV
    df.to_csv(filename, index=False)
    progress_bar.close()

def main():
    replace_stop_id_with_numbers('arrets.csv')
    print(f"Fin du remplacement de stop_id par des chiffres.")

if __name__=="__main__":
    # Remplacez 'arrets.csv' par le nom de votre fichier
    main()
