from fastapi import APIRouter, Depends
from app.api.dependencies import verify_token
from app.models.schemas import SyncRequest, SyncResponse

router = APIRouter()

@router.post("/sync", response_model=SyncResponse)
async def sync_state(request: SyncRequest, player_id: str = Depends(verify_token)):
    # In a real app you'd persist state to DB; here we echo back for demo
    return SyncResponse(ok=True, player_id=player_id)
