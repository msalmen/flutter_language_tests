# utils/android_locale.py
import subprocess
import time

def set_android_locale(locale_code):
    print(f"[ADB] Cambiando idioma a: {locale_code}")
    try:
        subprocess.run(
            f'adb shell "setprop persist.sys.locale {locale_code}; setprop ctl.restart zygote"',
            shell=True,
            check=True,
        )
        print("[ADB] Reinicio iniciado... Esperando 20 segundos.")
        time.sleep(20)  # esperar reinicio
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] No se pudo cambiar el idioma: {e}")
