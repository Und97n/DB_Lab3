from dbinterface import DBInterface
from database_helper import DatabaseHelper
import utils


class Model(object):

    def getTablesNames(self):
        return DatabaseHelper.getListOfTables()

    def getTableObject(self, table_name):
        return DatabaseHelper.getTableObject(table_name)

    def select_all(self, table_name):
        model = self.getTableObject(table_name)
        return DBInterface(model).select_all()

    def select(self, table, object_to_find):
        model = self.getTableObject(table)
        db_interface = DBInterface(model)

        mapped = utils.map_keys_and_values_from_object(object_to_find)

        if mapped is None:
            print("Aborting! mapped is None")
            return None

        return db_interface.select(mapped['columns'], mapped['values'])

    def fill_object(self, table_name, inflator_object):
        model = self.getTableObject(table_name)
        return DatabaseHelper.fill_db_object(model, inflator_object)

    def insert(self, object_to_insert):
        db_interface = DBInterface(None)
        return db_interface.insert(object_to_insert)

    def update(self, table, object_to_update, updated_object):
        model = self.getTableObject(table)
        db_interface = DBInterface(model)

        mappedFind = utils.map_keys_and_values_from_object(object_to_update)
        mappedUpdate = utils.map_keys_and_values_from_object(updated_object)

        return db_interface.update(mappedFind['columns'], mappedFind['values'], mappedUpdate['columns'], mappedUpdate['values'])

    def delete(self, table, object_to_delete):
        model = self.getTableObject(table)
        db_interface = DBInterface(model)

        mapped = utils.map_keys_and_values_from_object(object_to_delete)

        return db_interface.delete(mapped['columns'], mapped['values'])

    def rollback_session(self):
        DatabaseHelper.rollback_session()
