# moyotayo BE
2026 바이브해커톤 — moyotayo 백엔드 (FastAPI).

## Stack

* __[FastAPI](https://fastapi.tiangolo.com/)__ + Python 3.14
* __[SQLAlchemy 2.0](https://docs.sqlalchemy.org/)__ — 비동기 ORM
* __[Alembic](https://alembic.sqlalchemy.org/)__ — DB 마이그레이션
* __[Supabase](https://supabase.com/)__ — PostgreSQL · Auth · Realtime · Storage
* __[Pydantic v2](https://docs.pydantic.dev/)__ — 요청/응답 스키마 및 유효성 검사
* `python-jose` — JWT 토큰 처리

## 시작하기

```bash
# 가상환경 생성 및 활성화
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 패키지 설치
pip install -r requirements.txt

# 환경변수 설정
cp .env.example .env
# .env 파일에 실제 값 입력 후 저장

# 개발 서버 실행
uvicorn app.main:app --reload
```

실행 후 아래 URL에서 확인하세요:

* Swagger UI: `http://localhost:8000/docs`
* ReDoc: `http://localhost:8000/redoc`
* 헬스체크: `http://localhost:8000`

## 환경변수

`.env.example`을 복사해 `.env`를 만들고 아래 값을 채워주세요.

| 변수명 | 설명 |
|--------|------|
| `DATABASE_URL` | Supabase PostgreSQL 연결 URL (`postgresql+asyncpg://...`) |
| `SUPABASE_URL` | Supabase 프로젝트 URL |
| `SUPABASE_KEY` | Supabase Anon Key |
| `JWT_SECRET` | JWT 서명용 비밀키 |

## 디렉토리 구조

```
app/
├── main.py              # FastAPI 앱 진입점, CORS 설정, 라우터 등록
├── core/
│   ├── config.py        # 환경변수 관리 (Pydantic Settings)
│   ├── database.py      # DB 연결 및 세션 관리
│   └── dependencies.py  # 공통 의존성 (인증 미들웨어 등)
├── models/              # SQLAlchemy 테이블 모델
│   ├── user.py
│   └── pod.py
├── schemas/             # Pydantic 요청/응답 스키마
│   ├── user.py
│   └── pod.py
├── routers/             # API 엔드포인트 라우터
│   ├── auth.py
│   └── pods.py
└── services/            # 비즈니스 로직
    └── pod_service.py
alembic/                 # DB 마이그레이션 스크립트
.env                     # 환경변수 (git 제외)
.env.example             # 환경변수 템플릿
requirements.txt
```

## 부트스트랩 메모

* `app/main.py`가 CORS 미들웨어와 라우터를 등록합니다. 새 라우터 추가 시 여기에 `include_router`를 추가하세요.
* DB 세션 기본 설정: `expire_on_commit=False` — 필요에 따라 `app/core/database.py`에서 조정.
* Zustand store(`src/store/useAppStore.ts`)는 placeholder입니다. 실제 도메인 store로 교체하세요.
* Supabase Realtime은 팟 현황 실시간 동기화에 사용합니다. 별도 WebSocket 서버는 필요하지 않습니다.
* 마이그레이션은 모델 변경 후 아래 명령어로 생성하세요.

```bash
alembic revision --autogenerate -m "변경 내용 설명"
alembic upgrade head
```
