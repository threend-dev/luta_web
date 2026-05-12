from PIL import Image, ImageFilter

def apply_blur_mask(img_path, box, radius=20):
    try:
        img = Image.open(img_path).convert("RGBA")
        cropped = img.crop(box)
        blurred = cropped.filter(ImageFilter.GaussianBlur(radius))
        img.paste(blurred, box)
        img.save(img_path)
        print(f"Applied blur to {img_path} at {box}")
    except Exception as e:
        print(f"Error processing {img_path}: {e}")

box_email = (80, 710, 500, 760)

apply_blur_mask("assets/screenshots/2. 홈화면/사이드메뉴.png", box_email)
apply_blur_mask("assets/screenshots/9. 탈퇴/탈퇴실행.png", box_email)
