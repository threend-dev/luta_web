from PIL import Image, ImageFilter

def apply_blur_mask(img_path, box, radius=15):
    try:
        img = Image.open(img_path).convert("RGBA")
        cropped = img.crop(box)
        blurred = cropped.filter(ImageFilter.GaussianBlur(radius))
        img.paste(blurred, box)
        img.save(img_path)
        print(f"✅ Applied blur to {img_path} at {box}")
    except Exception as e:
        print(f"Error processing {img_path}: {e}")

box_email_sidebar = (45, 575, 480, 630)
apply_blur_mask("assets/screenshots/2. 홈화면/사이드메뉴.png", box_email_sidebar)

# We want to blur the (aniham@naver.com) part. Assuming standard iOS modal.
# Center of the modal is around y=1180.
# Box covering from x=200 to x=1080 (enough to cover `aniham@naver.com`), y=1160 to 1250
box_email_modal = (350, 1170, 950, 1260)
apply_blur_mask("assets/screenshots/9. 탈퇴/탈퇴실행.png", box_email_modal)
