"""
Parent Controller - Main agent orchestration and management
"""

import asyncio
from typing import List, Dict, Any, Optional, Callable


class BaseAgent:
    """Base class for agents"""
    
    def __init__(self, name: str):
        self.name = name
        self.status = "idle"
        self.last_result = None
    
    async def run(self, prompt: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Run agent with given prompt and context
        
        Args:
            prompt: Input prompt
            context: Context dictionary
        
        Returns:
            Result dictionary
        """
        self.status = "running"
        try:
            result = {
                "agent": self.name,
                "prompt": prompt,
                "response": f"[{self.name}] processed: {prompt[:50]}...",
                "status": "success",
                "context_used": list(context.keys())
            }
            self.last_result = result
            self.status = "idle"
            return result
        except Exception as e:
            self.status = "error"
            return {
                "agent": self.name,
                "error": str(e),
                "status": "failed"
            }


class ParentController:
    """
    Central controller for managing multiple agents
    Handles agent registration, execution, and upgrade requests
    """
    
    def __init__(self):
        """Initialize ParentController"""
        self.agents: Dict[str, BaseAgent] = {}
        self.upgrade_requests: List[Dict[str, Any]] = []
        self.execution_history: List[Dict[str, Any]] = []
        self.max_history: int = 500
    
    def register_agent(self, name: str, agent_instance: BaseAgent) -> Dict[str, Any]:
        """
        Register a new agent
        
        Args:
            name: Agent name
            agent_instance: Agent instance
        
        Returns:
            Registration confirmation
        """
        self.agents[name] = agent_instance
        return {
            "agent": name,
            "status": "registered",
            "total_agents": len(self.agents)
        }
    
    def unregister_agent(self, name: str) -> Dict[str, Any]:
        """
        Unregister an agent
        
        Args:
            name: Agent name to unregister
        
        Returns:
            Unregistration confirmation
        """
        if name in self.agents:
            del self.agents[name]
            return {
                "agent": name,
                "status": "unregistered",
                "total_agents": len(self.agents)
            }
        return {"error": f"Agent {name} not found"}
    
    async def run_agents(
        self,
        prompt: str,
        context: Dict[str, Any],
        target_agents: Optional[List[str]] = None
    ) -> List[Dict[str, Any]]:
        """
        Run multiple agents with given prompt and context
        
        Args:
            prompt: Input prompt
            context: Context dictionary
            target_agents: List of agent names to run (all if None)
        
        Returns:
            List of results from all executed agents
        """
        if target_agents is None:
            target_agents = list(self.agents.keys())
        
        # Filter target agents that exist
        valid_agents = {
            name: agent for name, agent in self.agents.items()
            if name in target_agents
        }
        
        if not valid_agents:
            return [{"error": f"No valid agents found. Available: {list(self.agents.keys())}"}]
        
        # Run agents concurrently
        tasks = [
            agent.run(prompt, context)
            for name, agent in valid_agents.items()
        ]
        
        try:
            results = await asyncio.gather(*tasks, return_exceptions=True)
            output = [
                {"error": str(r)} if isinstance(r, Exception) else r
                for r in results
            ]
            
            # Store in history
            execution = {
                "prompt": prompt,
                "agents_run": list(valid_agents.keys()),
                "results": output,
                "success": len([r for r in output if "error" not in r]) == len(output)
            }
            self._add_to_history(execution)
            
            return output
        except Exception as e:
            return [{"error": str(e)}]
    
    def request_upgrade(self, user: str, proposal: str) -> Dict[str, Any]:
        """
        Submit an upgrade request
        
        Args:
            user: User requesting upgrade
            proposal: Upgrade proposal description
        
        Returns:
            Request confirmation
        """
        request = {
            "id": len(self.upgrade_requests),
            "user": user,
            "proposal": proposal,
            "status": "pending",
            "timestamp": __import__("datetime").datetime.utcnow().isoformat()
        }
        self.upgrade_requests.append(request)
        return request
    
    def approve_upgrade(self, request_id: int) -> Dict[str, Any]:
        """
        Approve an upgrade request
        
        Args:
            request_id: ID of request to approve
        
        Returns:
            Updated request
        """
        if 0 <= request_id < len(self.upgrade_requests):
            self.upgrade_requests[request_id]["status"] = "approved"
            return self.upgrade_requests[request_id]
        return {"error": f"Request {request_id} not found"}
    
    def reject_upgrade(self, request_id: int) -> Dict[str, Any]:
        """
        Reject an upgrade request
        
        Args:
            request_id: ID of request to reject
        
        Returns:
            Updated request
        """
        if 0 <= request_id < len(self.upgrade_requests):
            self.upgrade_requests[request_id]["status"] = "rejected"
            return self.upgrade_requests[request_id]
        return {"error": f"Request {request_id} not found"}
    
    def _add_to_history(self, execution: Dict[str, Any]):
        """Store execution in history"""
        self.execution_history.append(execution)
        if len(self.execution_history) > self.max_history:
            self.execution_history.pop(0)
    
    def get_status(self) -> Dict[str, Any]:
        """Get controller status"""
        return {
            "agents": {
                name: {"status": agent.status, "last_result": agent.last_result}
                for name, agent in self.agents.items()
            },
            "total_agents": len(self.agents),
            "upgrade_requests": self.upgrade_requests,
            "execution_history_size": len(self.execution_history),
            "controller_status": "active"
        }
    
    def get_agent_status(self, agent_name: str) -> Dict[str, Any]:
        """Get status of specific agent"""
        if agent_name in self.agents:
            agent = self.agents[agent_name]
            return {
                "agent": agent_name,
                "status": agent.status,
                "last_result": agent.last_result
            }
        return {"error": f"Agent {agent_name} not found"}


# Global parent controller instance
parent_controller = ParentController()
