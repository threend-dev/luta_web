from PIL import Image, ImageDraw

def mask_area(img_path, box, out_path):
    # box = (left, top, right, bottom)
    img = Image.open(img_path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    # Draw a dark gray rectangle over the specified box
    draw.rectangle(box, fill=(50, 50, 50, 255))
    
    img.save(out_path)
    print(f"✅ Saved masked mask for {img_path}")

# 이메일 영역의 좌표 (x_start, y_start, x_end, y_end)를 설정합니다.
# 아이폰 해상도 (1290 x 2796) 기준 대략적인 프로필/탈퇴 정보 위치
box_sidebar = (200, 250, 900, 350)  # 사이드메뉴 이메일 추정 위치
box_delete = (150, 1000, 1050, 1200) # 탈퇴 모달의 이메일 추정 위치

# 덮어쓰기 합니다.
mask_area("assets/screenshots/0. 초기화면/실행화면.png", box_sidebar, "assets/screenshots/0. 초기화면/실행화면.png")
mask_area("assets/screenshots/9. 탈퇴/탈퇴실행.png", box_delete, "assets/screenshots/9. 탈퇴/탈퇴실행.png")

