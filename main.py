import pandas as pd
import os
import remplace
import remplace_times
import remplace_name_to_numb
import remplace_final
import mise_en_forme
import doublons
import add_transfers
import stops
import temps
import voisins
import MiseEnForme_pour_graphe
import remplace_graphe

def main():
    voisins.main()
    temps.main()
    stops.main()
    add_transfers.main()
    doublons.main()
    remplace_times.main()
    remplace.main()
    remplace_name_to_numb.main()
    remplace_final.main()
    mise_en_forme.main() #Pour utiliser https://github.com/BTajini/Paris-Metro-Project
    remplace_graphe.main()
    MiseEnForme_pour_graphe.main()

def supprimer_fichiers(dossier):
    # Parcourir tous les fichiers dans le répertoire
    for fichier in os.listdir(dossier):
        chemin_complet = os.path.join(dossier, fichier)
        
        # Vérifier si c'est un fichier et si son extension est .csv ou s'il s'appelle neighbors.txt
        if os.path.isfile(chemin_complet) and (fichier.endswith('.csv') or fichier.endswith('.py') or fichier == 'neighbors.txt'):
            try:
                os.remove(chemin_complet)
                print(f"Supprimé : {chemin_complet}")
            except Exception as e:
                print(f"Erreur lors de la suppression de {chemin_complet} : {e}")


if __name__=="__main__":
    main()
    dossier = os.path.dirname(os.path.abspath(__file__))
    supprimer_fichiers(dossier)
