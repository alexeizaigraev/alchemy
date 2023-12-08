from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy import  Column, Integer, String
  
# строка подключения
pg_database = "postgresql+psycopg2://postgres:postgres@localhost/alchemy"
# создаем движок SqlAlchemy
engine = create_engine(pg_database, echo=True)
 
# создаем модель, объекты которой будут храниться в бд
class Base(DeclarativeBase): pass
class Person(Base):
    __tablename__ = "people"
 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
 
# создаем таблицы
Base.metadata.create_all(bind=engine)
 
# создаем сессию подключения к бд
with Session(autoflush=False, bind=engine) as db:
    # создаем объект Person для добавления в бд
    tom = Person(name="Tom", age=38)
    db.add(tom)     # добавляем в бд
    db.commit()     # сохраняем изменения
    print(tom.id)   # можно получить установленный id

