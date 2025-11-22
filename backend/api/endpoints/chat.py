"""
Chat Endpoint - Chat and messaging interface
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, List

router = APIRouter(prefix="/chat", tags=["chat"])


class ChatMessage(BaseModel):
    """Chat message model"""
    text: str
    sender: str = "user"
    character: str = "aelira"


class ChatResponse(BaseModel):
    """Chat response model"""
    message: str
    character: str
    timestamp: str


@router.post("/send")
async def send_message(message: ChatMessage) -> Dict[str, Any]:
    """Send a chat message"""
    return {
        "status": "received",
        "message": message.text,
        "sender": message.sender,
        "character": message.character,
        "response": f"[{message.character.upper()}] received your message"
    }


@router.get("/history")
async def get_chat_history(limit: int = 50) -> Dict[str, Any]:
    """Get chat history"""
    return {
        "messages": [
            {
                "text": f"Message {i}",
                "sender": "user" if i % 2 == 0 else "character",
                "character": ["aelira", "zyra", "xyron", "orryn"][i % 4]
            }
            for i in range(min(limit, 50))
        ],
        "total": 50
    }


@router.post("/clear")
async def clear_history() -> Dict[str, str]:
    """Clear chat history"""
    return {"status": "cleared"}
