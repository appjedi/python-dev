import pandas as pd
import pymysql
from sqlalchemy import create_engine

def MySQLEx():
# Connect to the database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='Jedi2023',
        db='appjedin_timslist',
        cursorclass=pymysql.cursors.DictCursor
    )

    # Query
    query = "SELECT * FROM transactions"

    # Load into DataFrame
    df = pd.read_sql(query, conn)

    # Close connection
    conn.close()

def SQLAlchemyEx():

    # Create engine string
    engine = create_engine("mysql+pymysql://root@localhost:3306/test")

    # Query
    query = "SELECT * FROM users"
    df = pd.read_sql(query, engine)
    print(df)

SQLAlchemyEx()