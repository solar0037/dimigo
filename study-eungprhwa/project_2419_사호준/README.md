# project_2419_사호준
---

## 개요

응용프로그래밍화면구현 1학기 수업에서 진행한 프로젝트입니다. 수업 중에 실습한 `index.html` 파일은 최소한으로만 변경하였고, 기획서에 작성한 내용을 바탕으로 다음 페이지를 추가로 작성했습니다. `header.html`, `nav.html`, `footer.html`은 페이지마다 겹치는 부분으로, 따로 작성하고 jQuery를 이용해 불러와 코드 중복을 줄였습니다.

- `login.html` - 로그인
- `signup.html` - 가입
- `search.html` - 검색
- `product.html` - 상품 조회
- `purchase.html` - 상품 결제

빠진 페이지

- 소개, 안내 - `index.html`에 포함됨
- 고객센터, Q&A - `index.html`에 포함됨 (고객센터는 미포함)
- 관리자 - 미구현

## 시작하기

본 프로젝트는 jQuery를 통해 동적으로 HTML의 `header`, `nav`, `footer` 부분을 불러오기 때문에 서버에서 실행되지 않고 파일로 열 경우 CORS 에러가 발생합니다. 따라서 아래의 두 가지 방법 중 하나를 선택해 주세요.

### 1. VSCode의 Live Server 이용

VSCode의 확장인 Live Server를 설치하고 `F1` -> `Live Server: Open with Live Server`를 선택해 서버를 열어주세요. `localhost:5000/static`에 접속하면 웹페이지를 볼 수 있습니다.

### 2. 파이썬 서버 이용

파이썬을 설치하고 다음의 명령어를 입력해 주세요. 환경 변수 `PATH`에 파이썬과 pip가 등록되어 있어야 합니다.

```sh
pip install -r requirements.txt
uvicorn main:app
```

`localhost:8000`에 접속하면 웹페이지를 볼 수 있습니다.

## 사용한 기술

- HTML/CSS/JS - jQuery
- Python - FastAPI, uvicorn
