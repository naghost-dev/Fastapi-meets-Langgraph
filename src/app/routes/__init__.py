from typing import Annotated

from fastapi import APIRouter, Depends
from langgraph.graph.state import CompiledStateGraph

from app.dependencies import get_workflow

router = APIRouter(prefix="/agents",
                   dependencies=[])


@router.post("/invoke", tags=["agents"])
def invoke(prompt: str, workflow: Annotated[CompiledStateGraph, Depends(get_workflow)]):
    config={
        "configurable": {
            "thread_id": 1
        }
    }
    return workflow.invoke({"messages": [{"role": "user", "content": prompt}]}, config, stream_mode="updates")

