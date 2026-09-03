from fastapi import FastAPI,Request
import uvicorn
from src.graphs.graph_builder import GraphBuilder
from src.llms.groq_llm import GroqLLM


import os
from dotenv import load_dotenv

app=FastAPI()

load_dotenv()
LANGSMITH_API_KEY=os.getenv("LANGCHAIN_API_KEY")

@app.post("/blogs")
async def create_blogs(request:Request):
    data = await request.json()
    topic = data.get("topic","")

    groqllm = GroqLLM().get_llm()

    graph_builder=GraphBuilder(groqllm)

    if topic:
        graph_builder=graph_builder.setup_graph(usecase="topic")
        state=graph_builder.invoke({"topic":topic})

    return {"data":state}


if __name__ == "__main__":
    uvicorn.run("app:app",host="0.0.0.0",port=8000,reload=True)