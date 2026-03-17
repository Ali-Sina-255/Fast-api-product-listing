from fastapi import FastAPI

from apps.config.db import init_db
from apps.routes.route import router

app = FastAPI(
    title="FastAPI App",
    description="My production-ready FastAPI project",
    version="1.0.0",
)


# =========================
# STARTUP EVENT
# =========================
@app.on_event("startup")
async def on_startup():
    await init_db()
    print("🚀 Application started and DB initialized")


# =========================
# ROUTES
# =========================
app.include_router(router, prefix="/api/v1")


# =========================
# ROOT ENDPOINT
# =========================
@app.get("/")
def root():
    return {"message": "API is running"}
