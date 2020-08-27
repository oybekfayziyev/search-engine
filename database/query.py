from utils.utils import get_table_elements
import sqlite3
from sqlite3 import Error
from settings import DATABASE_NAME, TABLE_NAME

DATABASE_NAME = DATABASE_NAME
TABLE_NAME = TABLE_NAME


# CREATE TABLE
class DBConnect():

    def __init__(self):

        try:         
            self.connect = sqlite3.connect(DATABASE_NAME)
        except Error as e:
            self.connect = None
            print(e)

    def create_table(self, table_name = TABLE_NAME):

        cur = self.connect.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            created_date TEXT,
            updated_date TEXT  
        );
        '''.format(table_name=table_name))

    # Show all items
    def select_all_items(self, table_name = TABLE_NAME):
        query = "SELECT * FROM {table_name}".format(table_name=table_name)
        cur = self.connect.cursor()
        cur.execute(query)
        result = cur.fetchall()

        return result
    
    # Insert data into table
    def insert_into_table(self, **kwargs):

        # getting table elements from utils 
        title, description, created_date = get_table_elements(**kwargs)
        query = "INSERT INTO {table_name}(title, description, created_date) VALUES (?, ?, ?)".format(table_name=TABLE_NAME)
        connect = self.connect
        connect.execute(query, (title, description, created_date))

        self.connect.commit()
    
    # delete post with id
    def delete_from_table(self, id, table_name = TABLE_NAME):
        query = "DELETE FROM {table_name} WHERE id = {id}".format(table_name=table_name, id=id)
        curr = self.connect.cursor()
        curr.execute(query)
        self.connect.commit()
    
    # delete all
    def delete_all_posts(self,table_name=TABLE_NAME):
        query = "DELETE FROM {table_name}".format(table_name=table_name)
        curr = self.connect.cursor()
        curr.execute(query)
        self.connect.commit()
    
    def __del__(self):
        self.connect.close()

    

