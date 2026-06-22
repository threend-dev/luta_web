import re

html_file = 'views/features.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # 01 로그인 회원가입
    (r'<div class="screenshot-placeholder">\s*<span>로그인 화면<br>캡쳐 이미지</span>\s*</div>', 
     '<img src="../assets/screenshots/1. %ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%20%EB%B0%8F%20%EB%A1%9C%EA%B7%B8%EC%9D%B8/%EB%A1%9C%EA%B7%B8%EC%9D%B8.png" alt="로그인 화면" style="width: 100%; height: auto; border-radius: 8px;">'),
    (r'<div class="screenshot-placeholder">\s*<span>회원가입 화면<br>캡쳐 이미지</span>\s*</div>', 
     '<img src="../assets/screenshots/1. %ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%20%EB%B0%8F%20%EB%A1%9C%EA%B7%B8%EC%9D%B8/%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85.png" alt="회원가입 화면" style="width: 100%; height: auto; border-radius: 8px;">'),
    
    # 02 홈 화면
    (r'<div class="screenshot-placeholder">\s*<span>홈 화면<br>캡쳐 이미지</span>\s*</div>',
     '<img src="../assets/screenshots/2. %ED%99%88%ED%99%94%EB%A9%B4/%EB%A9%94%EC%9D%B8%EB%A9%94%EB%89%B4.png" alt="홈 화면" style="width: 100%; height: auto; border-radius: 8px;">'),
    
    # 03 팀 관리
    (r'<div class="screenshot-placeholder">\s*<span>팀 목록 화면<br>캡쳐 이미지</span>\s*</div>',
     '<img src="../assets/screenshots/3. %ED%8C%80%EA%B4%80%EB%A6%AC/%ED%8C%80%EB%93%B1%EB%A1%9D.png" alt="팀 목록 화면" style="width: 100%; height: auto; border-radius: 8px;">'),
    (r'<div class="screenshot-placeholder">\s*<span>팀 상세 화면<br>캡쳐 이미지</span>\s*</div>',
     '<img src="../assets/screenshots/3. %ED%8C%80%EA%B4%80%EB%A6%AC/%EC%84%A0%EC%88%98%EC%B6%94%EA%B0%80.png" alt="팀 상세 화면" style="width: 100%; height: auto; border-radius: 8px;">'),
    (r'<div class="screenshot-placeholder">\s*<span>팀 코드 공유<br>캡쳐 이미지</span>\s*</div>',
     '<img src="../assets/screenshots/3. %ED%8C%80%EA%B4%80%EB%A6%AC/%ED%8C%80%EA%B0%80%EC%9E%85%EC%BD%94%EB%93%9C.png" alt="팀 코드 공유" style="width: 100%; height: auto; border-radius: 8px;">'),
    
    # 04 라인업
    (r'<div class="screenshot-placeholder">\s*<span>라인업 편성 화면<br>캡쳐 이미지</span>\s*</div>',
     '<img src="../assets/screenshots/4. %EB%9D%BC%EC%9D%B8%EC%97%업/%EB%9D%BC%EC%9D%B8%EC%97%업.png" alt="라인업 편성 화면" style="width: 100%; height: auto; border-radius: 8px;">'),
    (r'<div class="screenshot-placeholder">\s*<span>포지션 선택<br>캡쳐 이미지</span>\s*</div>',
     '<img src="../assets/screenshots/4. %EB%9D%BC%EC%9D%B8%EC%97%업/%ED%8F%AC%EC%A7%80%EC%85%98%EB%B3%80%EA%B2%BD.png" alt="포지션 선택" style="width: 100%; height: auto; border-radius: 8px;">'),
    
    # 05 경기장
    (r'<div class="screenshot-placeholder">\s*<span>경기장 메인 화면<br>캡쳐 이미지</span>\s*</div>',
     '<img src="../assets/screenshots/5. %EA%B2%BD%EA%B8%B0%EC%9E%A5/%EA%B2%BD%EA%B8%B0%EC%8B%9C%EC%9E%91.png" alt="경기장 메인 화면" style="width: 100%; height: auto; border-radius: 8px;">'),
    (r'<div class="screenshot-placeholder">\s*<span>이닝 기록 화면<br>캡쳐 이미지</span>\s*</div>',
     '<img src="../assets/screenshots/5. %EA%B2%BD%EA%B8%B0%EC%9E%A5/%EB%93%9D%EC%A0%90%ED%83%80%EA%B2%A9.png" alt="이닝 기록 화면" style="width: 100%; height: auto; border-radius: 8px;">'),
    (r'<div class="screenshot-placeholder">\s*<span>타석 결과 입력<br>캡쳐 이미지</span>\s*</div>',
     '<img src="../assets/screenshots/5. %EA%B2%BD%EA%B8%B0%EC%9E%A5/%ED%83%80%EA%B2%A9%EC%B2%98%EB%A6%AC.png" alt="타석 결과 입력" style="width: 100%; height: auto; border-radius: 8px;">'),
    (r'<div class="screenshot-placeholder">\s*<span>태블릿 가로 모드<br>캡쳐 이미지</span>\s*</div>',
     '<img src="../assets/screenshots/5. %EA%B2%BD%EA%B8%B0%EC%9E%A5/%EC%88%98%EB%B9%84%EA%B5%90%EC%B2%B4.png" alt="태블릿 가로 모드" style="width: 100%; height: auto; border-radius: 8px;">'),
    
    # 06 경기 결과 (임시로 기록실 사진 활용 또는 그냥 두기)
    (r'<div class="screenshot-placeholder">\s*<span>경기 결과 목록<br>캡쳐 이미지</span>\s*</div>',
     '<img src="../assets/screenshots/7. %EA%B8%B0%EB%A1%9D%EC%8B%A4/%ED%99%88%EA%B8%B0%EB%A1%9D.png" alt="경기 결과 목록" style="width: 100%; height: auto; border-radius: 8px;">'),
    (r'<div class="screenshot-placeholder">\s*<span>경기 상세 정보<br>캡쳐 이미지</span>\s*</div>',
     '<img src="../assets/screenshots/7. %EA%B8%B0%EB%A1%9D%EC%8B%A4/%EC%9B%90%EC%A0%95%EA%B8%B0%EB%A1%9D.png" alt="경기 상세 정보" style="width: 100%; height: auto; border-radius: 8px;">'),
    
    # 07 기록실
    (r'<div class="screenshot-placeholder">\s*<span>기록실 화면<br>캡쳐 이미지</span>\s*</div>',
     '<img src="../assets/screenshots/7. %EA%B8%B0%EB%A1%9D%EC%8B%A4/%ED%99%88%EA%B8%B0%EB%A1%9D.png" alt="기록실 화면" style="width: 100%; height: auto; border-radius: 8px;">'),
    
    # 08 설정
    (r'<div class="screenshot-placeholder">\s*<span>설정 화면<br>캡쳐 이미지</span>\s*</div>',
     '<img src="../assets/screenshots/8. %EC%84%A4%EC%A0%95/%EC%84%A4%EC%A0%95%EC%B4%88%EA%B8%B0.png" alt="설정 화면" style="width: 100%; height: auto; border-radius: 8px;">'),
    (r'<div class="screenshot-placeholder">\s*<span>테마 설정<br>캡쳐 이미지</span>\s*</div>',
     '<img src="../assets/screenshots/8. %EC%84%A4%EC%A0%95/%EB%A7%88%EC%BB%A4%EC%84%A4%EC%A0%95.png" alt="테마 설정" style="width: 100%; height: auto; border-radius: 8px;">'),
]

for old, new in replacements:
    content = re.sub(old, new, content, flags=re.IGNORECASE)

# Fix URL encoded hangul for 라인업
content = content.replace('%EB%9D%BC%EC%9D%B8%EC%97%업', '%EB%9D%BC%EC%9D%B8%EC%97%85')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

