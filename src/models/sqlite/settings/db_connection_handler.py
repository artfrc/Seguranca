import sqlite3
from sqlite3 import Connection

class __DBConnectionHandler: #pylint: disable = C0103, invalid-name
    def __init__(self):
        self.__connection_string = "storage.db"
        self.__conn = None

    def connect(self):
        self.__conn = sqlite3.connect(self.__connection_string)

    def get_connection(self) -> Connection:
        return self.__conn
    
db_connection_handler = __DBConnectionHandler()