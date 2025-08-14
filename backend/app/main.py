from fastapi import FastAPI

app = FastAPI(title="Baldussi API teste")

@app.get("/ping")
def ping_call():
    return {"status": "pong"}
