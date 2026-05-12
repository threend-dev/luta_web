import pytesseract
from PIL import Image
import json

img_path = "assets/screenshots/2. 홈화면/사이드메뉴.png"
img = Image.open(img_path)
data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)

results = []
for i in range(len(data['text'])):
    text = data['text'][i].strip()
    if text:
        results.append({
            'text': text,
            'left': data['left'][i],
            'top': data['top'][i],
            'width': data['width'][i],
            'height': data['height'][i]
        })
        if "aniham" in text.lower() or "naver.com" in text.lower():
            print(f"FOUND: {text} at ({data['left'][i]}, {data['top'][i]}, {data['width'][i]}, {data['height'][i]})")

