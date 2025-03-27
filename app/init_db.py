import logging
from sqlalchemy import create_engine
from app.db import Base
from app.config import settings

def init_db():
    try:
        engine = create_engine(settings.db_url)        
        Base.metadata.create_all(bind=engine)
        
        return True
    except Exception as e:
        logging.error(f"Ошибка инициализации БД: {str(e)}")
        return False

if __name__ == "__main__":
    import sys
    logging.basicConfig(level=logging.INFO)
    
    if init_db():
        sys.exit(0)
    else:
        sys.exit(1)