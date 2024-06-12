#Libraries
import sys
import os
import heapq
from time import time
import re
import queue
import psutil
from numpy import inf
from acapela_box import AcapelaBox
import pygame
from difflib import get_close_matches
ab = AcapelaBox()

#Functions
def trouver_numero_station(fichier, nom_station):
    try:
        # Ouvrir le fichier en mode lecture
        with open(fichier, 'r') as f:
            # Lire chaque ligne du fichier
            stations = {}
            for ligne in f:
                # Diviser la ligne en mots
                mots = ligne.lower().split()
                # Récupérer le numéro de la station et son nom
                numero_station = mots[0]
                nom = ' '.join(mots[1:]).lower()
                stations[nom] = numero_station
            
            # Vérifier si le nom de la station est exact
            if nom_station.lower() in stations:
                return int(stations[nom_station.lower()])
            else:
                # Trouver des correspondances proches
                matches = get_close_matches(nom_station, stations.keys())
                if matches:
                    return matches
                else:
                    return None
    except FileNotFoundError:
        print("Le fichier spécifié n'existe pas.")

def parse_data(data):
    stations = {}
    # Utilisation d'une expression régulière pour extraire les informations pertinentes
    pattern = re.compile(r"id:(\d+) - Station :<([^>]*)>")
    matches = pattern.findall(data)
    for match in matches:
        station_id = int(match[0])
        station_name = match[1].strip()
        if station_name not in stations:
            stations[station_name] = []
        stations[station_name].append(station_id)
        cles=stations.keys()
    # Convertir le dictionnaire en une chaîne de caractères JSON avec un encodage spécifique
    return str(list(cles))

def play_audio(file_path):
    # Initialiser pygame
    pygame.init()

    try:
        # Charger le fichier audio
        pygame.mixer.music.load(file_path)

        # Jouer l'audio
        pygame.mixer.music.play()

        # Attendre que l'audio se termine
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except pygame.error as e:
        print("Une erreur s'est produite :", e)

def read(txt:str):
    ls = ab.get_languages()
    vs = ab.get_voices("fr-FR")
    fs = ab.get_audioformats()
    language = ls[13]  # Francais
    voice = vs[8]  # Claire
    format = fs[0]  # MP3
    audiofile = "audio.mp3"
    print("Everything is ready to start!")
    ab.acabox_flashsession(text=txt, voice=voice['id'], audioformat=format['id'])
    resp = ab.dovaas(text=txt, voice=voice['id'], format=format['value'])
    result = ab.download_file(resp['snd_url'], audiofile)
    print("result", result)
    play_audio(audiofile)

def main():
    pass

if __name__=="__main__":
    main()
