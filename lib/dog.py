from models import Dog
from sqlalchemy import (Column, Integer, String, DateTime, Index, desc, create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


def create_table(Base, engine):
    Base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name==name).first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id==id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name==name and Dog.breed==breed).first()

def update_breed(session, dog, breed):
    session.query(Dog).filter(Dog.id==dog.id).update({Dog.breed: breed})

if __name__ == '__main__':
    engine = create_engine('sqlite:///dogs.db')
    create_table(Base, engine)
    Session = sessionmaker(bind=engine)
    session = Session()