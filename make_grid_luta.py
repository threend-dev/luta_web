from PIL import Image, ImageDraw

img_path = "assets/screenshots/2. 홈화면/사이드메뉴.png"
img = Image.open(img_path).convert("RGBA")
draw = ImageDraw.Draw(img)

# We know LUTA and email are somewhere in the top half.
for y in range(400, 800, 20):
    draw.line((0, y, 600, y), fill="blue", width=1)
    draw.text((10, y), f"y={y}", fill="blue")

img.save("grid_luta.png")
