from fastapi import FastAPI
from pydantic import BaseModel
from agent import agent

app = FastAPI()

class Question(BaseModel):
    message: str


@app.post("/ask")
def ask(q: Question):
    result = agent.run(q.message)

    # only the final text
    return {"reply": result.content}

@app.get("/")
def home():
    return {"message": "Hello! welcomd to my AI app"}

