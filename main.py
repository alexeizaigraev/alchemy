from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
  
# строка подключения
pg_database = "postgresql+psycopg2://postgres:postgres@localhost/postgres"
  
# создаем движок SqlAlchemy
engine = create_engine(pg_database, echo=True)
# создаем класс сессии
Session = sessionmaker(autoflush=False, bind=engine)
# создаем саму сессию базы данных
with Session(autoflush=False, bind=engine) as session:
    pass