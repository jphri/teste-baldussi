from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import JWTError
from baldussi_backend.database import get_db
from baldussi_backend.models import User
from baldussi_backend.schema import Token
from baldussi_backend.security import create_access_token, decode_token, verify_password, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter(prefix="/auth", tags=["auth"])

# Padrão OAuth2 (o front envia form: username/password)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

@router.post("/token", response_model=Token)
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form.username).first()
    if not user or not verify_password(form.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")

    access_token = create_access_token(data={"sub": user.username}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return {"access_token": access_token, "token_type": "bearer"}

# Dependência para pegar usuário atual a partir do token
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    creds_error = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    try:
        payload = decode_token(token)
        sub = payload.get("sub")
        if not sub:
            raise creds_error
    except JWTError:
        raise creds_error
    user = db.query(User).filter(User.username == sub).first()
    if not user:
        raise creds_error
    return user

@router.get("/me")
def me(current: User = Depends(get_current_user)):
    return {"id": current.id, "username": current.username, "is_admin": current.is_admin}