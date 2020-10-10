import csv
import os
import re
import sqlite3
from sqlite3 import Error as SQLiteError

from settings import DB_FILE, DATA_FILE

QUERIES = {
    # Movies
    "create_table_movies": """
        CREATE TABLE IF NOT EXISTS movies (
            movie_id INTEGER NOT NULL PRIMARY KEY,
            movie_name TEXT NOT NULL,
            movie_year TEXT NOT NULL
        ) 
    """,
    
    "insert_movie": """
        INSERT INTO movies(movie_id, movie_name, movie_year)
        VALUES (?, ?, ?)
    """,
    
    # Users
    "create_table_users": """
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER NOT NULL PRIMARY KEY,
            user_gender INTEGER NOT NULL,
            CHECK( user_gender = 1 OR user_gender = 0)
        )
    """,
    
    "insert_user": """
        INSERT INTO users(user_id, user_gender)
        VALUES(?, ?)
    """,
    
    # Ratings
    "create_table_ratings": """
        CREATE TABLE IF NOT EXISTS ratings (
            user_id INTEGER NOT NULL,
            movie_id INTEGER NOT NULL,
            rating INTEGER NOT NULL,
            PRIMARY KEY (user_id, movie_id),
            CHECK ( rating > 0 AND rating <= 5),
            FOREIGN KEY (user_id)
                REFERENCES users (user_id),
            FOREIGN KEY (movie_id)
                REFERENCES movies (movie_id)
        )
    """,
    
    "insert_rating": """
        INSERT INTO ratings (user_id, movie_id, rating)
        VALUES(?, ?, ?)
    """
    }

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE)
    except SQLiteError as e:
        print(e)
    return conn
    
def create_table(conn, create_table_query):
    """
        Creates table from sql query statement.
        Input parameters:
            create_table_query: CREATE TABLE SQL query
        Return: 0 or 1: 1: success, 0: failure
    """
    operation_result = 0
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_query)
        operation_result = 1
    except SQLiteError as e:
        print(e)
    return operation_result
        

def insert_data_row(conn, insert_query, data_tuple):
    """
        Inserts data into database table using INSERT query.
        Input Parameters:
            conn - db connection
            insert_query - INSERT query
            insert_row - data tuple
        Returns: 
            lastrowid in case of success, or 0 in case of failure
    """
    try: 
        cursor = conn.cursor()
        cursor.execute(insert_query, data_tuple)
        conn.commit()
    except SQLiteError as err:
        print(err)
    return cursor.lastrowid

def process_data():
    # Number of inserted rows
    nmovies = 0
    nusers = 0
    nratings = 0
    
    # Delete DB file if exists
    if os.path.isfile(DB_FILE):
        os.remove(DB_FILE)
        
    # establish db connection
    conn = create_connection()
    if conn is None:
        print("Error: Data processing failed. Connection to DB failed.")
        return -1
        
    # Create DB Tables
    ### movies
    query = QUERIES["create_table_movies"]
    if create_table(conn, query) == 0:
        print("Failed to create table: movies")
        return -10
        
    ### users
    query = QUERIES["create_table_users"]
    if create_table(conn, query) == 0:
        print("Failed to create table: users")
        return -11
        
    ### ratings
    query = QUERIES["create_table_ratings"]
    if create_table(conn, query) == 0:
        print("Failed to create table: ratings")
        return -12
    
    # Adding data to DB tables
    movie_pattern = re.compile(r"^(\d+): (.+) \((\d{4})\)$")
    
    with open(DATA_FILE, newline='') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',', quotechar="\"")
        cnt = 0
        movie_id_list = []
        for row in datareader:
            cnt = cnt + 1
            row_data = row
            if cnt == 1:
                # adding data to movies
                for movie in row_data:
                    m = movie_pattern.match(movie)
                    if m is not None:
                        movie_id_list.append( m.group(1) )
                        movie_data = m.groups()
                        insert_query = QUERIES["insert_movie"]
                        row_id = insert_data_row(conn, insert_query, movie_data)
                        if row_id < 1:
                            print("movies: data insertion failed:")
                            print(movie_data)
                        else:
                            nmovies = nmovies + 1           
            else:
                # adding user data
                user_data = (row_data[0], row_data[1])
                insert_query = QUERIES["insert_user"]
                row_id = insert_data_row(conn, insert_query, user_data)
                if row_id < 1:
                    print("users: data insertion failed:")
                    print(user_data)
                else:
                    nusers = nusers + 1
                    
                # adding ratings data
                for i in range( len(movie_id_list) ):
                    user_id = row_data[0]
                    movie_id = movie_id_list[i]
                    if len(row_data[2+i]) > 0:
                        rating = row_data[2+i]
                        rating_data = (user_id, movie_id, rating)
                        insert_query = QUERIES["insert_rating"]
                        row_id = insert_data_row(conn, insert_query, rating_data)
                        if row_id < 1:
                            print("ratings: data insertion failed:")
                            print(rating_data)
                        else:
                            nratings = nratings + 1
    if conn:
        conn.close()
        
    print("Data processing finished successfully.")
    print("Now all the data is stored in SQLite database located in 'sqlitedb/movielens.db")
    print("Number of rows inserted to movies: {0}".format(nmovies))
    print("Number of rows inserted to users: {0}".format(nusers))
    print("Number of rows inserted to ratings: {0}".format(nratings))
    
    return 0
                    
            
if __name__ == "__main__":
    process_data()
    
            
            
    
           
        
    
    
    
    
    