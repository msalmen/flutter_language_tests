from appium import webdriver
import time

desired_caps = {
    "platformName": "Android",
    "deviceName": "Android",  # o el nombre exacto de tu dispositivo si lo necesitás
    "automationName": "UiAutomator2",
    "appPackage": "com.google.android.apps.nexuslauncher",  # ← Cambiar por el real
    "appActivity": "com.google.android.apps.nexuslauncher.NexusLauncherActivity",  # ← Cambiar por el real
    "noReset": True
}

driver = webdriver.Remote("http://localhost:4723", desired_caps)

print("[INFO] Conexión exitosa con el dispositivo")

time.sleep(5)
driver.quit()
