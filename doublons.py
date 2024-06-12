import csv
import os
from tqdm import tqdm

def check_duplicate(stop_name, D):
    if stop_name in D:
        return True
    return False

def add_suffix(stop_name, D):
    i = 2
    new_stop_name = stop_name
    if stop_name not in D:
        D[stop_name]=True
        return stop_name
    else:
        while check_duplicate(new_stop_name, D):
            new_stop_name = f"{stop_name} {i}"
            i += 1
        D[new_stop_name]=True
        return new_stop_name

def main():
    D={}
    filename = "arrets.csv"
    new_filename = "arrets.csv"
    stops = []
    print(f"Lecture de {filename} en cours...")
    # Read existing stops
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        total_rows = sum(1 for _ in csvfile)  # Compte le nombre total de lignes pour la barre de progression
        csvfile.seek(0)  # Réinitialise le curseur du fichier après le comptage

        # Ajoute tqdm à la boucle
        for row in tqdm(reader, total=total_rows, desc="Lecture des lignes CSV"):
            stops.append(row)
            
    print(f"Mise à jour des noms en cours...")
    # Update stop names
    for stop in tqdm(stops, desc="Mise à jour des noms des arrêts"):
        stop['stop_name'] = add_suffix(stop['stop_name'], D)
        
    print(f"Ecriture de {filename} en cours...")
    # Write updated stops to new file
    with open(new_filename, 'w', newline='') as csvfile:
        fieldnames = ['stop_id', 'stop_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        # Ajoute tqdm à la boucle
        for stop in tqdm(stops, desc="Écriture des arrêts dans le fichier CSV"):
            writer.writerow(stop)

    print(f"Fin de l'écriture du fichier {new_filename}.")

if __name__ == "__main__":
    main()
