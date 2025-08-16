from pydantic import BaseModel

# Modelos Pydantic
class UserCreate(BaseModel):
    username: str
    password: str
    is_admin: bool = False

class UserOut(BaseModel):
    id: int
    username: str
    is_admin: bool
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    sub: str | None = None  # username

class UserLogin(BaseModel):
    username: str
    password: str