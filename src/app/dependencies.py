from langgraph.checkpoint.memory import MemorySaver
from app.genai.workflows.example_workflow import workflow

memory = MemorySaver()
workflow_compiled = workflow.compile(checkpointer=memory)

async def get_workflow():
    yield workflow_compiled
