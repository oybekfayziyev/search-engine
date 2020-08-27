from database.query import DBConnect
import json
from utils.utils import load_data

class AddPost(DBConnect):

    def __init__(self, title = None, description=None):
        DBConnect.__init__(self)
        self.title = title
        self.description = description
    
    def get_title(self):
        return self.title
    
    def set_title(self, title):
        self.title = title
    
    def get_description(self):
        return self.description
    
    def set_description(self, description):
        self.description = description
    
    def load_data_from_json(self):
        title, description = load_data()
        self.set_title(title)
        self.set_description(description)
            
    def insert(self, title, description):
        self.insert_into_table(title = title, description = description)

    def delete(self, id):       
        self.delete_from_table(id)
    
    def delete_all(self):
        self.delete_all_posts()
        
    def get_title_and_description(self):
        title = []
        description = []
        result = self.select_all_items()

        for i in result:
            # print('i', i)
            title.append(i[1])
            description.append(i[2])
        
        return title, description

