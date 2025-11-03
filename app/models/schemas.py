from pydantic import BaseModel
from typing import Optional, Dict, Any

class LoginRequest(BaseModel):
    player_id: str

class TokenResponse(BaseModel):
    token: str

class SyncRequest(BaseModel):
    player_id: str
    state: Dict[str, Any]

class SyncResponse(BaseModel):
    ok: bool
    player_id: str

class TelemetryEvent(BaseModel):
    player_id: str
    event: str
    payload: Optional[Dict[str, Any]] = None
