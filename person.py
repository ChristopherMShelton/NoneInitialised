from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, inspect
import json


Base = declarative_base()

class Person(Base):
     __tablename__ = 'person'

     id = Column(String, primary_key=True)
     firstname = Column(String)
     surname = Column(String)
     birthday = Column(String)


      
     def __repr__(self):
        return "<Person(firstname='%s', surname='%s', birthday='%s')>" % (
                            self.firstname, self.surname, self.birthday)
     def to_dict(self):
        return dict(firstname=self.firstname, surname=self.surname, birthday=self.birthday)
