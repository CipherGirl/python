from fastapi import APIRouter, HTTPException, status, Depends
import psycopg2
from psycopg2.extensions import connection
from app.schemas.user import UserCreate, UserResponse
from app.services.user import UserService
from app.core.database import db_generator
from typing import List

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(
    user: UserCreate, 
    db: connection = Depends(db_generator)
):
    try:
        new_user = UserService.create_user(db, user)
        return new_user
    
    except psycopg2.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error creating user: {str(e)}"
        )

@router.get("/", response_model=List[UserResponse])
def get_users(db: connection = Depends(db_generator)):
    users = UserService.get_all_users(db)
    return users

@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int, 
    db: connection = Depends(db_generator)
):
    user = UserService.get_user_by_id(db, user_id)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

