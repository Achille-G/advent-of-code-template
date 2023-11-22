# advent-of-code-template

Ce projet contient mes solutions pour les défis de programmation de [Advent of Code](https://adventofcode.com/). Il est structuré pour faciliter l'ajout et le test de nouvelles solutions au fil des jours.

## Structure du Projet

- `main.py` : Le script principal pour exécuter les solutions.
- `input_manager.py` : Gère le chargement des données d'entrée, soit localement, soit en les téléchargeant depuis Advent of Code.
- `solutions/` : Contient des sous-dossiers pour chaque jour avec des scripts spécifiques pour chaque problème.
- `inputs/` : Dossiers organisés par jour contenant les fichiers d'input et de test.
- `utils.py` : Fonctions utilitaires pour le parsing et d'autres opérations communes.
- `.env` : Contient des variables d'environnement (comme le cookie de session pour Advent of Code).

## Configuration

1. **Installation des Dépendances** : Exécutez `pip install -r requirements.txt` pour installer les dépendances nécessaires.
2. **Cookie de Session** : Placez votre cookie de session Advent of Code dans un fichier `.env` à la racine du projet sous la forme `SESSION_COOKIE=votre_cookie_de_session`.
3. **Note :** Pensez à modifier l'année dans `input_manager.py` selon l'année du défi d'Advent of Code auquel vous participez.(exemple:2022)

## Utilisation

Pour exécuter une solution :

```bash
python main.py [numéro du jour] [numéro de la partie] [--test]
```

- `[numéro du jour]` : Le jour du défi (ex : 1, 2, 3, ...).
- `[numéro de la partie]` : La partie du défi (1 ou 2).
- `--test` : Optionnel. Utilisez-le pour exécuter la solution avec le fichier d'input de test.

## Ajouts de Nouvelles Solutions

1. Créez un nouveau script dans solutions/dayX/ pour le jour X.
2. Implémentez les fonctions de solution solve_part1 et solve_part2 dans ce script.
3. Testez votre solution en utilisant les fichiers d'input de test et les fichiers d'input réels.
