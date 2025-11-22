"""
Notifier Module for My.app
Handles WebSocket broadcasts and real-time notifications
"""

from typing import Dict, Any, List, Optional
from datetime import datetime


class Notifier:
    """
    Notification and Broadcasting Service
    Manages WebSocket connections and real-time event broadcasting
    """
    
    def __init__(self):
        """Initialize Notifier"""
        self.connections: List[Any] = []
        self.message_history: List[Dict[str, Any]] = []
        self.max_history: int = 1000
    
    async def connect(self, websocket: Any):
        """
        Register new WebSocket connection
        
        Args:
            websocket: WebSocket connection object
        """
        self.connections.append(websocket)
        print(f"New WebSocket connection. Total: {len(self.connections)}")
    
    async def disconnect(self, websocket: Any):
        """
        Unregister WebSocket connection
        
        Args:
            websocket: WebSocket connection object
        """
        if websocket in self.connections:
            self.connections.remove(websocket)
        print(f"WebSocket disconnected. Total: {len(self.connections)}")
    
    async def broadcast(self, message: Dict[str, Any]):
        """
        Broadcast message to all connected clients
        
        Args:
            message: Message dictionary to broadcast
        """
        # Add timestamp and store in history
        message["timestamp"] = datetime.utcnow().isoformat()
        self._add_to_history(message)
        
        # Broadcast to all connections
        for connection in self.connections:
            try:
                await connection.send_json(message)
            except Exception as e:
                print(f"Error broadcasting to connection: {e}")
    
    async def broadcast_to_group(self, group: str, message: Dict[str, Any]):
        """
        Broadcast message to specific group
        
        Args:
            group: Group identifier
            message: Message dictionary to broadcast
        """
        message["group"] = group
        message["timestamp"] = datetime.utcnow().isoformat()
        self._add_to_history(message)
        
        for connection in self.connections:
            try:
                await connection.send_json(message)
            except Exception as e:
                print(f"Error broadcasting to group {group}: {e}")
    
    def _add_to_history(self, message: Dict[str, Any]):
        """Store message in history"""
        self.message_history.append(message)
        if len(self.message_history) > self.max_history:
            self.message_history.pop(0)
    
    def get_message_history(self, limit: int = 50) -> List[Dict[str, Any]]:
        """
        Get recent message history
        
        Args:
            limit: Number of recent messages to return
        
        Returns:
            List of recent messages
        """
        return self.message_history[-limit:]
    
    def get_status(self) -> Dict[str, Any]:
        """Get notifier status"""
        return {
            "connected_clients": len(self.connections),
            "history_size": len(self.message_history),
            "max_history": self.max_history,
            "status": "active"
        }


# Global notifier instance
notifier = Notifier()
