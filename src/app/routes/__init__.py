from fastapi import APIRouter

router = APIRouter(prefix="/agents")


@router.post("/invoke", tags=["agents"])
def invoke():
    return "hello"
