from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from baldussi_backend.database import get_db
from baldussi_backend.models import User
from baldussi_backend.schema import Token
from baldussi_backend.security import create_access_token, decode_token, verify_password, ACCESS_TOKEN_EXPIRE_MINUTES
from baldussi_backend.auth import get_current_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/token", response_model=Token)
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form.username).first()
    if not user or not verify_password(form.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")

    access_token = create_access_token(data={"sub": user.username}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me")
def me(current: User = Depends(get_current_user)):
    return {"id": current.id, "username": current.username, "is_admin": current.is_admin}