import datetime
import json 
import csv
from settings import FIELDS
fields = FIELDS


def get_table_elements(**kwargs):

    # get data elements    
    title = kwargs.get('title')
    description = kwargs.get('description') or None
    created_date = datetime.datetime.now()
    

    return title, description, created_date

def validate(text):
    if len(text) > 0:
        return text
    
    return None

def menu():
    return '''
    1. ADD POST
    2. SEARCH POST
    3. DELETE POST
    4. SEE ALL POSTS
    5. ADD POST FROM JSON
    6. DELETE ALL
    7. EXIT
    '''

def load_data_from_json(filename):
    title = []
    description = []

    with open(filename,encoding="utf8") as f:
       
        data = json.loads(f.read())

        try:
            if data['post']:                                    
                for item in data["post"]:
                    title.append(item['title'])
                    description.append(" ".join(item['description']))            
                return title, description
        except:
            return None



def save_to_csv(filename):    
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writerows()

