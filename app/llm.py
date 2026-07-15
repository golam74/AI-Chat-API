from ollama import Client
import os
from pathlib import Path
from dotenv import load_dotenv
from fastapi import HTTPException

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

host = os.getenv("OLLAMA_HOST")
model = os.getenv("MODEL")

client = Client(host=host)


async def generate_response(message: str) -> str:

    try:

        response = client.chat(

            model=model,

            messages=[
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        return response["message"]["content"]

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="Something went wrong."
        )

