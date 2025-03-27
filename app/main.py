from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, services
from app.db import get_db

app = FastAPI()
tron = services.TronService()
db_service = services.DatabaseService()

@app.post("/address-info/", response_model=schemas.AddressInfoResponse)
async def get_address_info(
    request: schemas.AddressInfoRequest, 
    db: Session = Depends(get_db)
):
    try:
        info = tron.get_address_info(request.address)
        db_service.log_request(db, request.address, info)
        return info
    except Exception as e:
        db_service.log_request(db, request.address)
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/address-requests/", response_model=schemas.PaginatedResponse)
async def get_requests(
    page: int = 1,
    per_page: int = 10,
    db: Session = Depends(get_db)
):
    if page < 1 or per_page < 1:
        raise HTTPException(
            status_code=400,
            detail="Не может быть меньше 0"
        )
    result = db_service.get_requests(db, skip=(page-1)*per_page, limit=per_page)
    return {
        "items": result["items"],
        "total": result["total"],
        "page": page,
        "per_page": per_page
    }