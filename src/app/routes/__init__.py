from fastapi import APIRouter
from fastapi import Request
router = APIRouter(prefix="/agents")


@router.post("/invoke", tags=["agents"])
def invoke(prompt: str, request: Request):
    print(request.app.state)
    return "hello"
