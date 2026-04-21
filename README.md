# BaseBall Book Web

BaseBall Book 앱의 소개 및 안내 웹페이지입니다.

## 구조

```
baseball_book_web/
├── index.html              # 메인 HTML (SPA)
├── css/
│   ├── style.css           # 메인 스타일
│   └── responsive.css      # 반응형 스타일
├── js/
│   └── app.js              # SPA 라우터 & 인터랙션
├── assets/
│   ├── favicon.png         # 파비콘 (추가 필요)
│   └── screenshots/        # 앱 스크린샷 이미지 폴더
└── README.md
```

## 페이지 구성

| 페이지 | 설명 |
|--------|------|
| **홈** | 메인 랜딩 페이지, 핵심 기능 하이라이트, 담당자 이메일 연락처 |
| **앱 소개** | BaseBall Book 앱 소개, 대상 사용자, 주요 특징, 이용 요금 |
| **기능 안내** | 앱의 각 화면별 상세 기능 설명 및 사용 방법, 스크린샷 영역 |
| **FAQ** | 자주 묻는 질문과 답변 |

## 스크린샷 추가 방법

1. `assets/screenshots/` 폴더에 캡쳐 이미지 파일을 넣습니다.
2. `index.html`에서 해당 기능 섹션의 `screenshot-placeholder` div를 아래와 같이 교체합니다:

```html
<!-- 변경 전 (플레이스홀더) -->
<div class="screenshot-placeholder">
  <span>로그인 화면<br>캡쳐 이미지</span>
</div>

<!-- 변경 후 (실제 이미지) -->
<img src="assets/screenshots/login.png" alt="로그인 화면" class="screenshot-image">
```

## 담당자 이메일 변경

`index.html`에서 `sports@3nd.com`을 검색하여 원하는 이메일로 변경하세요.

## 로컬 실행

정적 웹사이트이므로 아무 HTTP 서버로 실행 가능합니다:

```bash
# Python
python3 -m http.server 8080

# Node.js (npx)
npx serve .
```
