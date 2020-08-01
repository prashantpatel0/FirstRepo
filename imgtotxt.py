from PIL import Image
import pytesseract 
from pytesseract import image_to_string 
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
captcha_text = image_to_string(Image.open('captcha.jpg'),lang='eng')

