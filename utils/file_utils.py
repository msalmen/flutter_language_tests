# utils/file_utils.py
import os
from datetime import datetime
import csv

def create_date_folder(base_path="screenshots"):
    os.makedirs(base_path, exist_ok=True)  # crea /screenshots si no existe
    today = datetime.now().strftime("%Y-%m-%d")
    full_path = os.path.join(base_path, today)
    os.makedirs(full_path, exist_ok=True)  # crea /screenshots/yyyy-mm-dd
    return full_path

def ensure_results_folder(path="results"):
    os.makedirs(path, exist_ok=True)
    return path

def log_result_to_csv(csv_path, data):
    file_exists = os.path.isfile(csv_path)
    with open(csv_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["archivo", "idioma_detectado", "idioma_esperado", "resultado", "fecha"])
        writer.writerow(data)
