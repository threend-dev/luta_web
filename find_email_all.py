import pytesseract
from PIL import Image

img_path = "assets/screenshots/2. 홈화면/사이드메뉴.png"
img = Image.open(img_path)
data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)

for i in range(len(data['text'])):
    text = data['text'][i].strip()
    if text:
         print(f"TEXT: {text} at ({data['left'][i]}, {data['top'][i]}, {data['width'][i]}, {data['height'][i]})")
