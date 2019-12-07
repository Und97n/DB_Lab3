from database_helper import DatabaseHelper
from sqlalchemy.orm.exc import NoResultFound


class BaseDao(object):

    def __init__(self, model):
        self.database = DatabaseHelper()
        self.model = model

    def __get_filters(self, query, columns, values):
        if not isinstance(columns, list) and not isinstance(values, list):
            # single params, such as Book.table_name, 'Kotlin Coroutines'
            return query.filter(columns == values)
        else:
            assert (isinstance(columns, list) and isinstance(values, list))
            # having list of params and values
            assert (columns.__len__() == values.__len__())
            index = 0
            for column in columns:
                query = query.filter(column == values[index])
                index += 1
            return query

    def __get_update_query(self, query, columns, values):
        if not isinstance(columns, list) and not isinstance(values, list):
            # single params, such as Book.table_name, 'Kotlin Coroutines'
            return query.update({columns: values})
        else:
            assert (isinstance(columns, list) and isinstance(values, list))
            # having list of params and values
            assert (columns.__len__() == values.__len__())

            index = 0
            obj = {}
            for column in columns:
                obj[column] = values[index]
                index += 1
            query = query.update(obj)
            return query

    def select_all(self):
        session = self.database.get_session()
        result = session.query(self.model).all()
        return result

    def select(self, columns, values):
        with self.database.get_session() as session:
            with session.query(self.model) as query:
                return self.__get_filters(query, columns, values).all()

    def delete(self, columns, values):
        session = self.database.get_session()
        result = self.select(columns, values)

        assert result

        if isinstance(result, list):
            # Many objects
            for obj in result:
                try:
                    session.delete(obj)
                    session.commit()
                    return True
                except NoResultFound:
                    print("Object NOT FOUND")
        else:
            # One object
            try:
                session.delete(result)
                session.commit()
                return True
            except NoResultFound:
                session.rollback()
                print("Object NOT FOUND")

    def update(self, columnsFind, valuesFind, columnsNew, valuesNew):
        session = self.database.get_session()
        query = session.query(self.model)
        query = self.__get_filters(query, columnsFind, valuesFind)

        assert (query)
        query = self.__get_update_query(query, columnsNew, valuesNew)

        assert (query)
        session.commit()
        print("Updated - SUCCESSFUL")
        return True

    def insert(self, obj):
        session = self.database.get_session()
        try:
            session.add(obj)
            session.commit()
        except BaseException as exception:
            session.rollback()
            print(exception)
