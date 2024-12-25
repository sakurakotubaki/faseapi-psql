from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.api.v1 import auth
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="FastAPI Authentication System with PostgreSQL",
    version="1.0.0"
)

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to FastAPI Docker Demo",
        "version": "1.0.0",
        "status": "running",
        "docs_url": "/docs",
        "openapi_url": "/openapi.json"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": settings.get_current_time()}

# エラーハンドリング
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

# ルーターの登録
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
