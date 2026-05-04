from PIL import Image, ImageFilter

def apply_blur_mask(img_path, box, radius=10):
    img = Image.open(img_path).convert("RGBA")
    
    # Crop the area we want to blur
    cropped = img.crop(box)
    
    # Apply Gaussian blur
    blurred = cropped.filter(ImageFilter.GaussianBlur(radius))
    
    # Paste it back
    img.paste(blurred, box)
    
    img.save(img_path)
    print(f"Applied blur to {img_path} at {box}")

# The user mentioned the email is directly under the 'LUTA' text in the side menu.
# For side menu (1290x2796), LUTA text is probably around y=200. Email should be around y=300 to y=400.
# Assuming x is around 250 to 900. Let's make an educated guess.
# Side menu box: LUTA 글자 바로 아래. 
box_sidebar = (200, 310, 850, 380)

# 탈퇴실행 화면에도 LUTA 글자가 있다고 했거나, 적어도 동일한 위치의 사이드메뉴가 열려있거나 아니면 모달 화면임.
# "위치는 동일하게 사이드메뉴 열었을때 LUTA 글자 바로 아래의 이메일 적힌 위치임"
# This means both screens have the exact same side-menu open, and the email is at the same exact pixel coordinates.
box_delete = (200, 310, 850, 380)

apply_blur_mask("assets/screenshots/2. 홈화면/사이드메뉴.png", box_sidebar, radius=15)
apply_blur_mask("assets/screenshots/9. 탈퇴/탈퇴실행.png", box_delete, radius=15)

