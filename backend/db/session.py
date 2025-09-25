from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings
from typing import Generator

sqlalchemy_database_url=settings.DATABASE_URL
print("Database URL:", sqlalchemy_database_url)  # Debugging line
engine=create_engine(sqlalchemy_database_url)




SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)



def get_db() -> Generator:   
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()