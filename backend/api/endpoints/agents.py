"""
Agents Endpoint - Agent management and execution
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, List, Optional
from agents.parent_controller import parent_controller, BaseAgent

router = APIRouter(prefix="/agents", tags=["agents"])


class AgentRequest(BaseModel):
    """Agent execution request"""
    prompt: str
    context: Dict[str, Any] = {}
    target_agents: Optional[List[str]] = None


class UpgradeRequest(BaseModel):
    """Agent upgrade request"""
    user: str
    proposal: str


@router.get("/list")
async def list_agents() -> Dict[str, Any]:
    """List all registered agents"""
    status = parent_controller.get_status()
    return {
        "agents": list(status["agents"].keys()),
        "total": status["total_agents"],
        "status": status["controller_status"]
    }


@router.get("/status")
async def get_agents_status() -> Dict[str, Any]:
    """Get all agents status"""
    return parent_controller.get_status()


@router.get("/status/{agent_name}")
async def get_agent_status(agent_name: str) -> Dict[str, Any]:
    """Get specific agent status"""
    result = parent_controller.get_agent_status(agent_name)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@router.post("/register")
async def register_agent(name: str) -> Dict[str, Any]:
    """Register a new agent"""
    agent = BaseAgent(name)
    return parent_controller.register_agent(name, agent)


@router.post("/run")
async def run_agents(request: AgentRequest) -> Dict[str, Any]:
    """Execute agents with prompt"""
    results = await parent_controller.run_agents(
        request.prompt,
        request.context,
        request.target_agents
    )
    return {
        "prompt": request.prompt,
        "results": results,
        "total_results": len(results)
    }


@router.post("/upgrade-request")
async def submit_upgrade(request: UpgradeRequest) -> Dict[str, Any]:
    """Submit agent upgrade request"""
    return parent_controller.request_upgrade(request.user, request.proposal)


@router.get("/upgrade-requests")
async def get_upgrade_requests() -> Dict[str, Any]:
    """Get pending upgrade requests"""
    status = parent_controller.get_status()
    return {
        "upgrade_requests": status["upgrade_requests"],
        "total": len(status["upgrade_requests"])
    }


@router.post("/upgrade-requests/{request_id}/approve")
async def approve_upgrade(request_id: int) -> Dict[str, Any]:
    """Approve upgrade request"""
    result = parent_controller.approve_upgrade(request_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@router.post("/upgrade-requests/{request_id}/reject")
async def reject_upgrade(request_id: int) -> Dict[str, Any]:
    """Reject upgrade request"""
    result = parent_controller.reject_upgrade(request_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result
