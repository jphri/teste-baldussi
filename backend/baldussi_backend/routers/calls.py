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