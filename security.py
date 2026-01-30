from fastapi import Request, HTTPException, status

async def verify_request(request: Request):
    api_key = request.headers.get("X-API-KEY")
    with open("apikeys.txt", "r") as f:
        valid_api_keys = [line.strip() for line in f.readlines()]
    if api_key not in valid_api_keys:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized. Invalid API key.")
    

__all__ = [
    "verify_request",
]