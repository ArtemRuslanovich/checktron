def test_address_info_endpoint(client):
    response = client.post(
        "/address-info/",
        json={"address": "TYMBJdSk5B6k7TTG5GmQZxqZg7tL2oZKZ9"}
    )
    assert response.status_code in (200, 400)
    if response.status_code == 200:
        assert "trx_balance" in response.json()

def test_requests_pagination(client):
    response = client.get("/address-requests/?page=1&per_page=5")
    assert response.status_code == 200
    data = response.json()
    assert len(data["items"]) <= 5