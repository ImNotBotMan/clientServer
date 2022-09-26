from dataclasses import dataclass
from mysql.connector import connect, Error
from getpass import getpass

class DataBase:

    def connect():
        try:
            connection = connect(host="localhost",user='root',passwd='212001art',);
            cursor = connection.cursor();
            cursor.execute('SHOW DATABASES')
            for db in cursor:
                print(db)
            cursor.execute('USE TODOS_LIST');
               
        except Error as e:
            print(e)

    def createDB():
        pass

    def get_list():
        pass;
    def add_item():
        pass;
    def remove_item():
        pass
    def update_item():
        pass    