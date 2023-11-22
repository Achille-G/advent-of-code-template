import requests
import os
from dotenv import load_dotenv

load_dotenv()
SESSION_COOKIE = os.getenv('SESSION_COOKIE')

def get_input(day, test=False):
    day_folder = f"inputs/day{day}"
    os.makedirs(day_folder, exist_ok=True)  # Crée le dossier s'il n'existe pas

    filename = os.path.join(day_folder, f"{'test' if test else 'input'}.txt")
    
    # Essayez d'abord de charger l'input depuis un fichier local
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        if test:
            # Si c'est un fichier de test et qu'il n'existe pas, créez un fichier vide
            with open(filename, "w") as file:
                pass
            print(f"Créé un fichier de test vide: {filename}")
            return ""
        else:
            # Si le fichier n'existe pas et que ce n'est pas un test, téléchargez l'input
            url = f"https://adventofcode.com/2022/day/{day}/input"
            cookies = {'session': SESSION_COOKIE}
            response = requests.get(url, cookies=cookies)

            if response.status_code == 200:
                input_data = response.text
                with open(filename, "w") as file:
                    file.write(input_data)
                return input_data
            else:
                print(f"Erreur lors du téléchargement de l'input pour le jour {day}: {response.status_code}")
                return None