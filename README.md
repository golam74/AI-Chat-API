<<<<<<< HEAD >>>>>>>>>
=======
# 🤖 AI Chat API

A production-ready AI Chat API built with FastAPI and Ollama.

## 🚀 Features

- FastAPI Backend
- Local LLM (Ollama)
- Request Validation
- Response Validation
- Environment Variables (.env)
- Error Handling
- Health Endpoint
- Model Endpoint
- AI Chat Endpoint

## 🛠 Tech Stack

- Python
- FastAPI
- Ollama
- Pydantic
- Uvicorn
- python-dotenv

## 📂 Project Structure

AI_Chat_API/
│
├── app/
│ ├── main.py
│ ├── llm.py
│ └── schemas.py
│
├── .env
├── requirements.txt
├── .gitignore
└── README.md

## ▶️ Installation

```bash
git clone (https://github.com/golam74?tab=repositories)

cd AI_Chat_API

pip install -r requirements.txt
```

## ▶️ Run

```bash
uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

## 📌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Home |
| GET | /health | Health Check |
| GET | /model | Model Information |
| POST | /chat | AI Chat |

## 👨‍💻 Author

Golam Israil

AI Engineer
=======
# AI-Chat-API
>>>>>>> 3629a77e4aaae1d1b204abf6b28edc43ebe43ec8
