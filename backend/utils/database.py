"""Database utilities for My.app"""

from typing import Dict, List, Optional
from datetime import datetime
import json


class InMemoryDatabase:
    """In-memory database for Stage 1-2 development"""
    
    def __init__(self):
        self.messages: Dict[str, list] = {}
        self.conversations: Dict[str, dict] = {}
        self.executions: Dict[str, dict] = {}
        self.users: Dict[str, dict] = {}
    
    # Messages
    def add_message(self, conversation_id: str, message: dict) -> str:
        """Add message to conversation"""
        if conversation_id not in self.messages:
            self.messages[conversation_id] = []
        
        message_id = f"msg_{datetime.now().timestamp()}"
        message['id'] = message_id
        message['timestamp'] = datetime.now().isoformat()
        self.messages[conversation_id].append(message)
        return message_id
    
    def get_messages(self, conversation_id: str) -> List[dict]:
        """Get all messages in conversation"""
        return self.messages.get(conversation_id, [])
    
    def clear_messages(self, conversation_id: str) -> bool:
        """Clear all messages in conversation"""
        if conversation_id in self.messages:
            self.messages[conversation_id] = []
            return True
        return False
    
    # Conversations
    def create_conversation(self, user_id: str, agent_id: str) -> str:
        """Create new conversation"""
        conversation_id = f"conv_{datetime.now().timestamp()}"
        self.conversations[conversation_id] = {
            'id': conversation_id,
            'user_id': user_id,
            'agent_id': agent_id,
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        self.messages[conversation_id] = []
        return conversation_id
    
    def get_conversation(self, conversation_id: str) -> Optional[dict]:
        """Get conversation details"""
        return self.conversations.get(conversation_id)
    
    # Executions
    def add_execution(self, agent_id: str, execution: dict) -> str:
        """Add agent execution"""
        execution_id = f"exec_{datetime.now().timestamp()}"
        execution['id'] = execution_id
        execution['started_at'] = datetime.now().isoformat()
        self.executions[execution_id] = execution
        return execution_id
    
    def get_execution(self, execution_id: str) -> Optional[dict]:
        """Get execution details"""
        return self.executions.get(execution_id)
    
    def update_execution(self, execution_id: str, updates: dict) -> bool:
        """Update execution"""
        if execution_id in self.executions:
            self.executions[execution_id].update(updates)
            self.executions[execution_id]['updated_at'] = datetime.now().isoformat()
            return True
        return False
    
    # Users
    def create_user(self, username: str, email: Optional[str] = None) -> str:
        """Create user"""
        user_id = f"user_{datetime.now().timestamp()}"
        self.users[user_id] = {
            'id': user_id,
            'username': username,
            'email': email,
            'created_at': datetime.now().isoformat()
        }
        return user_id
    
    def get_user(self, user_id: str) -> Optional[dict]:
        """Get user details"""
        return self.users.get(user_id)
    
    # Statistics
    def get_stats(self) -> dict:
        """Get database statistics"""
        return {
            'total_messages': sum(len(msgs) for msgs in self.messages.values()),
            'total_conversations': len(self.conversations),
            'total_executions': len(self.executions),
            'total_users': len(self.users)
        }


# Global database instance
db = InMemoryDatabase()
