from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from baldussi_backend.database import Base, engine

import baldussi_backend.routers.calls as calls
import baldussi_backend.routers.users as users

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Baldussi API teste")

app.include_router(calls.router)
app.include_router(users.router)

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou ["http://localhost:3000"] se quiser restringir
    allow_credentials=True,
    allow_methods=["*"],  # GET, POST, etc.
    allow_headers=["*"],  # Cabeçalhos permitidos
)

@app.get("/ping")
def ping_call():
    return {"status": "pong"}
