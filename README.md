# Fastapi-meets-Langgraph
 This repository provides a simple implementation of how to use LangGraph agents integrated and deployed through FastAPI. The goal is to demonstrate how to create a flow with LangGraph and expose its functionality via a REST API. 🚀

## Initial context
This project is based on the example Prompt Generation from User Requirements from LangGraph. It has been migrated to the src.app.genai package, aiming to separate business logic into different parts (we're not in a Jupyter notebook 😜).

## Considerations before professionalizing this project.

This project will work correctly on your machine, but as we increase the complexity (such as simply adding more workers to the Uvicorn server), you need to keep in mind that Langgraph relies on the concept of **checkpointers to store state**. Currently, the workflows I provided use the memory of the running project, meaning that if two workers are started, the checkpoints from one process will not be accessible to the other, as they are in separate processes.

For this reason, it is necessary to add external persistence (and no, I’m not talking about SQLite). Please take a look at the [following article as a recommendation](https://langchain-ai.github.io/langgraph/how-tos/#persistence). As of December 21, you can use MongoDB or Postgres (don’t go ahead and implement something yourself, this evolves too quickly…).

## The [dependencies.py](src%2Fapp%2Fdependencies.py) file

In the dependencies.py file, we will have the various workflows created in LangGraph precompiled, allowing them to be reused thanks to the magic of dependency injection. The compilation of these workflows usually takes a few valuable milliseconds, which we can leverage to avoid a dreaded Timeout.

## The [routes](src%2Fapp%2Froutes%2F__init__.py) file

We have defined two routes: **`/invoke`** and **`/invoke/{thread_id}`**. The first one will allow us to **start the execution flow**, while the second one will allow us to **continue it**.  

As you can see, the functions have the attribute:  
**`workflow: Annotated[CompiledStateGraph, Depends(get_workflow)]`**,  

which is essentially one of the **workflows** we previously prepared in **`dependencies.py`**.


## Run project

You can start the project using the Makefile provided. First, you need to install the dependencies Once those are resolved, you can run the project
* Install dependencies: 
    ``` shell
    make install
    ```
* Start the project: 
    ``` shell
    make run
    ```
If you're unable to enjoy the benefits of make, you can run the commands directly:

* Install dependencies: 
    ``` shell
    poetry install
    ```
* Start the project: 
    ``` shell
    uvicorn src.app.main:app --port 18080 --reload
    ```

If everything went well, you should be able to access the following URL: http://localhost:18080/docs, resulting in the OpenAPI interface.
(Sorry about the port, it’s a habit I picked up at my first job. 😓)


