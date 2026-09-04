from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

from src.graphs.graph_builder import GraphBuilder
from src.llms.groq_llm import GroqLLM


app = FastAPI()


class BlogRequest(BaseModel):
    topic: str


@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.post("/blogs")
async def create_blogs(request: BlogRequest):

    topic = request.topic.strip()

    if not topic:
        raise HTTPException(
            status_code=400,
            detail="Topic is required"
        )

    groqllm = GroqLLM().get_llm()

    graph_builder = GraphBuilder(groqllm)
    graph = graph_builder.setup_graph(usecase="topic")

    state = graph.invoke({
        "topic": topic
    })

    return {
        "data": state
    }


if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000
    )