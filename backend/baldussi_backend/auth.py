from baldussi_backend.database import get_db
from baldussi_backend.models import User
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import JWTError
from baldussi_backend.security import create_access_token, decode_token, verify_password, ACCESS_TOKEN_EXPIRE_MINUTES

# Padrão OAuth2 (o front envia form: username/password)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

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
