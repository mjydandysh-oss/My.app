"""
Main API Router - Combines all endpoints
"""

from fastapi import APIRouter
from api.endpoints import console, chat, agents
from agents.parent_controller import parent_controller
from config.settings import settings

router = APIRouter()

# Include endpoint routers
router.include_router(console.router)
router.include_router(chat.router)
router.include_router(agents.router)


@router.get("/")
async def root():
    """Root endpoint - API info"""
    return {
        "app": settings.API_TITLE,
        "version": settings.API_VERSION,
        "status": "active",
        "endpoints": {
            "console": "/console",
            "chat": "/chat",
            "agents": "/agents"
        }
    }


@router.get("/health")
async def health_check():
    """Health check endpoint"""
    status = parent_controller.get_status()
    return {
        "status": "healthy",
        "agents_available": status["total_agents"],
        "controller": status["controller_status"]
    }


@router.get("/config")
async def get_config():
    """Get API configuration"""
    return settings.to_dict()
