import pytesseract
from PIL import Image

data = pytesseract.image_to_data(Image.open("assets/screenshots/9. 탈퇴/탈퇴실행.png"), output_type=pytesseract.Output.DICT, lang='kor+eng', config='--psm 11')
for i in range(len(data['text'])):
    t = data['text'][i].strip()
    left = data['left'][i]
    top = data['top'][i]
    if len(t) > 2 and (not t.isdigit()):
        print(f"TEXT: '{t}' at ({left}, {top}, w={data['width'][i]}, h={data['height'][i]})")
