import sys
from PIL import Image

# Let's inspect the center-ish area of the reference image to see what color the text was masked with
ref = Image.open("assets/screenshots/1. 회원가입 및 로그인/인증요청.png").convert("RGB")
img_tar1 = Image.open("assets/screenshots/2. 홈화면/사이드메뉴.png").convert("RGB")

# We can just blind out the email in side menu and delete screen
# We just need to know the bounding box and fill it with background color or gray color.
print("We can try applying a clean mask...")
