from tqdm import tqdm

def remove_first_line(file_path):
    """
    Supprime la première ligne d'un fichier.

    Args:
        file_path (str): Le chemin du fichier à modifier.

    Returns:
        None
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    with open(file_path, 'w') as file:
        file.writelines(lines[1:])

def replace_commas_with_spaces(file_path):
    """
    Remplace toutes les virgules par des espaces dans un fichier.

    Args:
        file_path (str): Le chemin du fichier à modifier.

    Returns:
        None
    """
    with open(file_path, 'r') as file:
        content = file.read()
    
    content = content.replace(',', ' ')
    
    with open(file_path, 'w') as file:
        file.write(content)

def main():
    """
    Fonction principale pour supprimer la première ligne de 'travel_time_updated.csv' et 'arrets.csv',
    et remplacer les virgules par des espaces dans 'arrets.csv'.

    Args:
        None

    Returns:
        None
    """
    # Suivi de la suppression de la première ligne dans 'travel_time_updated.csv'
    with tqdm(total=1, desc="Suppression de la première ligne de travel_time_updated.csv") as pbar:
        remove_first_line("travel_time_updated.csv")
        pbar.update(1)

    # Suivi de la suppression de la première ligne et du remplacement des virgules par des espaces dans 'arrets.csv'
    with tqdm(total=2, desc="Traitement de arrets.csv") as pbar:
        remove_first_line("arrets.csv")
        pbar.update(1)
        replace_commas_with_spaces("arrets.csv")
        pbar.update(1)

    print("La première ligne des fichiers a été supprimée avec succès, et les virgules ont été remplacées par des espaces dans arrets.csv.")

if __name__ == "__main__":
    main()
