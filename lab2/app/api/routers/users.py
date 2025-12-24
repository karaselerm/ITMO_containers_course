from api.schemas.schemas import UserCreateRequest, UserCreateResponse
from db.db import get_db
from db.models import User
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserCreateResponse, status_code=201)
async def create_user(user_data: UserCreateRequest, db: Session = Depends(get_db)):
    """Создать нового пользователя"""
    new_user = User(name=user_data.name, age=user_data.age)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{user_id}", response_model=UserCreateResponse)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    """Получить пользователя по ID"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/", response_model=list[UserCreateResponse])
async def get_all_users(db: Session = Depends(get_db)):
    """Получить всех пользователей"""
    users = db.query(User).all()
    return users
