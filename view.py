import pandas as pd
import getch
import sys


class View(object):

    # Print menu entries for selection of some column from column list
    def select_column_menu(self, table_name, columns):
        print("Select some field of table '", table_name, "':", sep="")
        counter = 1
        for column in columns:
            print("\t%d: %s" % (counter, column))
            counter += 1

    def print_table(self, table_data, on_none_message=None):
        if table_data:
            for row in table_data:
                print(list(map(lambda x: x[x.find('=')+1:], str(row).split(', '))))
        elif on_none_message:
            print(on_none_message)

    # Request some input from user. Validation can be done with list of valid cases or with lambda.
    # 'back' and 'exit' are allways valid.
    # 'exit' means exit from program
    # Very nice looking code
    def request_input(self,
                      message,
                      valid_cases=[],
                      validator=None,
                      message_on_wrong="Wrong input, try again(or enter 'back'):"):
        if validator is None:
            validator = (lambda x: (any(x is s for s in valid_cases))) if valid_cases else (lambda _: True)

        print(message, end=" ")
        while True:
            try:
                retval = input()
                if retval == 'back' or validator(retval):
                    return retval
                else:
                    print(message_on_wrong, end=" ")
            except KeyboardInterrupt:
                print("\nInterrupted by user")
                sys.exit()
            except Exception as e:
                print("Error on input:", e)

    # Print tables list (menu entries)
    def print_tables(self, tables_list):
        counter = 1
        for table in tables_list:
            print("\t", counter, ": ", table, sep="")
            counter += 1

    # Print Ok if 'is_all_ok', else print 'FAIL'
    # Then call 'getch'
    def after_action_message(self, is_all_ok):
        return self.print_and_getch("Ok" if is_all_ok else "FAIL")

    # Print some message and call 'getch'.
    # User may have some time to rest before menu loop will continue.
    def print_and_getch(self, message):
        print(message)
        return getch.getch()

    def request_input_object(self, columns):
        inputed_object = {}
        print("Let's fill some objects: ")
        for column in columns:
            print(column.name + " = ")
            value = input()
            if str(value) == "": continue
            inputed_object[column] = str(value)
        return inputed_object

    def print_main_menu(self, tables_names):
        print("################################\nSELECT TABLE")
        index = 1
        for table_name in tables_names:
            print("    " + str(index) + ". " + str(table_name))
            index += 1

        print()

    def print_table_menu(self, table_name):
        print("################################\nTABLE", table_name)
        print("    1. Select all")
        print("    2. Select some")
        print("    3. Insert")
        print("    4. Update")
        print("    5. Delete")
        print()

    def show_fetched_result(self, db_object, result):
        df = pd.DataFrame(result)
        df.columns = db_object.columns
        print(df)