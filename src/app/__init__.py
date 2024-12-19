from contextlib import asynccontextmanager

from fastapi import FastAPI
from langgraph.checkpoint.memory import MemorySaver

from app.routes import router
from app.workflows.example_workflow import workflow


@asynccontextmanager
async def lifespan(app: FastAPI):
    memory = MemorySaver()
    graph = workflow.compile(checkpointer=memory)

    yield {
        'workflow': graph
    }

app = FastAPI(lifespan=lifespan)
app.include_router(router)


