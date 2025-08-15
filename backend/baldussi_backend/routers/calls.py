import baldussi_backend.call_api as call_api
from fastapi import APIRouter

router = APIRouter(prefix='/calls', tags=['calls'])

@router.get('/raw')
async def raw_get_fn(count: int = 100, empresa_id: str | None = None):
    response = call_api.calls_raw(count, empresa_id)
    return {
        "count": len(response),
        "data": response
    }

@router.get("/get")
async def get_fn(page: int = 1, limit: int = 100, empresa_id: str | None = None, date_from: str | None = None, date_to: str | None = None, destino: str | None = None, sip_code: str | None = None, q: str | None = None):
    response = call_api.calls(page, limit, empresa_id, date_from, date_to, destino, sip_code)
    return response