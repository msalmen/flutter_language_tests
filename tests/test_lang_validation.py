# tests/test_lang_validation.py
from appium import webdriver
import time
from datetime import datetime
from utils.ocr import extract_text
from utils.language_check import detect_language
from utils.file_utils import create_date_folder, ensure_results_folder, log_result_to_csv

# Configuraciones
expected_lang = "es"
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
folder = create_date_folder()
screenshot_name = "home_es.png"
screenshot_path = f"{folder}/{screenshot_name}"

results_folder = ensure_results_folder()
csv_path = f"{results_folder}/lang_test_results.csv"

# Capabilities
desired_caps = {
    "platformName": "Android",
    "deviceName": "Android",
    "automationName": "UiAutomator2",
    "appPackage": "com.tuapp.flutter",  # reemplazar con real
    "appActivity": ".MainActivity",
    "noReset": True
}

# Conexión Appium
driver = webdriver.Remote("http://localhost:4723", desired_caps)
time.sleep(5)

# Captura
driver.save_screenshot(screenshot_path)
print(f"[INFO] Captura guardada: {screenshot_path}")
driver.quit()

# OCR + Detección de idioma
text = extract_text(screenshot_path)
detected_lang = detect_language(text)
print(f"[INFO] Idioma detectado: {detected_lang}")

# Validación
resultado = "OK" if detected_lang == expected_lang else "FAIL"
log_result_to_csv(csv_path, [screenshot_name, detected_lang, expected_lang, resultado, timestamp])
print(f"[RESULTADO] {resultado} — Registrado en {csv_path}")
