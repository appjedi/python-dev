import sqlite3 as dbapi2

from movie import Movie


class Database:
    __dbfile=None
    __dbName="test"
    def __init__(self, dbfile):
        self.__dbfile = dbfile
        print ("dbName:",self.__dbfile)


    def add_movie(self, title, year):
        with dbapi2.connect(self.__dbfile) as connection:
            cursor = connection.cursor()
            # title=";truncate table users;" # SQL Injection
            query = "INSERT INTO MOVIE (TITLE, YR) VALUES (?, ?)"
            cursor.execute(query, [title, year])
            connection.commit()
            movie_key = cursor.lastrowid
        return movie_key

    def update_movie(self, movie_key, movie):
        with dbapi2.connect(self.__dbfile) as connection:
            cursor = connection.cursor()
            query = "UPDATE MOVIE SET TITLE = ?, YR = ? WHERE (ID = ?)"
            cursor.execute(query, (movie.title, movie.year, movie_key))
            connection.commit()

    def delete_movie(self, movie_key):
        with dbapi2.connect(self.__dbfile) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM MOVIE WHERE (ID = ?)"
            cursor.execute(query, (movie_key,))
            connection.commit()

    def get_movie(self, movie_key):
        print("get_movie")
        with dbapi2.connect(self.__dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT TITLE, YR FROM MOVIE WHERE (ID = ?)"
            cursor.execute(query, (movie_key,))
            title, year = cursor.fetchone()
        movie_ = Movie(title, year=year)
        return movie_

    def get_movies(self):
        movies = []
        print("get_movies")
        with dbapi2.connect(self.__dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, TITLE, YR FROM MOVIE ORDER BY ID"
            # print(query)
            cursor.execute(query)
            for movie_key, title, year in cursor:

                movies.append((movie_key, title, year))
        return movies

    def get_dbname(self):
        return self.__dbName
    
    def set_dbname(self, name):
        self.__dbName=name
    
def test():
    #print("start")
    db = Database("./movies.sqlite")
    print (db.get_dbname())
    # db.add_movie("Batman", 1997)
    rows = db.get_movies()
    for row in rows:
        print(row[1])
    print("end")
test()