# main.py
import os
import time
from datetime import datetime
from appium import webdriver

from utils.ocr import extract_text
from utils.language_check import detect_language
from utils.file_utils import create_date_folder, ensure_results_folder, log_result_to_csv
from utils.android_locale import set_android_locale
from config.lang_config import load_lang_config

# Cargar configuración de idiomas desde JSON
lang_configs = load_lang_config()

# Crear carpetas necesarias
folder = create_date_folder()
results_folder = ensure_results_folder()
csv_path = os.path.join(results_folder, "lang_test_results.csv")

# Recorrer cada idioma configurado
for lang in lang_configs:
    lang_code = lang["code"]
    locale = lang["locale"]
    expected_keywords = lang["expected_keywords"]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    screenshot_name = f"home_{lang_code}.png"
    screenshot_path = os.path.join(folder, screenshot_name)

    print(f"\n🔁 Probando idioma: {lang_code} ({locale})")

    # Cambiar idioma del dispositivo
    # set_android_locale(locale)
    print(f"[⚠️] Salteando cambio de idioma (no soportado sin root en Android {API})")


    # Configurar Appium
    desired_caps = {
        "platformName": "Android",
        "deviceName": "Android",
        "automationName": "UiAutomator2",
        "appPackage": "com.tepydev.app/",  # ⚠️ Cambiar si corresponde
        "appActivity": "com.tepydev.app.MainActivity",
        "noReset": True
    }

    driver = None

    try:
        driver = webdriver.Remote("http://localhost:4723", desired_caps)
        time.sleep(5)
        driver.save_screenshot(screenshot_path)
        print(f"[📸] Captura guardada: {screenshot_path}")

        # OCR + limpieza
        texto_raw = extract_text(screenshot_path)
        texto = limpiar_texto_ocr(texto_raw)
        print(f"[🧹] Texto filtrado:\n{texto}\n")

        # Detección de idioma
        detected_lang = detect_language(texto)
        print(f"[🔤] Idioma detectado: {detected_lang}")

        # Validación por palabras clave
        missing = [kw for kw in expected_keywords if kw.lower() not in texto.lower()]
        if missing:
            print(f"[⚠️] Palabras clave faltantes: {missing}")
            resultado = "FAIL"
        else:
            resultado = "OK" if detected_lang == lang_code else "FAIL"

        log_result_to_csv(csv_path, [screenshot_name, detected_lang, lang_code, resultado, timestamp])
        print(f"[✅] Resultado final: {resultado}")

    except Exception as e:
        print(f"[❌] Error en idioma {lang_code}: {e}")
        log_result_to_csv(csv_path, [screenshot_name, "ERROR", lang_code, "ERROR", timestamp])

    finally:
        try:
            if driver:
                driver.quit()
        except:
            pass
