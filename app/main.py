from fastapi import FastAPI
from app.schemas import ChatRequest, ChatResponse
from app.llm import generate_response

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Chat API Running"}


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    # Remove Extra Spaces
    message = request.message.strip()

    # Generate AI Response
    ai_response = await generate_response(message)

    # Return Response
    return {
        "response": ai_response
    }