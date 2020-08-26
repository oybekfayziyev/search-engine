from pathlib import Path
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# JOIN DATABASE FOLDER NAME TO THE PATH
database = os.path.join(BASE_DIR, 'database')
post = os.path.join(BASE_DIR, 'post')
search = os.path.join(BASE_DIR, 'search')

DATABASE_NAME = 'social.db'
TABLE_NAME = 'post'


FIELDS = ['id', 'title', 'description', 'created_date']