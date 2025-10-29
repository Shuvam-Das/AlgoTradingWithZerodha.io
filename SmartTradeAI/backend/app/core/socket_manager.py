from typing import Dict, Set
import json
from fastapi import WebSocket
from app.utils.logging import logger

class SocketManager:
    def __init__(self):
        self.active_connections: Dict[int, Set[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, user_id: int):
        await websocket.accept()
        if user_id not in self.active_connections:
            self.active_connections[user_id] = set()
        self.active_connections[user_id].add(websocket)
        logger.info(f"Client connected. Total active connections for user {user_id}: {len(self.active_connections[user_id])}")

    def disconnect(self, websocket: WebSocket, user_id: int):
        if user_id in self.active_connections:
            self.active_connections[user_id].discard(websocket)
            if not self.active_connections[user_id]:
                del self.active_connections[user_id]
        logger.info(f"Client disconnected. Total active connections for user {user_id}: {len(self.active_connections.get(user_id, set()))}")

    async def broadcast_to_user(self, user_id: int, message: dict):
        if user_id in self.active_connections:
            disconnected = set()
            for connection in self.active_connections[user_id]:
                try:
                    await connection.send_json(message)
                except Exception as e:
                    logger.error(f"Error sending message to user {user_id}: {str(e)}")
                    disconnected.add(connection)
            
            # Clean up disconnected connections
            for connection in disconnected:
                self.active_connections[user_id].discard(connection)
            if not self.active_connections[user_id]:
                del self.active_connections[user_id]

socket_manager = SocketManager()