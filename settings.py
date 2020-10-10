import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(ROOT_DIR, 'notebooks', 'sqlitedb', 'movielens.db')
DATA_FILE = os.path.join(ROOT_DIR, 'data', 'data.csv')