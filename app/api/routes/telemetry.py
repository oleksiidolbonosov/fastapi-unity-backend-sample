from fastapi import APIRouter, Depends
from app.api.dependencies import verify_token
from app.models.schemas import TelemetryEvent

router = APIRouter()

@router.post("/telemetry")
async def telemetry(event: TelemetryEvent, player_id: str = Depends(verify_token)):
    # In production you'd push events to analytics pipeline; here we log
    return {"status": "received", "player_id": player_id, "event": event.event}
