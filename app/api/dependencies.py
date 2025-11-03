from fastapi import Header, HTTPException, status
from jose import jwt, JWTError
from app.core.config import settings

def verify_token(authorization: str = Header(...)) -> str:
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication scheme"
            )
        payload = jwt.decode(token, settings.app_secret, algorithms=["HS256"])
        player_id: str = payload.get("sub")
        if player_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )
        return player_id
    except (ValueError, JWTError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
