from sqlalchemy import Column, Integer, String, String, Boolean
from baldussi_backend.database import Base

# Modelo de tabela
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    is_admin = Column(Boolean, default=False)

