import bcrypt

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from baldussi_backend.schema import UserOut, UserCreate
from baldussi_backend.database import get_db
from baldussi_backend.models import User

router = APIRouter(prefix='/users', tags=['users'])

@router.get("/", response_model=list[UserOut])
def list_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@router.post("/register", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        db.close()
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_pw = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    new_user = User(
        username=user.username,
        password_hash=hashed_pw.decode('utf-8'),
        is_admin=user.is_admin
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


