"""Data models for My.app"""

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum


class MessageType(str, Enum):
    """Message types"""
    USER = "user"
    AGENT = "agent"
    SYSTEM = "system"


class Message(BaseModel):
    """Message model"""
    id: Optional[str] = None
    content: str
    message_type: MessageType = MessageType.USER
    agent_id: Optional[str] = None
    agent_name: Optional[str] = None
    timestamp: Optional[datetime] = Field(default_factory=datetime.now)
    metadata: Optional[dict] = None

    class Config:
        schema_extra = {
            "example": {
                "content": "Hello, how can I help you?",
                "message_type": "agent",
                "agent_name": "Aelira",
                "timestamp": "2024-11-23T12:00:00"
            }
        }


class ExecutionStatus(str, Enum):
    """Execution status"""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class Execution(BaseModel):
    """Agent execution model"""
    id: Optional[str] = None
    agent_id: str
    agent_name: str
    prompt: str
    result: Optional[str] = None
    status: ExecutionStatus = ExecutionStatus.PENDING
    started_at: Optional[datetime] = Field(default_factory=datetime.now)
    completed_at: Optional[datetime] = None
    error: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "agent_id": "aelira",
                "agent_name": "Aelira",
                "prompt": "Provide strategic advice",
                "status": "completed",
                "result": "Strategic recommendation..."
            }
        }


class User(BaseModel):
    """User model"""
    id: Optional[str] = None
    username: str
    email: Optional[str] = None
    preferences: Optional[dict] = None
    created_at: Optional[datetime] = Field(default_factory=datetime.now)


class AgentProfile(BaseModel):
    """Agent profile model"""
    id: str
    name: str
    title: str
    color: str
    emoji: str
    personality: str
    traits: List[str]
    memory_capacity: int = 100

    class Config:
        schema_extra = {
            "example": {
                "id": "aelira",
                "name": "Aelira",
                "title": "Wisdom Guardian",
                "color": "#667eea",
                "emoji": "🔮",
                "personality": "Strategic, patient, insightful",
                "traits": ["strategic", "patient", "insightful"]
            }
        }


class ConversationHistory(BaseModel):
    """Conversation history model"""
    user_id: Optional[str] = None
    agent_id: Optional[str] = None
    messages: List[Message] = []
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)
