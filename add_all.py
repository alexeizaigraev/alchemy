from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy import  Column, Integer, String
 
pg_database = "postgresql+psycopg2://postgres:postgres@localhost/alchemy"
engine = create_engine(pg_database, echo=True)
 
class Base(DeclarativeBase): pass
class Person(Base):
    __tablename__ = "people"
 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
 
Base.metadata.create_all(bind=engine)
 
with Session(autoflush=False, bind=engine) as db:
    # добавляем два объекта
    alice = Person(name="Alice", age=33)
    kate = Person(name="Kate", age=28)
    db.add_all([alice, kate])
    db.commit()

