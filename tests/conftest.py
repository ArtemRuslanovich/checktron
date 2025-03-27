import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db import Base, get_db
from app.main import app
from fastapi.testclient import TestClient
from app.models import AddressRequest

@pytest.fixture(autouse=True)
def clean_db(db_session):
    yield
    db_session.query(AddressRequest).delete()
    db_session.commit()

@pytest.fixture(scope="session")
def test_db():
    engine = create_engine(f"postgresql://artemruslanovic@localhost:5432/tron_test_db")
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def db_session(test_db):
    connection = test_db.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    
    session.autocommit = False
    
    yield session
    
    transaction.rollback()
    session.close()
    connection.close()

@pytest.fixture
def test_data(db_session):
    data = {
        "address": "TEST_1",
        "bandwidth_used": 100,
        "bandwidth_available": 500,
        "energy_used": 200,
        "energy_available": 1000,
        "trx_balance": 50
    }
    db_session.add(AddressRequest(**data))
    db_session.commit()
    return data

@pytest.fixture(autouse=True)
def clean_test_data(db_session):
    yield
    db_session.query(AddressRequest).delete()
    db_session.commit()

@pytest.fixture
def client(test_db):
    app.dependency_overrides[get_db] = lambda: sessionmaker(bind=test_db)()
    yield TestClient(app)
    app.dependency_overrides.clear()