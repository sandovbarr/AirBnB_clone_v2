#!/usr/bin/python3
""" State Module for HBNB project """
import os
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            '''
                returns the list of City instances with state_id
                equals to the current State.id
            '''
            ins_ret_list = []
            for key, obj in models.storage.all().items():
                if obj.__class__.__name__ == 'City':
                    if obj.state_id == self.id:
                        ins_ret_list.append(obj)
            return ins_ret_list
    else:
        cities = relationship('City', cascade="all, delete",
                              backref='state')
