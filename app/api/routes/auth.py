from fastapi import APIRouter
from jose import jwt
from app.core.config import settings
from app.models.schemas import LoginRequest, TokenResponse

router = APIRouter()

@router.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest):
    token = jwt.encode(
        {"sub": request.player_id},
        settings.app_secret,
        algorithm="HS256"
    )
    return TokenResponse(token=token)
