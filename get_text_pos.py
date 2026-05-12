import pytesseract
from PIL import Image

for img_path in ["assets/screenshots/2. 홈화면/사이드메뉴.png", "assets/screenshots/9. 탈퇴/탈퇴실행.png"]:
    try:
        img = Image.open(img_path)
        data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT, config='--psm 11')
        print(f"\nScanning: {img_path}")
        for i in range(len(data['text'])):
            text = data['text'][i].strip()
            if text:
                print(f"TEXT: '{text}' at ({data['left'][i]}, {data['top'][i]}, w={data['width'][i]}, h={data['height'][i]})")
    except Exception as e:
        pass
