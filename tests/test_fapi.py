from app.models import AddressRequest

def test_address_info_endpoint(client):
    response = client.post(
        "/address-info/",
        json={"address": "TYMBJdSk5B6k7TTG5GmQZxqZg7tL2oZKZ9"}
    )
    assert response.status_code in (200, 400)
    if response.status_code == 200:
        assert "trx_balance" in response.json()

def test_requests_pagination(client, db_session):
    db_session.add(AddressRequest(
        address="TEST1",
        bandwidth_used=100,
        bandwidth_available=500,
        energy_used=200,
        energy_available=1000,
        trx_balance=50
    ))
    db_session.commit()

    response = client.get("/address-requests/?page=1&per_page=1")
    assert response.status_code == 200
    data = response.json()
    assert len(data["items"]) == 1
    assert all(field in data["items"][0] for field in [
        "id", "address", "bandwidth_used", "energy_available"
    ])