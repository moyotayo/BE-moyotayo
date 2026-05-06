from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, pods

app = FastAPI(title="Moyotayo API", version="0.1.0")

# CORS 설정 (프론트 연동 필수!)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 배포 시 프론트 도메인으로 변경
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(pods.router, prefix="/pods", tags=["pods"])

@app.get("/")
async def health_check():
    return {"status": "ok"}