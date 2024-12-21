import uuid
from typing import Annotated

from fastapi import APIRouter, Depends
from langgraph.graph.state import CompiledStateGraph
from pydantic import BaseModel

from app.dependencies import get_workflow

router = APIRouter(prefix="/agents",
                   dependencies=[])


class InvokeResponseModel(BaseModel):
    configuration: dict
    response: list


def get_config(thread_id: str=None):
    if thread_id is None:
        thread_id=str(uuid.uuid4())
    return {
        "configurable": {
            "thread_id": thread_id
        }
    }


@router.post("/invoke", tags=["agents"])
def invoke(prompt: str, workflow: Annotated[CompiledStateGraph, Depends(get_workflow)]) -> InvokeResponseModel:
    config = get_config()
    response = workflow.invoke({"messages": [{"role": "user", "content": prompt}]}, config, stream_mode="updates")
    return InvokeResponseModel(response=response, configuration=config)


@router.post("/invoke/{thread_id}", tags=["agents"])
def invoke(prompt: str, thread_id: str, workflow: Annotated[CompiledStateGraph, Depends(get_workflow)]) -> InvokeResponseModel:
    config = get_config(thread_id)
    response = workflow.invoke({"messages": [{"role": "user", "content": prompt}]}, config, stream_mode="updates")
    return InvokeResponseModel(response=response, configuration=config)
