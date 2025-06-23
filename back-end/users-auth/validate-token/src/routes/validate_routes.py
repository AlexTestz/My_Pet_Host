from fastapi import APIRouter, Header
from src.utils.jwt_manager import verify_token

router = APIRouter(prefix="/api/auth", tags=["Token Validation"])

@router.get("/validate-token")
def validate_token(Authorization: str = Header(...)):
    token = Authorization.replace("Bearer ", "")
    payload = verify_token(token)
    return {"message": "✅ Token is valid", "payload": payload}
