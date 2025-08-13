from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

app = FastAPI(
    title="Gaming AI Chatbot",
    description="AI-powered gaming assistant with ML recommendations",
    version="1.0.0"
)

# CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Gaming AI Chatbot API is running! 🎮🤖"}


@app.get("/health")
async def health():
    return {"status": "healthy", "ml_api": "connected"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
