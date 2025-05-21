# utils/ocr.py
# verify_ocr.py
import pytesseract
import cv2
import os


# Ruta manual si no está en el PATH
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def verificar_tesseract():
    try:
        version = pytesseract.get_tesseract_version()
        print(f"[✅] Tesseract instalado correctamente: {version}")
    except Exception as e:
        print(f"[❌] Tesseract no encontrado: {e}")
        return False
    return True

def probar_ocr_con_ejemplo():
    sample_image = "sample_text.png"

    if not os.path.exists(sample_image):
        print(f"[⚠️] No se encontró la imagen {sample_image}")
        return

    print(f"[🔍] Procesando imagen: {sample_image}")
    img = cv2.imread(sample_image)
    texto_raw = pytesseract.image_to_string(img)

    texto_limpio = limpiar_texto_ocr(texto_raw)

    print("[📄] Texto detectado por OCR (filtrado):")
    print("–––––––––––––––––––––––––––––––––")
    print(texto_limpio.strip())
    print("–––––––––––––––––––––––––––––––––")

if __name__ == "__main__":
    if verificar_tesseract():
        probar_ocr_con_ejemplo()


def extract_text(image_path):
    img = cv2.imread(image_path)
    text = pytesseract.image_to_string(img)
    return text