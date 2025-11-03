from fastapi import FastAPI
from app.api.routes import auth, sync, telemetry

app = FastAPI(
    title="FastAPI Unity Backend",
    description="Sample backend for Unity game integration",
    version="1.0.0"
)

app.include_router(auth.router, prefix="/api", tags=["auth"])
app.include_router(sync.router, prefix="/api", tags=["sync"])
app.include_router(telemetry.router, prefix="/api", tags=["telemetry"])

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
