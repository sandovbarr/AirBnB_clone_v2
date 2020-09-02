#!/usr/bin/python3

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from os import getenv
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    ''' create a manage session for MySQL db'''
    __engine = None
    __session = None
    classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
            }

    def __init__(self):
        ''' Constructor '''
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        if getenv('HBNB_MYSQL_HOST'):
            host = getenv('HBNB_MYSQL_HOST')
        else:
            host = 'localhost'

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def all(self, cls=None):
        ''' Query all objects in current db '''
        r_dic = {}
        if cls is not None:
            query = self.__session.query(cls)
            for res in query:
                k = res.__class__.__name__ + '.' + res.id
                r_dic[k] = res
        else:
            for k, v in DBStorage.classes.items():
                if not isinstance(v, type(BaseModel)):
                    query = self.__session.query(v).all()
                    for res in query:
                        k = res.__class__.__name__ + '.' + res.id
                        r_dic[k] = res
        return r_dic

    def new(self, obj):
        ''' add the object to the current database session '''
        self.__session.add(obj)

    def delete(self, obj=None):
        ''' delete from the current database session '''
        if obj is not None:
            self.__session.delete(obj)

    def save(self):
        '''  commit all changes of the current database session '''
        self.__session.commit()

    def reload(self):
        ''' load all data'''
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        R_Session = scoped_session(Session)
        self.__session = R_Session

    def close(self):
        ''' Close the session '''
        self.__session.remove()
