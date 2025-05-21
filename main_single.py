# main_single.py
import os
import time
from datetime import datetime
from appium import webdriver

from utils.ocr import extract_text
from utils.language_check import detect_language
from utils.file_utils import create_date_folder, ensure_results_folder, log_result_to_csv
from config.lang_config import load_lang_config

# Idioma a testear
lang_code = "es"

# Buscar el idioma en el JSON
lang_config = next((lang for lang in load_lang_config() if lang["code"] == lang_code), None)

if not lang_config:
    raise ValueError(f"[❌] No se encontró configuración para el idioma '{lang_code}' en lang_config.json")

expected_keywords = lang_config["expected_keywords"]

# Rutas
folder = create_date_folder()
results_folder = ensure_results_folder()
csv_path = os.path.join(results_folder, "lang_test_results.csv")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
screenshot_name = f"home_{lang_code}.png"
screenshot_path = os.path.join(folder, screenshot_name)

# Configuración Appium
desired_caps = {
    "platformName": "Android",
    "deviceName": "Android",
    "automationName": "UiAutomator2",
    "appPackage": "com.tepydev.app",  # ⚠️ Ajustar si cambia
    "appActivity": "com.tepydev.app.MainActivity",  # ⚠️ sin punto
    "noReset": True
}

driver = None

try:
    print(f"\n🔁 Ejecutando test para idioma: {lang_code}")
    driver = webdriver.Remote("http://localhost:4723", desired_caps)
    time.sleep(5)
    driver.save_screenshot(screenshot_path)
    print(f"[ 📸 ] Captura guardada: {screenshot_path}")

    texto_raw = extract_text(screenshot_path)
    texto = extract_text(screenshot_path)
    print(f"[ 📄 ] Texto OCR completo:\n{texto}\n")


    detected_lang = detect_language(texto)
    print(f"[ 🔤 ] Idioma detectado por OCR: {detected_lang}")

    missing = [kw for kw in expected_keywords if kw.lower() not in texto.lower()]
    if missing:
        print(f"[ ⚠️ ] Palabras clave faltantes: {missing}")
        resultado = "FAIL"
    else:
        resultado = "OK" if detected_lang == lang_code else "FAIL"

    log_result_to_csv(csv_path, [screenshot_name, detected_lang, lang_code, resultado, timestamp])
    if resultado == "OK":
        print(f"[ ✅ ] Resultado final: {resultado}")
    elif resultado == "FAIL":
        print(f"[ ❌ ] Resultado final: {resultado}")
    else:
        print(f"[ ⚠️ ] Resultado final: {resultado}")


except Exception as e:
    print(f"[ ❌ ] Fallo el test para idioma {lang_code}: {e}")
    log_result_to_csv(csv_path, [screenshot_name, "ERROR", lang_code, "ERROR", timestamp])

finally:
    try:
        if driver:
            driver.quit()
    except:
        pass
