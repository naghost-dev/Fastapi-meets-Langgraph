# Fastapi-meets-Langgraph
 This repository provides a simple implementation of how to use LangGraph agents integrated and deployed through FastAPI. The goal is to demonstrate how to create a flow with LangGraph and expose its functionality via a REST API. 🚀

## Initial context
This project is based on the example Prompt Generation from User Requirements from LangGraph. It has been migrated to the src.app.genai package, aiming to separate business logic into different parts (we're not in a Jupyter notebook 😜).

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
(Sorry about the port, it’s a habit I picked up at my first job.)


