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

# The user stated the location in both screens is the same. 
# Re-using the same box as side menu: (45, 575, 480, 630)
box_email_same = (45, 575, 480, 630)
apply_blur_mask("assets/screenshots/9. 탈퇴/탈퇴실행.png", box_email_same)
