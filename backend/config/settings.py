"""
Configuration settings for My.app Backend
Stage 1: Initial Configuration
"""

import os
from typing import Optional

class Settings:
    """Base application settings"""
    
    # API Configuration
    API_TITLE: str = "My.app API"
    API_VERSION: str = "1.0.0"
    DEBUG: bool = os.getenv("DEBUG", "true").lower() == "true"
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    
    # LLM Configuration
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    HF_MODEL: Optional[str] = os.getenv("HF_MODEL")
    LLAMA_PATH: Optional[str] = os.getenv("LLAMA_PATH")
    LLM_TIMEOUT: int = int(os.getenv("LLM_TIMEOUT", "30"))
    
    # WebSocket Configuration
    WS_HEARTBEAT: int = int(os.getenv("WS_HEARTBEAT", "30"))
    
    # Agent Configuration
    MAX_AGENTS: int = int(os.getenv("MAX_AGENTS", "10"))
    AGENT_TIMEOUT: int = int(os.getenv("AGENT_TIMEOUT", "60"))
    
    @classmethod
    def to_dict(cls):
        return {
            "api_title": cls.API_TITLE,
            "api_version": cls.API_VERSION,
            "debug": cls.DEBUG,
            "host": cls.HOST,
            "port": cls.PORT,
            "llm_providers": {
                "openai": bool(cls.OPENAI_API_KEY),
                "huggingface": bool(cls.HF_MODEL),
                "llama_local": bool(cls.LLAMA_PATH),
            },
            "max_agents": cls.MAX_AGENTS,
        }

settings = Settings()
