import logging
from sqlalchemy import inspect
from app.db import engine, Base
from app.models import AddressRequest

def init_db():
    try:
        logging.info("Создание таблиц...")
        
        Base.metadata.create_all(bind=engine, tables=[AddressRequest.__table__])
        
        inspector = inspect(engine)
        if "address_requests" in inspector.get_table_names():
            logging.info("Таблица успешно создана")
            return True
        logging.error("Таблица не создана")
        return False
    except Exception as e:
        logging.error(f"Ошибка: {str(e)}")
        return False

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    import sys
    sys.exit(0 if init_db() else 1)