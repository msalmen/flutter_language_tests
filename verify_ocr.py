# verify_ocr.py
import os
import pytesseract
import cv2

# (opcional) Seteo explícito de ruta si no está en el PATH:
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
    # Ruta de imagen de prueba (podés reemplazar esto por la tuya)
    sample_image = "sample_text.png"

    if not os.path.exists(sample_image):
        print(f"[⚠️] No se encontró la imagen {sample_image}")
        return

    print(f"[🔍] Procesando imagen: {sample_image}")
    img = cv2.imread(sample_image)
    text = pytesseract.image_to_string(img)
    print("[📄] Texto detectado por OCR:")
    print("–––––––––––––––––––––––––––––––––")
    print(text.strip())
    print("–––––––––––––––––––––––––––––––––")

if __name__ == "__main__":
    if verificar_tesseract():
        probar_ocr_con_ejemplo()
