class Controller(object):

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def start(self):
        tables = self.model.getTablesNames()
        length = int(len(tables))
        self.view.print_main_menu(tables)

        input_v = self.view.request_input("Enter number (from 1 to " + str(len(tables)) + "):",
                                          validator=lambda x: x.isdigit() and 0 < int(x) <= len(tables))
        if input_v != 'back':
            self.show_table_menu(tables[(int(input_v)+1)])

    def show_table_menu(self, table_name):
        self.view.print_table_menu(table_name)
        table_object = self.model.getTableObject(table_name)
        input_v = self.view.request_input("Enter number (from 1 to 6):", valid_cases=['1', '2', '3', '4', '5'])

        if input_v == '1':
            result = self.model.select_all(table_name)
            self.view.print_table(result, "Nothing")
            self.view.print_and_getch()
            self.show_table_menu(table_name)
        elif input_v == '2':
            filled_object = self.view.request_input_object(table_object.get_columns())
            result = self.model.select(table_name, filled_object)
            self.view.print_table(result, "Noting found")
            self.show_table_menu(table_name)
        elif input_v == '3':
            filled_object = self.view.request_input_object(table_object.get_columns())
            db_object = self.model.fill_object(table_name, filled_object)
            self.model.insert(db_object)
            self.show_table_menu(table_name)
        elif input_v == '4':
            filled_object = self.view.request_input_object(table_object.get_columns())
            updated_object = self.view.request_input_object(table_object.get_columns())
            self.model.update(table_name, filled_object, updated_object)
            self.show_table_menu(table_name)
        elif input_v == '5':
            filled_object = self.view.request_input_object(table_object.get_columns())
            self.model.delete(table_name, filled_object)
            self.show_table_menu(table_name)
        elif input_v == 'back':
            self.start()
