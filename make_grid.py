from PIL import Image, ImageDraw

img_path = "assets/screenshots/2. 홈화면/사이드메뉴.png"
img = Image.open(img_path).convert("RGBA")
draw = ImageDraw.Draw(img)

# Draw grid lines for Y from 1000 to 1500 to check lower part
for y in range(1000, 1500, 50):
    draw.line((0, y, 1000, y), fill="blue", width=1)
    draw.text((10, y), f"y={y}", fill="blue")

img.save("grid_email_new.png")
