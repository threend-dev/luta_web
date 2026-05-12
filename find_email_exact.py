from PIL import Image
import pytesseract

img_path = "assets/screenshots/2. 홈화면/사이드메뉴.png"
img = Image.open(img_path)

data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)

print("Searching for LUTA or email...")
for i in range(len(data['text'])):
    text = data['text'][i].strip()
    if text:
        print(f"TEXT: '{text}' at ({data['left'][i]}, {data['top'][i]}, w={data['width'][i]}, h={data['height'][i]})")

