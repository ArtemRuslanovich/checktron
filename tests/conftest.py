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

@pytest.fixture
def db_session(test_db):
    connection = test_db.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()
    
    yield session
    
    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture
def client(test_db):
    app.dependency_overrides[get_db] = lambda: sessionmaker(bind=test_db)()
    yield TestClient(app)
    app.dependency_overrides.clear()