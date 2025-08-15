from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import baldussi_backend.routers.calls as calls

app = FastAPI(title="Baldussi API teste")

app.include_router(calls.router)

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
