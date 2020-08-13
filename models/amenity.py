#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship, backref
from models.place import place_amenity
import os
import models


class Amenity(BaseModel, Base):
    ''' Create amenities table '''
    __tablename__ = 'amenities'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place',
                                       secondary='place_amenity')
    else:
        name = ""
