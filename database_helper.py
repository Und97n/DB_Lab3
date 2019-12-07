from models import *
import sqlalchemy as db
import credentials as credentials
from sqlalchemy.orm import *
from sqlalchemy import inspect
from sqlalchemy import Boolean, BOOLEAN
from sqlalchemy.exc import NoInspectionAvailable
import utils

class DatabaseHelper(object):
    # params
    __session = None
    __engine = None

    #Using singleton pattern
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '__instance'):
            cls.__instance = super(DatabaseHelper, cls).__new__(cls)
        return cls.__instance

    #Using singleton pattern
    @classmethod
    def get_engine(cls):
        if cls.__engine is None:
            cls.__engine = engine = db.create_engine('postgresql://' + credentials.user + ':' + credentials.password + "@" +
                                                     credentials.host + ":" + credentials.port + "/" + credentials.db_name)
            print("Created database engine ", cls.__engine)
        return cls.__engine

    #Using singleton pattern
    @classmethod
    def get_session(cls):
        if cls.__session is None:
            cls.__session = Session(cls.get_engine())
            print("Database session opened")
        return cls.__session

    @classmethod
    def close(cls):
        cls.get_session().close()
        print("Database session closed")

    # Повертає інспектора для виконання запитів (engine - об'єкт для взаємодії з БД)
    @classmethod
    def __getInspector(cls):
        return inspect(cls.get_engine())

    @classmethod
    def rollback_session(cls):
        cls.get_session().rollback()

    # Повертає список таблиць у БД (engine - об'єкт для взаємодії з БД)
    @classmethod
    def getListOfTables(cls):
        inspector = cls.__getInspector()

        table_list = []

        for table_name in inspector.get_table_names():
            if table_name is None: continue
            table_list.append(table_name)

        return table_list

    @classmethod
    def getTableColumns(cls, table_name):
        inspector = cls.__getInspector()
        return inspector.get_columns(table_name)

    @classmethod
    def get_primary_keys(cls, table_name):
        inspector = cls.__getInspector()
        return inspector.get_primary_keys(table_name)

    @classmethod
    def get_foreign_keys(cls, table_name):
        inspector = cls.__getInspector()
        return inspector.get_foreign_keys(table_name)

    @classmethod
    def fill_db_object(cls, model, inflator_object):
        assert (isinstance(inflator_object, object))

        db_object = model.create()
        for key in inflator_object.keys():
            setattr(db_object, key.name, inflator_object[key])
        return db_object

    @classmethod
    def getTableObject(cls, table_name): 
        if table_name == 'promoter': 
            return promoter 
        if table_name == 'ad': 
            return ad 
        if table_name == 'theme': 
            return theme 
        if table_name == 'user': 
            return user 
        if table_name == 'user_theme': 
            return user_theme 
        if table_name == 'product': 
            return product 
        if table_name == 'session': 
            return session