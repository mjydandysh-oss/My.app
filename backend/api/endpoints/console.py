"""
Console Endpoint - System console and logging
"""

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import Dict, Any

router = APIRouter(prefix="/console", tags=["console"])


@router.get("/status")
async def console_status() -> Dict[str, Any]:
    """Get console status"""
    return {
        "status": "operational",
        "endpoint": "console",
        "version": "1.0.0"
    }


@router.get("/logs")
async def get_logs(limit: int = 50) -> Dict[str, Any]:
    """Get system logs"""
    return {
        "logs": [
            f"[LOG {i}] System message" for i in range(min(limit, 50))
        ],
        "total": 50,
        "limit": limit
    }


@router.websocket("/ws")
async def websocket_console(websocket: WebSocket):
    """WebSocket console for real-time logs"""
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Echo: {data}")
    except WebSocketDisconnect:
        print("Console WebSocket disconnected")
