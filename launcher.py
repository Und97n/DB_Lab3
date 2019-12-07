from database_helper import DatabaseHelper
from controller import Controller
from view import View
from model import Model


def main():
    controller = Controller(View(), Model())
    controller.start()
    DatabaseHelper.close()

if __name__ == '__main__':
    main()
