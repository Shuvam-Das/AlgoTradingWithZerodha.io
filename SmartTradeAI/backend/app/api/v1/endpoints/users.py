from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api import deps
from app.core.security import get_password_hash
from app.schemas.user import User, UserCreate, UserUpdate
from app.crud.crud_user import crud_user

router = APIRouter()

@router.post("/register", response_model=User)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: UserCreate
) -> Any:
    """
    Create new user.
    """
    user = crud_user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists."
        )
    
    return crud_user.create(db=db, obj_in=user_in)

@router.get("/me", response_model=User)
def read_user_me(
    current_user: User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Get current user.
    """
    return current_user

@router.put("/me", response_model=User)
def update_user_me(
    *,
    db: Session = Depends(deps.get_db),
    password: str = Body(None),
    full_name: str = Body(None),
    email: str = Body(None),
    current_user: User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Update current user.
    """
    current_user_data = UserUpdate(
        password=get_password_hash(password) if password else None,
        full_name=full_name,
        email=email
    )
    return crud_user.update(db=db, db_obj=current_user, obj_in=current_user_data)