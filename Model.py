from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///banco.db')

Session = sessionmaker()
Session.configure(bind=engine)

session = Session()

Base = declarative_base()

class Mensagens(Base):
  __tablename__ = 'mensagens'
  id = Column(Integer,primary_key=True)
  data = Column(String)
  origem = Column(String)
  assunto = Column(String)

if __name__ == '__main__':
  Base.metadata.create_all(engine)