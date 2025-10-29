from fastapi import FastAPI, Depends, WebSocket, WebSocketDisconnect, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from pydantic import ValidationError

from app.core.config import settings
from app.api.api_v1.api import api_router
from app.core.socket_manager import socket_manager
from app.api import deps
from app.models.user import User
from app.schemas.token import TokenPayload
from app.crud.crud_user import crud_user

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix=settings.API_V1_STR)

# WebSocket endpoint
@app.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket,
    token: str = None,
    db: Session = Depends(deps.get_db)
):
    if not token:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return

    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (JWTError, ValidationError):
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return
        
    user = crud_user.get(db, id=token_data.sub)
    if not user:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return

    try:
        await socket_manager.connect(websocket, user.id)
        while True:
            try:
                data = await websocket.receive_text()
                # You can process received data here if needed
                await socket_manager.broadcast_to_user(user.id, {"event": "data", "data": data})
            except WebSocketDisconnect:
                socket_manager.disconnect(websocket, user.id)
                break
    except Exception as e:
        socket_manager.disconnect(websocket, user.id)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}