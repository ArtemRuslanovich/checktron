from app.services import DatabaseService
from app.models import AddressRequest

def test_log_request(db_session):
    service = DatabaseService()
    address = "random123321"

    request = service.log_request(
        db_session,
        address,
        {"trx_balance": 1000}
    )

    record = db_session.query(AddressRequest).filter(
        AddressRequest.address == address
    ).first()
    
    assert record is not None
    assert record.trx_balance == 1000

def test_get_requests(db_session):
    service = DatabaseService()
    
    for i in range(3):
        db_session.add(AddressRequest(
            address=f"ADDR_{i}",
            trx_balance=i*100
        ))
    db_session.commit()
    
    result = service.get_requests(db_session, skip=1, limit=1)
    
    assert len(result["items"]) == 1
    assert result["total"] == 3
