import requests

API_HOST="http://217.196.61.183:8080"

def health():
    result = requests.get(API_HOST+"/health")
    result.raise_for_status()
    return result.json()

def calls(page: int = 1, limit: int = 100, empresa_id: str | None = None, date_from: str | None = None, date_to: str | None = None, destino: str | None = None, sip_code: str | None = None, q: str | None = None):
    params = { }
    params["page"] = page
    params["limit"] = limit
    params["empresa_id"] = empresa_id
    params["date_from"] = date_from
    params["date_to"] = date_to
    params["destino"] = destino
    params["sip_code"] = sip_code
    params["q"] = q

    result = requests.get(API_HOST+"/calls", params)
    result.raise_for_status()
    return result.json()

def calls_raw(count: int = 100, empresa_id: str | None = None):
   params = {}
   params["count"] = count
   params["empresa_id"] = empresa_id
   
   result = requests.get(API_HOST+"/calls/raw", params)
   result.raise_for_status()
   return result.json()
