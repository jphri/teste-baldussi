import baldussi_backend.call_api as call_api
from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session
from baldussi_backend.database import get_db
from baldussi_backend.models import Call
from baldussi_backend.schema import KpiResponse
from baldussi_backend.auth import get_current_user
from baldussi_backend.models import User

from datetime import datetime

router = APIRouter(prefix='/calls', tags=['calls'])

@router.get('/raw')
async def raw_get_fn(_: User = Depends(get_current_user), count: int = 100, empresa_id: str | None = None):
    response = call_api.calls_raw(count, empresa_id)
    return {
        "count": len(response),
        "data": response
    }

@router.get("/get")
async def get_fn(_: User = Depends(get_current_user), page: int = 1, limit: int = 100, empresa_id: str | None = None, date_from: str | None = None, date_to: str | None = None, destino: str | None = None, sip_code: str | None = None, q: str | None = None):
    response = call_api.calls(page, limit, empresa_id, date_from, date_to, destino, sip_code)
    return response

@router.post("/ingest")
async def ingest_fn(_: User = Depends(get_current_user), db: Session = Depends(get_db)):
    calls = call_api.calls_raw(2000)
    processed = 0
    for call in calls:
        exists = db.query(Call).filter(Call.chamada_id == call["chamada_id"]).first()
        if exists:
            continue
        if call["data"]:
            call["data"] = datetime.strptime(call["data"], "%Y-%m-%d %H:%M:%S")
        if call["duracao_real"]:
            tempo = datetime.strptime(call["duracao_real"], "%H:%M:%S")
            call["duracao_real"] = tempo.hour * 3600 + tempo.minute * 60 + tempo.second
        if call["duracao"]:
            tempo = datetime.strptime(call["duracao"], "%H:%M:%S")
            call["duracao"] = tempo.hour * 3600 + tempo.minute * 60 + tempo.second
        db.add(Call(**call))
        processed += 1
    db.commit()
    return processed

@router.get("/kpi", response_model=KpiResponse)
async def kpi_fn(_: User = Depends(get_current_user), db: Session = Depends(get_db)):
    total = db.query(Call).count()
    atendidas = db.query(Call).filter(Call.motivo_desligamento == "OK").count()
    asr = 0
    acd = 0

    data = db.query(Call).filter(Call.motivo_desligamento == "OK").all()
    if atendidas > 0:
        for call in data:
            acd += call.duracao_real
        acd /= atendidas
        asr = (atendidas / total) * 100
    else:
        acd = 0
        asr = 0

    return KpiResponse(
        total=total,
        atendidas=atendidas,
        asr=asr,
        acd=acd
    )

@router.get('/calls_per_day')
async def calls_per_day(_: User = Depends(get_current_user), db: Session = Depends(get_db)):
    data = db.query(
        func.count(Call.chamada_id).label('total'),
        func.date(Call.data).label('day')
    ).group_by(
        func.date(Call.data)
    ).order_by(
        func.date(Call.data)
    )
    l = []
    for row in data:
        a = {}
        a["total"] = row.total
        a["data"] = row.day
        l.append(a)

    return l