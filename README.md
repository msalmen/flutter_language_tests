✅ README.md completo
markdown
Copiar
Editar
# 🧪 flutter_language_tests

Automatización de pruebas visuales para verificar que una app Flutter muestre correctamente los textos localizados según el idioma configurado en el sistema operativo.

---

## 📌 Objetivo

Validar automáticamente que los textos en la interfaz de usuario se correspondan con el idioma esperado, usando:

- Appium para control del dispositivo
- OCR (Tesseract) para extraer texto de capturas
- Python para scripting y automatización

---

## ⚙️ Requisitos

- Python 3.10 o superior
- Tesseract OCR (instalado en Windows)
- Appium v2
- Android SDK configurado
- Dispositivo Android (físico o emulado) con la app instalada
- Git

---

## 🛠️ Instalación del entorno

1. **Clonar el repositorio**

```bash
git clone https://github.com/tuusuario/flutter_language_tests.git
cd flutter_language_tests
Crear y activar entorno virtual

bash
Copiar
Editar
python -m venv .venv
.\.venv\Scripts\activate
Instalar dependencias

bash
Copiar
Editar
pip install -r requirements.txt
Instalar Appium CLI y driver

bash
Copiar
Editar
npm install -g appium
appium driver install uiautomator2
Instalar Tesseract OCR (si no lo hiciste)
Descargar desde: https://github.com/UB-Mannheim/tesseract/wiki
Y asegurarse de que esté en PATH o configurado manualmente en utils/ocr.py.

🚀 Cómo correr pruebas
1. Iniciar Appium
bash
Copiar
Editar
appium
Dejalo corriendo en una terminal.

2. Ejecutar una prueba de idioma
bash
Copiar
Editar
python main_single.py
Esto tomará una captura de pantalla y verificará que las palabras clave del idioma es estén presentes.

3. Ver resultados
Los resultados se guardan automáticamente en:

📸 screenshots/YYYY-MM-DD/

📄 results/lang_test_results.csv

📁 Estructura del proyecto
bash
Copiar
Editar
flutter_language_tests/
├── main.py                 # Ejecuta pruebas para todos los idiomas del JSON
├── main_single.py          # Ejecuta una sola prueba
├── config/
│   ├── lang_config.json    # Configuración de idiomas y palabras clave
│   └── lang_config.py
├── utils/
│   ├── ocr.py              # OCR con Tesseract
│   ├── file_utils.py       # Carpetas, fechas, CSV
│   ├── android_locale.py   # Cambia idioma con adb (requiere root)
│   └── language_check.py   # Detección automática de idioma
├── screenshots/            # Capturas organizadas por fecha
├── results/                # Resultados de ejecución
└── requirements.txt
📌 Sistema de versiones
Usamos SemVer (MAJOR.MINOR.PATCH) y etiquetas Git:

v1.0.0: Primer versión funcional con pruebas OCR en un idioma

v1.1.0: Soporte multilenguaje desde archivo JSON

v1.2.0: Inclusión de logs en CSV y estructura de carpetas automática

v1.3.0: Pruebas visuales completas con OCR sin filtros

v1.4.0: Soporte opcional para HTML resumen visual (pendiente)

Usar git tag vX.X.X -m "Descripción" + git push origin --tags

🛣️ Roadmap
 OCR funcional con Appium

 Screenshot + validación de idioma

 Registro automático en CSV

 Reporte en HTML con enlaces a capturas

 Soporte a múltiples resoluciones y layouts

 UI para configurar idiomas a testear

 Fuzzy matching opcional para tolerar errores OCR

🧑‍💻 Contribución
Podés abrir issues o pull requests con mejoras. Todo está estructurado para ser progresivamente expandido.

🧠 Autor
Mauricio Salmen
Tester QA | Automación | Apps móviles | OCR aplicado a localización