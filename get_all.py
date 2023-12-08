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

    # получение всех объектов
    # people = db.query(Person).all()
    # for p in people:
    #     print(f"{p.id}.{p.name} ({p.age})")
     
    # получение одного объекта по id
    first_person = db.get(Person, 1)
    print(f"{first_person.name} - {first_person.age}")  

    # фильтр
    print('-' * 10)
    people = db.query(Person).filter(Person.age > 30).all()
    for p in people:
        print(f"{p.id}.{p.name} ({p.age})")

    # первый из
    first = db.query(Person).filter(Person.id==1).first()
    print(f"{first.name} ({first.age})")    # Tom (38)