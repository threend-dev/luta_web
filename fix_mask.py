from PIL import Image, ImageDraw

def precise_mask(img_path, box, is_dark_bg=False):
    img = Image.open(img_path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    
    # We sample the background color just outside the box
    # to blend it perfectly like the reference image likely did.
    sample_x = box[0] - 10
    sample_y = box[1] + (box[3] - box[1]) // 2
    
    bg_color = img.getpixel((sample_x, sample_y))
    
    # Paint over the box with the exact background color to make it disappear
    draw.rectangle(box, fill=bg_color)
    img.save(img_path)
    print(f"Masked {img_path} with color {bg_color}")

# 2. 홈화면/사이드메뉴.png
# In side menu, the profile usually has name and email at the top.
# Typically around y=200 to 350. Let's make a generous box.
# We should probably do a specific slice.
precise_mask("assets/screenshots/2. 홈화면/사이드메뉴.png", (200, 260, 800, 310))

# 9. 탈퇴/탈퇴실행.png 
# The modal in the middle showing "계정 (email@...) 탈퇴"
precise_mask("assets/screenshots/9. 탈퇴/탈퇴실행.png", (150, 1100, 1100, 1200))

