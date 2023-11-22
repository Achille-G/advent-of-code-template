import importlib
import os

def solution_for_day(day, input_data, part):
    try:
        # Importe dynamiquement le module de solution pour le jour donné
        solution_module = importlib.import_module(f".day{day}", "solutions")
    except ImportError:
        raise ImportError(f"No solution module found for day {day}")

    # Appelle la fonction solve du module importé
    return solution_module.solve(input_data, part)