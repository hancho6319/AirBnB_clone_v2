#!/usr/bin/env python3

"""
This module defines a class named FileStorage
"""


from json import dumps, loads
import os
from models.my_classes import my_classes

class DBStorage:
    """ Storage for database with SQL Alchemy and MySQL """
    __engine = None
    __session = None

    def __init__(self):
        """ Constructor for DBStorage """

        sqlDb = environ.get('HBNB_MYSQL_DB')
        sqlHost = environ.get('HBNB_MYSQL_HOST')
        sqlUser = environ.get('HBNB_MYSQL_USER')
        sqlPwd = environ.get('HBNB_MYSQL_PWD')
        sqlEnv = environ.get('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(sqlDb, sqlHost, sqlUser, sqlPwd, sqlEnv), ppp=True)

    def close(self):
        """
        Closes Session
        """
        self.__session.close()
