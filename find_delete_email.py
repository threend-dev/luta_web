import pytesseract
from PIL import Image

img = Image.open("assets/screenshots/9. 탈퇴/탈퇴실행.png")
data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT, lang='kor+eng')

words = []
for i in range(len(data['text'])):
    t = data['text'][i].strip()
    if t:
        words.append((t, data['left'][i], data['top'][i], data['width'][i], data['height'][i]))

# Print all text found around y=1000..1600
for w in words:
    if 1000 < w[2] < 1600:
        print(f"'{w[0]}' at (x={w[1]}, y={w[2]}, w={w[3]}, h={w[4]})")
