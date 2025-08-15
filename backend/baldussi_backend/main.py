from fastapi import FastAPI

import baldussi_backend.routers.calls as calls

app = FastAPI(title="Baldussi API teste")

app.include_router(calls.router)

@app.get("/ping")
def ping_call():
    return {"status": "pong"}
