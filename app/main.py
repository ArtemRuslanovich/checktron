from fastapi import FastAPI, Depends, HTTPException, Query
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
    page: int = Query(1, gt=0),
    per_page: int = Query(5, le=5),
    db: Session = Depends(get_db)
):
    return db_service.get_requests(db, page=page, per_page=per_page)