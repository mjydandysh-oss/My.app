"""
My.app Backend - Main FastAPI Application
Stage 1: Initial Scaffold with Agent Orchestration
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.router import router
from backend.config.settings import settings
from backend.agents.parent_controller import parent_controller, BaseAgent

# Initialize FastAPI app
app = FastAPI(
    title=settings.API_TITLE,
    version=settings.API_VERSION,
    debug=settings.DEBUG
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(router)


@app.on_event("startup")
async def startup_event():
    """Initialize on startup"""
    print(f"Starting {settings.API_TITLE} v{settings.API_VERSION}")
    
    # Register default agents
    for agent_name in ["Aelira", "Zyra", "Xyron", "Orryn"]:
        agent = BaseAgent(agent_name)
        parent_controller.register_agent(agent_name, agent)
        print(f"Registered agent: {agent_name}")
    
    print("Application startup complete")


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown"""
    print(f"Shutting down {settings.API_TITLE}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )
